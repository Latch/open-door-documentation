#!/usr/bin/env python3
"""Rebuild the Android and iOS API reference pages from a published SDK release.

Run it from the root of this repository, on the release's docs branch, once the SDK
release is out. Then review the diff and commit it with the rest of the docs PR.

    python3 .github/sdk-reference/generate.py                          # newest 2.4.x on docs/sdk-2.4.0
    python3 .github/sdk-reference/generate.py --android 2.4 --ios 2.4.0

iOS pages come from the DocC archive and swiftinterface in the Latch/opendoor-sdk-spm tag.
Android pages come from the Dokka HTML in the javadoc jar on Maven Central.
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
MAVEN = "https://repo1.maven.org/maven2/com/door/opendoor.android"
SPM = "https://github.com/Latch/opendoor-sdk-spm.git"
PAGES = {
    "android": "docs/OpenDOOR - Mobile SDK/android-docs/android-api-reference",
    "ios": "docs/OpenDOOR - Mobile SDK/ios-docs/ios-api-reference",
}


def run(*args):
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode:
        sys.exit(f"{' '.join(args[:3])} failed:\n{result.stdout}{result.stderr}")
    return result.stdout


def version_key(version):
    return tuple(int(part) for part in version.split("."))


def newest(versions, minor):
    matching = [v for v in versions if re.fullmatch(r"\d+(\.\d+)+", v) and version_key(v)[:2] == minor]
    return max(matching, key=version_key, default=None)


def android_versions():
    with urllib.request.urlopen(f"{MAVEN}/maven-metadata.xml", timeout=60) as response:
        return re.findall(r"<version>([^<]+)</version>", response.read().decode())


def ios_versions():
    return re.findall(r"refs/tags/([^\s^]+)$", run("git", "ls-remote", "--tags", SPM), re.MULTILINE)


def build_android(version, work):
    jar = os.path.join(work, "javadoc.jar")
    try:
        urllib.request.urlretrieve(f"{MAVEN}/{version}/opendoor.android-{version}-javadoc.jar", jar)
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise
        print(f"Android {version} has no javadoc jar on Maven Central, so its pages are left as they are.")
        return False
    dokka = os.path.join(work, "dokka")
    zipfile.ZipFile(jar).extractall(dokka)
    print(run(sys.executable, os.path.join(HERE, "android_reference.py"),
              "--dokka", dokka, "--version", version, "--out", PAGES["android"]).strip())
    return True


def build_ios(version, work):
    spm = os.path.join(work, "spm")
    run("git", "clone", "--quiet", "--depth", "1", "--branch", version, "--filter=blob:none", "--sparse", SPM, spm)
    run("git", "-C", spm, "sparse-checkout", "set", "--no-cone", "/OpenDOORCore.doccarchive/data/",
        "/OpenDOORCore.xcframework/ios-arm64/OpenDOORCore.framework/Modules/")
    interface = next((os.path.join(root, name) for root, _, names in os.walk(spm)
                      for name in names if name == "arm64-apple-ios.swiftinterface"), None)
    if interface is None:
        print(f"iOS {version} has no swiftinterface in opendoor-sdk-spm, so its pages are left as they are.")
        return False
    print(run(sys.executable, os.path.join(HERE, "ios_reference.py"),
              "--archive", os.path.join(spm, "OpenDOORCore.doccarchive"), "--interface", interface,
              "--version", version, "--out", PAGES["ios"]).strip())
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", help="minor version to document, e.g. 2.4 (default: from the branch name)")
    parser.add_argument("--android", help="Android release to use (default: the newest for the version)")
    parser.add_argument("--ios", help="iOS release tag to use (default: the newest for the version)")
    args = parser.parse_args()

    if not all(os.path.isdir(folder) for folder in PAGES.values()):
        sys.exit("Run this from the root of the docs repository.")
    # The first X.Y in the branch name: v2.4, or docs/sdk-2.4.0 for a release's docs branch.
    named = re.search(r"(?<![\d.])\d+\.\d+", run("git", "branch", "--show-current"))
    version = args.version or (named.group(0) if named else "")
    if not re.fullmatch(r"\d+\.\d+", version):
        sys.exit("Pass --version X.Y, or run this on a branch named for the version, like docs/sdk-2.4.0.")
    minor = version_key(version)

    android = args.android or newest(android_versions(), minor)
    ios = args.ios or newest(ios_versions(), minor)
    if not android and not ios:
        sys.exit(f"No {version} release is published yet.")
    with tempfile.TemporaryDirectory() as work:
        built = [name for name, release, build in (("Android", android, build_android), ("iOS", ios, build_ios))
                 if release and build(release, work)]
    if not built:
        sys.exit("Nothing was rebuilt.")
    print(f"Rebuilt the {' and '.join(built)} reference. Review the diff and commit it with the docs PR.")


if __name__ == "__main__":
    main()

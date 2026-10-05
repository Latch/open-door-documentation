# SDK reference generator

Builds the Android and iOS API reference pages from a published SDK release. Run it when you prepare the docs PR for a release, then commit the pages with the rest of the PR. Merging the PR publishes everything through ReadMe's git sync.

```bash
python3 .github/sdk-reference/generate.py
```

Run it from the root of this repository, on the docs branch for the version (for example `v2.4`), once the SDK release is out. It takes the newest Android release and iOS tag for that version; `--android` and `--ios` pick specific ones. Python 3.10 or newer, standard library only.

The pages are generated, so edits made to them directly are lost on the next run. Fix the text in the SDK's doc comments instead.

## Inputs

Both come from public release artifacts.

- **iOS**: `OpenDOORCore.doccarchive` and `arm64-apple-ios.swiftinterface` from the [`Latch/opendoor-sdk-spm`](https://github.com/Latch/opendoor-sdk-spm) tag.
- **Android**: the Dokka HTML in `opendoor.android-<version>-javadoc.jar` on Maven Central (`com.door:opendoor.android`).

## Wording

The text comes from the SDK doc comments, and those are checked before a release: detekt checks the Android public API and SwiftLint checks the iOS one. The docs themselves are checked by Vale on every pull request (`.github/vale`).

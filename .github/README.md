# OpenDOOR developer docs

The source of [developers.door.com](https://developers.door.com). ReadMe syncs this repository both ways: each `vX.Y` branch is the docs version X.Y, and merging into a branch publishes it. Edits made in the ReadMe editor come back as commits on the branch.

## Mobile SDK API reference

The Android and iOS API reference pages (`android-api-reference/` and `ios-api-reference/` under `docs/OpenDOOR - Mobile SDK`) are generated from each SDK release. Nobody writes them by hand.

How a release gets its pages:

1. **The text starts in the SDK's doc comments.** Before a release, detekt (Android) and SwiftLint (iOS) reject comments that describe how the SDK works inside rather than how it behaves.
2. **The release publishes the docs with the SDK.**
   - Android: Maven Central gets `opendoor.android-<version>-javadoc.jar`, the Dokka HTML of the public API.
   - iOS: the [`Latch/opendoor-sdk-spm`](https://github.com/Latch/opendoor-sdk-spm) tag carries `OpenDOORCore.doccarchive` and the framework's `.swiftinterface`.
3. **The release docs PR rebuilds the pages.** Each release gets one docs branch, cut from its version's branch (for example `docs/sdk-2.4.0` from `v2.4`). Once the release is out, run this on it:

   ```bash
   python3 .github/sdk-reference/generate.py
   ```

   It downloads both releases' docs and rewrites the two reference folders, keeping the page layout and URLs. Commit the result with the rest of the PR. `--android` and `--ios` pick specific releases. It needs Python 3.10 or newer and nothing else.
4. **Merging the PR publishes the pages.**

To change what a reference page says, fix the SDK doc comment and ship it in a release, then regenerate. Edits made to the pages directly, in git or in the ReadMe editor, are lost on the next run.

The 2.1, 2.2 and 2.3 pages predate this and were written by hand.

## Wording check

Every pull request runs Vale over the Mobile SDK docs (rules in `.github/vale`). The docs are partner-facing, so they describe behavior only. The check fails on internal names, the backend, storage technology, internal logging and sync mechanics, and how the SDK is built. Code samples and links aren't checked.

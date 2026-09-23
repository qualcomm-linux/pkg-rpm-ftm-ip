<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# ftm-ip RPM - CentOS Stream 10

ftm-ip provides network access to Qualcomm WLAN Factory Test Mode (FTM).
The ftmdaemon-ip daemon lets test clients communicate with a device over
IP to perform WLAN factory testing.

This branch contains the CentOS Stream 10 RPM packaging for ftm-ip from the Qualcomm Linux `260825/prebuilt_yocto` release tarball.

## Package

| Field | Value |
|---|---|
| Package | ftm-ip |
| Summary | WLAN Factory Test Mode daemon with an IP interface |
| Version | 1.0.2 |
| Source | qcom-ftm-ip_1.0_armv8-2a.tar.gz |
| Source checksum | See sources |

The Yocto source archive version (`1.0`) is tracked separately from the RPM version.

The prebuilt payload installs:

- /usr/bin/ftmdaemon-ip
- /usr/bin/ftm_ip

License documents from the prebuilt archive are installed under
`/usr/share/licenses/ftm-ip/` and marked as license files in the RPM:

- `NO.LOGIN.BINARY.LICENSE.QTI`

The original copy is retained under `/usr/share/doc/qcom-ftm-ip/`.

The Yocto executable links to libbsd and GLib in addition to libnl and glibc.
RPM records these shared-library dependencies automatically.

## Files

- ftm-ip.spec
- sources
- .github/workflows/build-on-pr.yml
- .github/workflows/pkg-release.yml

Do not commit source tarballs or built RPMs. The source tarball is resolved from the dist-git `sources` file and the spec `Source0` URL.

## Build

Local validation can be run with qcom-rpm-utils:

    /path/to/qcom-rpm-utils/scripts/build-rpm.sh \
      --tarball /path/to/qcom-ftm-ip_1.0_armv8-2a.tar.gz \
      --spec ftm-ip.spec \
      --output /path/to/output

For CI, open a PR against this c10s branch. The build-on-pr workflow builds RPM artifacts but does not publish them.

## Release

After the PR is merged, run Actions -> Release on the c10s branch. The release workflow publishes the generated RPMs to Artifactory after approval.

%global debug_package %{nil}
%global source_version 1.0

Name:           ftm-ip
Version:        1.0.2
Release:        1%{?dist}
Summary:        WLAN Factory Test Mode daemon with an IP interface

License:        Qualcomm.nologin.binaries.license
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260825/prebuilt_yocto/qcom-%{name}_%{source_version}_armv8-2a.tar.gz

ExclusiveArch:  aarch64

%description
ftm-ip provides network access to Qualcomm WLAN Factory Test Mode (FTM).
The ftmdaemon-ip daemon lets test clients communicate with a device over
IP to perform WLAN factory testing.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}/
ln -s ftmdaemon-ip %{buildroot}%{_bindir}/ftm_ip
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files
%license usr/share/doc/qcom-%{name}/NO.LOGIN.BINARY.LICENSE.QTI

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.2-1
- Initial prebuilt RPM packaging

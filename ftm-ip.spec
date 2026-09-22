%global debug_package %{nil}

Name:           ftm-ip
Version:        1.0.2
Release:        1%{?dist}
Summary:        WLAN Factory Test Mode daemon over IP

License:        Qualcomm.nologin.binaries.license
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260630.1/prebuilt_noble/ftmdaemon-ip_%{version}_arm64.tar.gz

ExclusiveArch:  aarch64

%description
ftm-ip is packaged from a Qualcomm Linux release tarball.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a data/ftmdaemon-ip/arm64/. %{buildroot}/
ln -s ftmdaemon-ip %{buildroot}%{_bindir}/ftm_ip
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.2-1
- Initial prebuilt RPM packaging

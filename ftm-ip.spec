%global debug_package %{nil}

Name:           ftm-ip
Version:        1.0.2
Release:        1%{?dist}
Summary:        WLAN Factory Test Mode daemon over IP

License:        Qualcomm-Technologies-Inc.-Proprietary
Source0:        %{name}-prebuilt-%{version}.tar.gz

ExclusiveArch:  aarch64

%description
ftm-ip is packaged from a prebuilt payload tarball for Qualcomm Linux platforms.

%prep
%autosetup -n %{name}-prebuilt-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a . %{buildroot}/
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.2-1
- Initial prebuilt RPM packaging

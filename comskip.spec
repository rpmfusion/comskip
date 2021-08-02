%global _lto_cflags %{nil}
# suppress gcc-10 FTBFS
%define _legacy_common_support 1
Name:           comskip
Version:        0.82.009
Release:        5%{?dist}
Summary:        A free commercial detector
License:        GPLv2+
URL:            https://github.com/erikkaashoek/Comskip
Source0:        %{url}/archive/%{version}/Comskip-%{version}.tar.gz

BuildRequires:  libtool
BuildRequires:  argtable-devel
BuildRequires:  ffmpeg-devel

%description
Comskip is a free commercial detector written by erikkaashoek

%prep
%autosetup -p1 -n Comskip-%{version}

%build
./autogen.sh
# suppress deprecated-declarations
export CFLAGS='%{optflags} -Wno-deprecated-declarations'
%configure --disable-gui
%make_build

%install
%make_install

%files
%license LICENSE
%{_bindir}/comskip

%changelog
* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.82.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.82.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 0.82.009-3
- Rebuilt for new ffmpeg snapshot

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.82.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 14 2020 leigh123linux <leigh123linux@googlemail.com> - 0.82.009-1
- Update to 0.82.009

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.82.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 0.82.003-6
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.82.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.82.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 17 2018 mprahl <mprahl@redhat.com> - 0.82.003-3
- Explicitly disable the GUI
- Fix compilation errors with newer ffmpeg versions

* Sat Jan 27 2018 mprahl <mprahl@redhat.com> - 0.82.003-2
- Removed unneeded dependencies

* Tue Dec 12 2017 Matt Prahl <mprahl@redhat.com> - 0.82.003-1
- Initial release


%global date 20231230
%global commit 109b5d10b086d299d7e43878ccc7951cb7133ed8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           comskip
Version:        0.82.011
Release:        0.7.%{date}git%{shortcommit}%{?dist}
Summary:        A free commercial detector
License:        GPL-2.0-or-later
URL:            https://github.com/erikkaashoek/Comskip
Source0:        %{url}/archive/%{commit}/Comskip-%{commit}.tar.gz

BuildRequires:  libtool
BuildRequires:  argtable-devel
%if 0%{?fedora} && 0%{?fedora} > 35
BuildRequires:  compat-ffmpeg4-devel
%else
BuildRequires:  ffmpeg-devel
%endif

%description
Comskip is a free commercial detector written by erikkaashoek

%prep
%autosetup -p1 -n Comskip-%{commit}
NOCONFIGURE=1 ./autogen.sh

%build
export PKG_CONFIG_PATH="%{_libdir}/compat-ffmpeg4/pkgconfig"
%configure --disable-gui
%make_build

%install
%make_install

%files
%license LICENSE
%{_bindir}/comskip

%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.82.011-0.7.20231230git109b5d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 01 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.82.011-0.6.20231230git109b5d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 10 2024 Antonio Trande <sagitter@fedoraproject.org> - 0.82.011-0.5.20231230git109b5d1
- Update to commit 109b5d1

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.82.011-0.4.20220225git9900227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.82.011-0.3.20220225git9900227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.82.011-0.2.20220225git9900227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sun Mar 06 2022 Leigh Scott <leigh123linux@gmail.com> - 0.82.011-0.1.20220225git9900227
- Update to git snapshot
- Switch to compat-ffmpeg4

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.82.009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 0.82.009-6
- Rebuilt for new ffmpeg snapshot

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


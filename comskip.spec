Name:           comskip
Version:        0.82.003
Release:        5%{?dist}
Summary:        A free commercial detector
License:        GPLv2+
URL:            https://github.com/erikkaashoek/Comskip
Source0:        %{url}/archive/v%{version}.tar.gz
Patch0:         0001-Added-AM_PROG_CC_C_O-for-missing-legacy-source.patch
Patch1:		0002-replace-deprecated-CODEC_FLAG_GRAY.patch
Patch2:		0003-Allow-GUI-to-be-explicitly-enabled-or-disabled-with-.patch

BuildRequires:  libtool
BuildRequires:  argtable-devel
BuildRequires:  ffmpeg-devel

%description
Comskip is a free commercial detector written by erikkaashoek

%prep
%autosetup -p1 -n Comskip-%{version}

%build
# The version wasn't updated in the configure.ac file
sed -i "s/0.81.098/%{version}/" configure.ac
./autogen.sh
%configure --disable-gui
%make_build

%install
%make_install

%files
%license LICENSE
%{_bindir}/comskip

%changelog
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


%define		_rc	pre9
Summary:	ksquirrel-libs - a set of image decoders
Summary(pl):	ksquirrel-libs - zestaw dekoder�w obrazk�w
Name:		ksquirrel-libs
Version:	0.6.0
Release:	0.%{_rc}.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}-%{_rc}.tar.bz2
# Source0-md5:	47fca33edc543f60f2045651bb2033ed
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.1.9
BuildRequires:	jasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpixman-devel
BuildRequires:	libpng-devel
BuildRequires:	libsvg-cairo-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	libwmf-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ksquirrel-libs is a set of image decoders.
- It contains regular libraries for KSquirrel.
- It contains different image decoders for JPEG, PNG, BMP, TIFF etc.

You can use ksquirrel-libs in other projects, just write your own
mechanism that could use libraries.

%description -l pl
ksquirrel-libs jest zestawem dekoder�w obrazk�w.
- Zawiera normalne biblioteki dla KSquirrela.
- Zawiera r�ne dekodery obraz�w: JPEG, PNG, BMP, TIFF itd.

Mo�na u�ywa� ksquirrel-libs w innych projektach. Wystarczy tylko
napisa� w�asny mechanizm, kt�ry b�dzie potrafi� ich u�ywa�.

%prep
%setup -q

%build
%configure \
	--libdir=%{_libdir}/ksquirrel-libs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/ksquirrel-libs/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/html/*.{css,gif,html,png}
%dir %{_libdir}/ksquirrel-libs
%attr(755,root,root) %{_libdir}/ksquirrel-libs/*.so
%{_libdir}/ksquirrel-libs/rgbmap
%{_libdir}/ksquirrel-libs/version

#
#TODO:
# - make xorg deps
#
Summary:	ksquirrel-libs - a set of image decoders
Summary(pl):	ksquirrel-libs - zestaw dekoderów obrazków
Name:		ksquirrel-libs
Version:	0.6.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}.tar.bz2
# Source0-md5:	19f8e31da699c10bdbbcf2a33c9ce947
Patch0:		%{name}-pkgconfigdir.patch
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
ksquirrel-libs jest zestawem dekoderów obrazków.
- Zawiera normalne biblioteki dla KSquirrela.
- Zawiera ró¿ne dekodery obrazów: JPEG, PNG, BMP, TIFF itd.

Mo¿na u¿ywaæ ksquirrel-libs w innych projektach. Wystarczy tylko
napisaæ w³asny mechanizm, który bêdzie potrafi³ ich u¿ywaæ.

%package devel
Summary:	Header files for ksquirrel-libs
Summary(pl):	Nag³ówki biblioteki ksquirrel-libs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ksquirrel-libs.

%description devel -l pl
Nag³ówki biblioteki ksquirrel-libs.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_libdir}/ksquirrel-libs/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/html/*.{css,gif,html,png}
%dir %{_libdir}/ksquirrel-libs
%attr(755,root,root) %{_libdir}/ksquirrel-libs/*.so
%attr(755,root,root) %{_libdir}/ksquirrel-libs/libkls*.so.*.*.*
%attr(755,root,root) %{_libdir}/ksquirrel-libs/libksquirrel-libs.so.*.*.*
%{_datadir}/ksquirrel-libs/rgbmap

%files devel
%defattr(644,root,root,755)
%{_includedir}/ksquirrel-libs
%{_pkgconfigdir}/*.pc

#
#TODO:
# - add support for:
#   b) vec2web - http://www.ribbonsoft.com/vec2web.html
# - check if they work - ksquirrel doesnt work for me
#
Summary:	ksquirrel-libs - a set of image decoders
Summary(pl.UTF-8):	ksquirrel-libs - zestaw dekoderów obrazków
Name:		ksquirrel-libs
Version:	0.7.3
Release:	1
License:	LGPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}.tar.bz2
# Source0-md5:	059e1f0ca8f7e4f3aceb36baf6749810
Patch0:		kde-ac260-lt.patch
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	freetype-devel >= 2.1.9
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	jasper-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libwmf-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Suggests:	djvulibre
Suggests:	librsvg
Suggests:	medcon
Suggests:	netpbm-progs
Suggests:	transfig
#Suggests:	vec2web
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ksquirrel-libs is a set of image decoders.
- It contains regular libraries for KSquirrel.
- It contains different image decoders for JPEG, PNG, BMP, TIFF etc.

You can use ksquirrel-libs in other projects, just write your own
mechanism that could use libraries.

%description -l pl.UTF-8
ksquirrel-libs jest zestawem dekoderów obrazków.
- Zawiera normalne biblioteki dla KSquirrela.
- Zawiera różne dekodery obrazów: JPEG, PNG, BMP, TIFF itd.

Można używać ksquirrel-libs w innych projektach. Wystarczy tylko
napisać własny mechanizm, który będzie potrafił ich używać.

%package devel
Summary:	Header files for ksquirrel-libs
Summary(pl.UTF-8):	Nagłówki biblioteki ksquirrel-libs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for ksquirrel-libs.

%description devel -l pl.UTF-8
Nagłówki biblioteki ksquirrel-libs.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C admin cvs
%configure \
	DJVU=/usr/bin/ddjvu \
	ILBMTOPPM=/usr/bin/ilmbtoppm \
	LEAFTOPPM=/usr/bin/leaftoppm \
	MACTOPBM=/usr/bin/macptopbm \
	MEDCON=/usr/bin/medcon \
	NEOTOPPM=/usr/bin/neotoppm \
	PI1TOPPM=/usr/bin/pi1toppm \
	PI3TOPPM=/usr/bin/pi3topbm \
	PICTTOPPM=/usr/bin/picttoppm \
	UTAHTOPNM=/usr/bin/rletopnm \
	RSVG=/usr/bin/rsvg-convert \
	VEC2WEB=/usr/bin/vec2web \
	XFIG=/usr/bin/fig2dev \
	XIMTOPPM=/usr/bin/ximtoppm
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
%doc AUTHORS COPYING README doc/html/*.{css,gif,html,png}
%attr(755,root,root) %{_bindir}/ksquirrel-libs-*
%attr(755,root,root) %{_libdir}/libksquirrel-libs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libksquirrel-libs.so.0
%attr(755,root,root) %{_libdir}/libksquirrel-libs-png.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libksquirrel-libs-png.so.0
%dir %{_libdir}/ksquirrel-libs
%attr(755,root,root) %{_libdir}/ksquirrel-libs/libkls_*.so*
%dir %{_datadir}/ksquirrel-libs
%{_datadir}/ksquirrel-libs/*.ui
%{_datadir}/ksquirrel-libs/rgbmap

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libksquirrel-libs.so
%attr(755,root,root) %{_libdir}/libksquirrel-libs-png.so
%{_libdir}/libksquirrel-libs.la
%{_libdir}/libksquirrel-libs-png.la
%{_includedir}/ksquirrel-libs
%{_pkgconfigdir}/ksquirrellibs.pc

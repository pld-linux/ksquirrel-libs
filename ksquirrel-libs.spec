#
#TODO:
# - make xorg deps
#
%define		_pre	pre2
Summary:	ksquirrel-libs - a set of image decoders
Summary(pl.UTF-8):	ksquirrel-libs - zestaw dekoderów obrazków
Name:		ksquirrel-libs
Version:	0.7.0
Release:	0.%{_pre}.1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}-%{_pre}.tar.bz2
# Source0-md5:	2f49743848f386c3c52c19431ddcd772
Patch0:		%{name}-pkgconfigdir.patch
Patch1:		kde-ac260.patch
Patch2:		%{name}-am110.patch
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.1.9
BuildRequires:	giflib-devel
BuildRequires:	jasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpixman-devel
BuildRequires:	libpng-devel
BuildRequires:	libsvg-cairo-devel
BuildRequires:	libtiff-devel
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

%description devel
Header files for ksquirrel-libs.

%description devel -l pl.UTF-8
Nagłówki biblioteki ksquirrel-libs.

%prep
%setup -q -n %{name}-%{version}-%{_pre}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
#cp -f /usr/share/automake/config.sub admin
#%{__make} -f admin/Makefile.common cvs

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_libdir}/ksquirrel-libs/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/html/*.{css,gif,html,png}
%attr(755,root,root) %{_bindir}/ksquirrel-libs-*
%dir %{_libdir}/ksquirrel-libs
%attr(755,root,root) %{_libdir}/ksquirrel-libs/*.so
%attr(755,root,root) %{_libdir}/ksquirrel-libs/libkls*.so.*.*.*
%attr(755,root,root) %{_libdir}/libksquirrel-libs.so*
%dir %{_datadir}/ksquirrel-libs
%{_datadir}/ksquirrel-libs/rgbmap

%files devel
%defattr(644,root,root,755)
%{_includedir}/ksquirrel-libs
%{_prefix}/lib/pkgconfig/*.pc
#%{_pkgconfigdir}/*.pc

Summary:	ksquirrel-libs - a set of image decoders
Summary(pl):	ksquirrel-libs - zestaw dekoderów obrazków
Name:		ksquirrel-libs
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}.tar.bz2
# Source0-md5:  4bc3d75b443c8ff6f3a5427cc4164ca9
Patch0:		%{name}-gif.patch
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
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

%prep
%setup -q 
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%configure \
	--libdir=%{_libdir}/ksquirrel
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/ksquirrel
%attr(755,root,root) %{_libdir}/ksquirrel/*.so

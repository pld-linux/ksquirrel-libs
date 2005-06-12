Summary:	Graphics file browser utility - libraries
Summary(pl):	Narzêdzie do przegl±dania plików graficznych - biblioteki
Name:		ksquirrel-libs
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ksquirrel/%{name}-%{version}.tar.bz2
# Source0-md5:  4bc3d75b443c8ff6f3a5427cc4164ca9
URL:		http://ksquirrel.sourceforge.net/
BuildRequires:  XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  rpmbuild(macros) >= 1.197
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries to KSquirrel.

%description -l pl
KSquirrel - biblioteki.

%prep
%setup -q 

%build
%configure
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
%{_libdir}/FIXME

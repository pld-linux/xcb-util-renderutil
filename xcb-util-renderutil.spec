Summary:	XCB util-renderutil module
Summary(pl.UTF-8):	Moduł XCB util-renderutil
Name:		xcb-util-renderutil
Version:	0.3.9
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	468b119c94da910e1291f3ffab91019a
URL:		http://xcb.freedesktop.org/XcbUtil/
BuildRequires:	gperf
BuildRequires:	libxcb-devel >= 1.4
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	xcb-proto >= 1.6
Conflicts:	xcb-util < 0.3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

XCB util-renderutil module provides the following library:
- renderutil: Convenience functions for the Render extension.

%description -l pl.UTF-8
xcb-util udostępnia wiele bibliotek opartych powyżej libxcb (głównej
biblioteki protokołu X) oraz trochę bibliotek rozszerzeń. Te
eksperymentalne biblioteki udostępniają wygodne funkcje i interfejsy
czyniące surowy protokół X bardziej używalnym. Niektóre biblioteki
udostępniają także kod kliencki nie będący ściśle częścią protokołu X,
ale tradycyjnie dostarczany przez Xlib.

Moduł XCB util-renderutil udostępnia następującą biliotekę:
- renderutil: wygodne funkcje do rozszerzenia Render.

%package devel
Summary:	Header files for XCB util-renderutil library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XCB util-renderutil
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxcb-devel >= 1.4
Conflicts:	xcb-util-devel < 0.3.8

%description devel
Header files for XCB util-renderutil library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XCB util-renderutil.

%package static
Summary:	Static XCB util-renderutil library
Summary(pl.UTF-8):	Statyczna biblioteka XCB util-renderutil
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XCB util-renderutil library.

%description static -l pl.UTF-8
Statyczna biblioteka XCB util-renderutil.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxcb-render-util.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxcb-render-util.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-render-util.so
%{_libdir}/libxcb-render-util.la
%{_includedir}/xcb/xcb_renderutil.h
%{_pkgconfigdir}/xcb-renderutil.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxcb-render-util.a

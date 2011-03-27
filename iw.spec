Summary:	iw - utility to show or manipulate wireless devices and their configuration
Summary(pl.UTF-8):	iw - narzędzie do wyświetlania i modyfikowania konfiguracji urządzeń bezprzewodowych
Name:		iw
Version:	0.9.21
Release:	2
License:	BSD
Group:		Networking/Admin
Source0:	http://wireless.kernel.org/download/iw/%{name}-%{version}.tar.bz2
# Source0-md5:	726db5f1fd6bc316434414770513ef81
URL:		http://wireless.kernel.org/en/users/Documentation/iw
BuildRequires:	libnl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
iw is a new nl80211 based CLI configuration utility for wireless
devices.

%description -l pl.UTF-8
iw to nowe, oparte na sterowniku nl80211, działające z linii poleceń
narzędzie do konfiguracji urządzeń bezprzewodowych.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install iw $RPM_BUILD_ROOT%{_sbindir}
install iw.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_sbindir}/iw
%{_mandir}/man8/iw.8*

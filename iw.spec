Summary:	iw - utility to show or manipulate wireless devices and their configuration
Summary(pl.UTF-8):	iw - narzędzie do wyświetlania i modyfikowania konfiguracji urządzeń bezprzewodowych
Name:		iw
Version:	4.9
Release:	1
License:	BSD
Group:		Networking/Admin
Source0:	https://www.kernel.org/pub/software/network/iw/%{name}-%{version}.tar.xz
# Source0-md5:	02d36655b45a0288feb0e87e461e365a
URL:		http://wireless.kernel.org/en/users/Documentation/iw
BuildRequires:	libnl-devel >= 1:3.2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

sed -i -e 's#git rev-parse#false#g' version.sh

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

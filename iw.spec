Summary:	nl80211 based CLI
Name:		iw
Version:	0.9.19
Release:	1
License:	BSD
Group:		Networking/Admin
Source0:	http://wireless.kernel.org/download/iw/%{name}-%{version}.tar.bz2
# Source0-md5:	3b88743f9c6ce8a7e2f5fd7d18fdea42
URL:		http://wireless.kernel.org/en/users/Documentation/iw
BuildRequires:	libnl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
iw is a new nl80211 based CLI configuration utility for wireless
devices.

%prep
%setup -q

%build
%{__make} \
	V=1 \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install iw $RPM_BUILD_ROOT%{_sbindir}
install iw.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

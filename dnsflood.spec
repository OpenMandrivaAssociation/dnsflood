Summary:	DNS Flood Detector
Name:		dnsflood
Version:	1.12
Release:	%mkrel 6
License:	GPL
Group:		System/Servers
URL:		http://www.adotout.com/dnsflood.html
Source0:	http://www.adotout.com/%{name}-%{version}.tar.bz2
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
DNS Flood Detector was developed to detect abusive usage levels on high traffic
nameservers and to enable quick response to the use of one's nameserver to
facilitate spam.

%prep

%setup -q -n dns_flood_detector

cp %{SOURCE1} %{name}.init
cp %{SOURCE2} %{name}.sysconfig

%build
%serverbuild

gcc $CFLAGS -D_BSD_SOURCE -lpcap -lpthread -lm -o dns_flood_detector dns_flood_detector.c

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_sysconfdir}/sysconfig

install -m0755 dns_flood_detector %{buildroot}%{_sbindir}/
install -m0755 %{name}.init %{buildroot}%{_initrddir}/%{name}
install -m0644 %{name}.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/dns_flood_detector

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%config(noreplace) %{_sysconfdir}/sysconfig/dns_flood_detector
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0755,root,root) %{_sbindir}/dns_flood_detector

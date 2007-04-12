Summary:	DNS Flood Detector
Name:		dnsflood
Version:	1.12
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://www.adotout.com/dnsflood.html
Source0:	http://www.adotout.com/%{name}-%{version}.tar.bz2
Source1:	%{name}.init.bz2
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:	libpcap-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-root

%description
DNS Flood Detector was developed to detect abusive usage levels on
high traffic nameservers and to enable quick response to the use
of one's nameserver to facilitate spam.

%prep

%setup -q -n dns_flood_detector

bzcat %{SOURCE1} > %{name}.init

%build

#make \
#    CFLAGS="%{optflags} -D_BSD_SOURCE" \
#    LDLIBS="-lpcap -lpthread -lm"

gcc %{optflags} -D_BSD_SOURCE -lpcap -lpthread -lm -o  dns_flood_detector dns_flood_detector.c

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_initrddir}

install -m0755 dns_flood_detector %{buildroot}%{_sbindir}/
install -m0755 %{name}.init %{buildroot}%{_initrddir}/%{name}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0755,root,root) %{_sbindir}/dns_flood_detector



Summary:	DNS Flood Detector
Name:		dnsflood
Version:	1.12
Release:	8
License:	GPL
Group:		System/Servers
URL:		https://www.adotout.com/dnsflood.html
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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.12-7mdv2011.0
+ Revision: 617851
- the mass rebuild of 2010.0 packages

* Sun Oct 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.12-6mdv2010.0
+ Revision: 453456
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.12-5mdv2009.1
+ Revision: 298245
- rebuilt against libpcap-1.0.0

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.12-4mdv2009.0
+ Revision: 266569
- rebuild early 2009.0 package (before pixel changes)

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - LSB-compatible init script

* Tue Mar 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.12-2mdv2008.1
+ Revision: 188542
- fix typo
- use a better initscript

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.12-1mdv2008.1
+ Revision: 136367
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.12-1mdv2007.0
+ Revision: 101648
- Import dnsflood

* Sun Mar 05 2006 Oden Eriksson <oeriksson@mandriva.com> 1.12-1mdk
- 1.12 (Minor feature enhancements)

* Sat Jan 14 2006 Oden Eriksson <oeriksson@mandriva.com> 1.11-1mdk
- 1.11

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10-2mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Sat Nov 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.10-1mdk
- 1.10


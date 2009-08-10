Summary:	Script to download and run some unofficial clamav signatures
Summary(pl.UTF-8):	Skrypt do ściągania i uruchamiania kilku nieoficjalnych sygnatur do clamav
Name:		clamav-unofficial-sigs
Version:	3.5.4
Release:	0.1
License:	BSD-like
Group:		Applications/Databases
Source0:	http://www.inetmsg.com/pub/%{name}.tar.gz
# Source0-md5:	18dfec4fa44df9c1a300d01be923637d
URL:		http://www.sanesecurity.co.uk/download_scripts_linux.htm
Requires:	rsync
Requires:	clamav
Requires:	crond
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package contains script and configuration files that provide the capability
to download, test, and update the 3rd-party signature databases provide by
Sanesecurity (www.sanesecruity.com), MSRBL (www.msrbl.com), SecuriteInfo
(http://www.securiteinfo.com/services/clamav_unofficial_malwares_signatures.shtml),
MalwarePatrol (www.malware.com.br), and OITC (http://www.oitc.com/winnow/clamsigs).

%description -l pl.UTF-8
Pakiet zawiera skrypt i pliki konfiguracyjne umożliwiające ściąganie,
testowanie, aktualizowanie sygnatur dla clamav dostarczonych przez Sanesecurity
(www.sanesecruity.com), MSRBL (www.msrbl.com), SecuriteInfo
(http://www.securiteinfo.com/services/clamav_unofficial_malwares_signatures.shtml),
MalwarePatrol (www.malware.com.br), i OITC (http://www.oitc.com/winnow/clamsigs).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}/{logrotate.d,cron.d}}
install clamav-unofficial-sigs.sh clamd-status.sh $RPM_BUILD_ROOT%{_sbindir}
install clamav-unofficial-sigs.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install clamav-unofficial-sigs.conf $RPM_BUILD_ROOT%{_sysconfdir}
install clamav-unofficial-sigs-cron $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/%{name}
install clamav-unofficial-sigs-logrotate $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}

sed -e 's@/usr/local/bin/@%{_sbindir}/@g' -e 's@/usr/local/etc/@%{_sysconfdir}/@g' -i $RPM_BUILD_ROOT%{_sysconfdir}/*.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL LICENSE CHANGELOG

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_sbindir}/*
%{_sysconfdir}/*/%{name}
%{_mandir}/man8/*

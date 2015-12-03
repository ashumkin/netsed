Name:		netsed
Version:	1.4
Release:	1%{?dist}
Summary:	Netsed, the network packet stream editor.

Group:		System Environment/Base
License:	GPL
URL:		http://silicone.homelinux.org/projects/netsed/
Source0:	netsed-%{version}.tar.gz
Packager:	Alexey Shumkin <alex.crezoff@gmail.com>

%define debug_package %{nil}

%description
This program allows to modify TCP/IP or UDP traffic "on the fly".


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
%make_install PREFIX=%{_prefix}

%files
/usr/bin/netsed

%doc README NEWS TODO LICENSE



%changelog


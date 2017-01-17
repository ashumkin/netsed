Name:		netsed-ashumkin-mod
Version:	1.4
Release:	1%{?dist}
Summary:	A tool to modify network packets

Group:		System Environment/Base
License:	GPLv2+
URL:		http://github.com/ashumkin/netsed
Source0:	netsed-ashumkin-mod-%{version}.tar.gz
Packager:	Alexey Shumkin <alex.crezoff@gmail.com>

%define debug_package %{nil}

%description
NetSED is small and handful utility designed to alter the contents of
packets forwarded through your network in real time. It is really useful
for network hackers in following applications:

* black-box protocol auditing - whenever there are two or more
  proprietary boxes communicating over undocumented protocol (by enforcing
  changes in ongoing transmissions, you will be able to test if tested
  application is secure),
* fuzz-alike experiments, integrity tests - whenever you want to test
  stability of the application and see how it ensures data integrity,
* other common applications - fooling other people, content filtering,
  etc - choose whatever you want to.


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


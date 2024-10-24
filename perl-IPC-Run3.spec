%define modname	IPC-Run3

Summary:	Run a subprocess in batch mode (a la system)

Name:		perl-%{modname}
Version:	0.049
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/IPC::Run3
Source0:	http://www.cpan.org/modules/by-module/IPC/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-devel

%description
IPC::Run3 allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed. 

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided. 

%prep
%autosetup -p1 -n %{modname}-%{version}
perl -pi -e 's#/usr/local/bin/#%{_bindir}/#' bin/run3profpp

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install
mkdir -p %{buildroot}/%{_bindir}
cp bin/* %{buildroot}/%{_bindir}
chmod 0755 %{buildroot}/%{_bindir}/*

%files
%doc Changes META.yml
%{_bindir}/*
%{perl_vendorlib}/IPC
%{_mandir}/man3/*

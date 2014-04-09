%define modname	IPC-Run3
%define modver 0.048

Summary:	Run a subprocess in batch mode (a la system)

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/IPC/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
IPC::Run3 allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed. 

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided. 

%prep
%setup -qn %{modname}-%{modver}
perl -pi -e 's#/usr/local/bin/#%{_bindir}/#' bin/run3profpp

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
mkdir -p %{buildroot}/%{_bindir}
cp bin/* %{buildroot}/%{_bindir}
chmod 0755 %{buildroot}/%{_bindir}/*

%files
%doc Changes META.yml
%{_bindir}/*
%{perl_vendorlib}/IPC
%{_mandir}/man3/*




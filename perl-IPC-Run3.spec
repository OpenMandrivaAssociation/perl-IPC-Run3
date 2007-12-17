%define module  IPC-Run3
%define name    perl-%{module}
%define version 0.039
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Run a subprocess in batch mode (a la system)
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/IPC/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch


%description
IPC::Run3 allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed. 

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided. 

%prep
%setup -q -n %{module}-%{version}
perl -pi -e 's#/usr/local/bin/#%{_bindir}/#' bin/run3profpp

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}/%{_bindir}
cp bin/* %{buildroot}/%{_bindir}
chmod 0755 %{buildroot}/%{_bindir}/*

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/IPC
%{_mandir}/*/*
%{_bindir}/*


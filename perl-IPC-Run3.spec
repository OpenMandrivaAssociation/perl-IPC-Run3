%define upstream_name    IPC-Run3
%define upstream_version 0.044

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:        Run a subprocess in batch mode (a la system)
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}


%description
IPC::Run3 allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed. 

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 's#/usr/local/bin/#%{_bindir}/#' bin/run3profpp

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
%doc Changes META.yml
%{perl_vendorlib}/IPC
%{_mandir}/*/*
%{_bindir}/*

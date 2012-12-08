%define upstream_name    IPC-Run3
%define upstream_version 0.044

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Run a subprocess in batch mode (a la system)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%{perl_vendorlib}/IPC
%{_mandir}/*/*
%{_bindir}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.44.0-4mdv2012.0
+ Revision: 765380
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.44.0-3
+ Revision: 763897
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.44.0-2
+ Revision: 667217
- mass rebuild

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.44.0-1mdv2011.0
+ Revision: 572704
- update to 0.044

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.043-1mdv2010.1
+ Revision: 383973
- update to new version 0.043

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.042-2mdv2009.1
+ Revision: 351918
- rebuild

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.042-1mdv2009.0
+ Revision: 270889
- update to new version 0.042

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.041-1mdv2009.0
+ Revision: 270388
- update to new version 0.041

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.040-2mdv2009.0
+ Revision: 223804
- rebuild

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.040-1mdv2008.1
+ Revision: 138326
- update to new version 0.040

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.039-1mdv2008.1
+ Revision: 105894
- update to new version 0.039

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.038-1mdv2008.1
+ Revision: 104497
- update to new version 0.038

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.037-1mdv2008.0
+ Revision: 46530
- update to new version 0.037


* Thu Sep 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.036-1mdv2007.0
- new version

* Mon Jul 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.035-1mdv2007.0
- new version

* Tue Dec 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.034-1mdk
- 0.034

* Fri Nov 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.033-1mdk
- New release 0.033
- %%mkrel
- fix sources URL

* Wed Oct 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.032-1mdk
- 0.032

* Thu Sep 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.031-1mdk
- New release 0.031

* Fri Sep 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.030-1mdk
- version
- fix source url
- don't ship empty directories
- make test in %%check

* Mon Jul 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.020-1mdk
- 0.020

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.01-2mdk
- rebuild for new perl

* Tue Aug 03 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.01-1mdk
- 0.01

* Tue May 11 2004 Michael Scherer <misc@mandrake.org> 0.009-1mdk
- New release 0.009

* Wed Apr 28 2004 Michael Scherer <misc@mandrake.org> 0.01-3mdk 
- really fix Requires

* Wed Apr 28 2004 Michael Scherer <misc@mandrake.org> 0.01-2mdk 
- fix Requires

* Wed Apr 28 2004 Michael Scherer <misc@mandrake.org> 0.01-1mdk
- first release, based on perl-IPC-Run


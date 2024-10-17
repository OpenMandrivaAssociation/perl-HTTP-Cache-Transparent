%define module	HTTP-Cache-Transparent
%define upstream_version 1.1

Name:		perl-%{module}
Version:	%perl_convert_version 1.1
Release:	3
Summary:	A transparant caching implementation of http get
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/M/MA/MATTIASH/HTTP-Cache-Transparent-1.1.tar.gz
Url:		https://search.cpan.org/dist/%module/

BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildArch:	noarch

%description
HTTP::Cache::Transparent is an implementation of http get that keeps a local
cache of fetched pages to avoid fetching the same data from the server
if it hasn't been updated. The cache is stored on disk and is thus
persistent between invocations.

The http-headers If-Modified-Since and ETag are used to let the server
decide if the version in the cache is up-to-date or not.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/HTTP/Cache/Transparent.pm
%{_mandir}/*/*

%changelog
* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2010.0
+ Revision: 440586
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.0-4mdv2009.1
+ Revision: 350222
- 2009.1 rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 257245
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2008.1
+ Revision: 119231
- update to new version 1.0


* Wed Jan 03 2007 Stefan van der Eijk <stefan@mandriva.org> 0.7-1mdv2007.0
+ Revision: 103810
- Import perl-HTTP-Cache-Transparent

* Thu Mar 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.7-1mdk
- 0.7

* Sun Jul 17 2005 Stefan van der Eijk <stefan@eijk.nu> 0.6-1mdk
- 0.6
- %%mkrel
- BuildRequires

* Mon Jan 24 2005 Stefan van der Eijk <stefan@mandrake.org> 0.5-1mdk
- first mdk release



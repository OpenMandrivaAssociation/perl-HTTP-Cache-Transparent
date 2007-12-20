%define module	HTTP-Cache-Transparent
%define name	perl-%{module}
%define version 1.0
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A transparant caching implementation of http get
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/M/MA/MATTIASH/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%module/
BuildRoot:	%{_tmppath}/%{name}-buildroot/
BuildRequires:	perl-libwww-perl
Buildarch:	noarch

%description
HTTP::Cache::Transparent is an implementation of http get that keeps a local
cache of fetched pages to avoid fetching the same data from the server
if it hasn't been updated. The cache is stored on disk and is thus
persistent between invocations.

The http-headers If-Modified-Since and ETag are used to let the server
decide if the version in the cache is up-to-date or not.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
EOF
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/HTTP/Cache/Transparent.pm
%{_mandir}/*/*



%define module	Locale-Hebrew
%define version	1.04
%define release	%mkrel 2

Name:      perl-%{module}
Summary:   Locale-Hebrew - Bidirectional Hebrew support
Version:   %{version}
Release:   %{release}
License:   GPL or Artistic
Group:     Development/Perl
Url:       http://www.cpan.org
Source:    http://search.cpan.org//CPAN/authors/id/A/AU/AUTRIJUS/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is based on code from the Unicode Consortium.

The charset on their code was bogus, therefore this module had to work
the real charset from scratch.  There might have some mistakes, though.

One function, "hebrewflip", is exported by default.

%prep
%setup -q -n %{module}-%{version} 
chmod -R u+w %{_builddir}/%{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*/Locale/Hebrew.pm
%{perl_vendorlib}/*/auto/Locale/Hebrew/Hebrew.so
%{perl_vendorlib}/*/auto/Locale/Hebrew/autosplit.ix
%{_mandir}/*/*


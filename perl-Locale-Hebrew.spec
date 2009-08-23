%define upstream_name       Locale-Hebrew
%define upstream_version    1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:   Bidirectional Hebrew support
License:   GPL or Artistic
Group:     Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz
Patch:     Locale-Hebrew-1.04-fix-format-errors.patch
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is based on code from the Unicode Consortium.

The charset on their code was bogus, therefore this module had to work
the real charset from scratch.  There might have some mistakes, though.

One function, "hebrewflip", is exported by default.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch -p 1
# patching make signature check fail 
rm -f t/0-signature.t

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
%{perl_vendorarch}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/*/*


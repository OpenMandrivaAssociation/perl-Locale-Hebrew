%define upstream_name	 Locale-Hebrew
%define upstream_version 1.05

Name:      perl-%{upstream_name}
Version:   %perl_convert_version %{upstream_version}
Release:	3

Summary:   Bidirectional Hebrew support
License:   GPL+ or Artistic
Group:     Development/Perl
Url:       http://www.cpan.org
Source0:   http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:    Locale-Hebrew-1.04-fix-format-errors.patch

BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is based on code from the Unicode Consortium.

The charset on their code was bogus, therefore this module had to work
the real charset from scratch.  There might have some mistakes, though.

One function, "hebrewflip", is exported by default.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p 1
# patching make signature check fail 
rm -f t/0-signature.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.50.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat Nov 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 597083
- new version

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-3mdv2011.0
+ Revision: 556000
- rebuild for perl 5.12

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-2mdv2010.1
+ Revision: 504943
- tighten spec file

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 419910
- new perl version macro
- fix format errors

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.04-5mdv2009.0
+ Revision: 257642
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.04-4mdv2009.0
+ Revision: 245696
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.04-2mdv2008.1
+ Revision: 152124
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sat Jun 17 2006 Stefan van der Eijk <stefan@.eijk.nu> 1.04-1
- Initial build.


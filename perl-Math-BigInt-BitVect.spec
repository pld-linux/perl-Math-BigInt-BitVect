#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BigInt-BitVect
Summary:	Math::BigInt's replacement module using Bit::Vector
Summary(pl.UTF-8):   Moduł zastępujący rdzeń Math::BigInt, używający Bit::Vector
Name:		perl-Math-BigInt-BitVect
Version:	1.12
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1ed80eeb987b604c935951c5fb7b04ce
Patch0:		%{name}-test.patch
BuildRequires:	perl-Math-BigInt >= 1.68
BuildRequires:	perl(Math::BigFloat) >= 1.42
BuildRequires:	perl-Bit-Vector >= 6.3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.60
Requires:	perl(Math::BigFloat) >= 1.35
Requires:	perl-Bit-Vector >= 6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInt::BitVect provides support for big integer calculations
via means of Bit::Vector, a fast C library by Steffen Beier.

%description -l pl.UTF-8
Math::BigInt::BitVect dostarcza obsługę obliczeń na dużych liczbach
całkowitych poprzez procedury Bit::Vector - szybkiej biblioteki w C
autorstwa Steffena Beiera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# sqrt(+inf) == inf, not NaN
#%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES CREDITS LICENSE README TODO
%{perl_vendorlib}/Math/BigInt/*.pm
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}

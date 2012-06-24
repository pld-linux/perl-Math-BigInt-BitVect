#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	BigInt-BitVect
Summary:	Math::BigInt's replacement module using Bit::Vector
Summary(pl):	Modu� zast�puj�cy rdze� Math::BigInt, u�ywaj�cy Bit::Vector
Name:		perl-Math-BigInt-BitVect
Version:	1.11
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d4f2123c53c4388e3d2c40f9a7433a44
Patch0:		%{name}-test.patch
BuildRequires:	perl-Math-BigInt >= 1.60
BuildRequires:	perl(Math::BigFloat) >= 1.35
BuildRequires:	perl-Bit-Vector >= 6.0
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.60
Requires:	perl(Math::BigFloat) >= 1.35
Requires:	perl-Bit-Vector >= 6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInt::BitVect provides support for big integer calculations
via means of Bit::Vector, a fast C library by Steffen Beier.

%description -l pl
Math::BigInt::BitVect dostarcza obs�ug� oblicze� na du�ych liczbach
ca�kowitych poprzez procedury Bit::Vector - szybkiej biblioteki w C
autorstwa Steffena Beiera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# sqrt(+inf) == inf, not NaN
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{!?_without_tests:%{__make} test}

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

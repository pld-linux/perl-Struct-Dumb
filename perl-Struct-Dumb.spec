#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Struct
%define	pnam	Dumb
Summary:	Struct::Dumb - make simple lightweight record-like structures
Name:		perl-Struct-Dumb
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb9ea100dc6f9ecd1c345381930dda08
URL:		http://search.cpan.org/dist/Struct-Dumb/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Struct::Dumb creates record-like structure types, similar to the
struct keyword in C, C++ or C#, or Record in Pascal. An invocation of
this module will create a construction function which returns new
object references with the given field values. These references all
respond to lvalue methods that access or modify the values stored.

It's specifically and intentionally not meant to be an object class.
You cannot subclass it. You cannot provide additional methods. You
cannot apply roles or mixins or metaclasses or traits or antlers or
whatever else is in fashion this week.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Struct/Dumb.pm
%{_mandir}/man3/Struct::Dumb.3pm*

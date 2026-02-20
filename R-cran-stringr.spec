%define		fversion	%(echo %{version} |tr r -)
%define		modulename	stringr
Summary:	Make it easier to work with strings
Name:		R-cran-%{modulename}
Version:	0.6.2
Release:	2
License:	MIT
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	452628504e0910c1d0b1756370716f87
URL:		http://cran.fhcrc.org/web/packages/stringr/index.html
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
stringr is a set of simple wrappers that make R's string functions
more consistent, simpler and easier to use. It does this by ensuring
that: function and argument names (and positions) are consistent,
all functions deal with NA's and zero length character appropriately,
and the output data structures from each function matches the input
data structures of other functions.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}

%define		fversion	%(echo %{version} |tr r -)
%define		modulename	stringr
%undefine	_debugsource_packages
Summary:	Make it easier to work with strings
Name:		R-cran-%{modulename}
Version:	1.6.0
Release:	1
License:	MIT
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	e6d638f79f82b1c39fc88e7295ba1c9d
URL:		https://stringr.tidyverse.org
BuildRequires:	R >= 4.1.0
Requires(post,postun):	R >= 4.1.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R-cli
Requires:	R-glue >= 1.6.1
Requires:	R-lifecycle >= 1.0.3
Requires:	R-magrittr
Requires:	R-rlang >= 1.0.0
Requires:	R-stringi >= 1.5.3
Requires:	R-vctrs >= 0.4.0
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
R CMD build --no-build-vignettes %{modulename}

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

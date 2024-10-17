%bcond_with internet
%global packname  mboost
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.2.2
Release:          2
Summary:          Model-Based Boosting
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/mboost_2.2-2.tar.gz
Requires:         R-methods R-stats 
Requires:         R-Matrix R-survival R-splines R-lattice 
Requires:         R-multicore R-party R-ipred R-MASS R-fields R-BayesX R-gbm 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-stats
BuildRequires:    R-Matrix R-survival R-splines R-lattice 
BuildRequires:    R-multicore R-party R-ipred R-MASS R-fields R-BayesX R-gbm 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Functional gradient descent algorithm (boosting) for optimizing general
risk functions utilizing component-wise (penalised) least squares
estimates or regression trees as base-learners for fitting generalized
linear, additive and interaction models to potentially high-dimensional

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/cache
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/*.R
%{rlibdir}/%{packname}/*.Rda

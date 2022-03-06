#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	jaraco.itertools module
Summary(pl.UTF-8):	Moduł jaraco.itertools
Name:		python-jaraco.itertools
# keep 4.x here for python 2.x support
Version:	4.4.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jaraco-itertools/
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.itertools/jaraco.itertools-%{version}.tar.gz
# Source0-md5:	4472a08481110e531ac6b6443658eb00
URL:		https://pypi.org/project/jaraco.itertools/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:31.0.1
BuildRequires:	python-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python-inflect
BuildRequires:	python-more_itertools >= 4.0.0
BuildRequires:	python-pytest >= 3.5
#BuildRequires:	python-pytest-checkdocs
BuildRequires:	python-pytest-flake8
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools >= 1:31.0.1
BuildRequires:	python3-setuptools_scm >= 1.15
%if %{with tests}
BuildRequires:	python3-inflect
BuildRequires:	python3-more_itertools >= 4.0.0
BuildRequires:	python3-pytest >= 3.5
#BuildRequires:	python3-pytest-checkdocs
BuildRequires:	python3-pytest-flake8
BuildRequires:	python3-six
%endif
%endif
%if %{with doc}
BuildRequires:	python-jaraco.packaging >= 3.2
BuildRequires:	python-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-jaraco
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jaraco.itertools module.

%description -l pl.UTF-8
Moduł jaraco.itertools.

%package -n python3-jaraco.itertools
Summary:	jaraco.itertools module
Summary(pl.UTF-8):	Moduł jaraco.itertools
Group:		Libraries/Python
Requires:	python3-jaraco
Requires:	python3-modules >= 1:3.2

%description -n python3-jaraco.itertools
jaraco.itertools module.

%description -n python3-jaraco.itertools -l pl.UTF-8
Moduł jaraco.itertools.

%package apidocs
Summary:	API documentation for Python jaraco.itertools module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona jaraco.itertools
Group:		Documentation

%description apidocs
API documentation for Python jaraco.itertools module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona jaraco.itertools.

%prep
%setup -q -n jaraco.itertools-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
cd build-2/lib
%{__python} -m pytest
cd ../..
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
cd build-3/lib
%{__python3} -m pytest
cd ../..
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html docs docs/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

# packaged in python-jaraco.spec
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/jaraco/__init__.py*
%endif

%if %{with python3}
%py3_install

# packaged in python-jaraco.spec
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/jaraco/__init__.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/jaraco/__pycache__/__init__.*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/jaraco/itertools.py[co]
%{py_sitescriptdir}/jaraco.itertools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-jaraco.itertools
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/jaraco/itertools.py
%{py3_sitescriptdir}/jaraco/__pycache__/itertools.cpython-*.py[co]
%{py3_sitescriptdir}/jaraco.itertools-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif

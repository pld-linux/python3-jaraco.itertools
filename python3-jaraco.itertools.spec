#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	jaraco.itertools module
Summary(pl.UTF-8):	Moduł jaraco.itertools
Name:		python3-jaraco.itertools
Version:	6.4.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jaraco-itertools/
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.itertools/jaraco_itertools-%{version}.tar.gz
# Source0-md5:	e026dd329dcfda52c511419d1c6c7a05
URL:		https://pypi.org/project/jaraco.itertools/
BuildRequires:	python3-build
BuildRequires:	python3-coherent.licensed
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:61.2
BuildRequires:	python3-setuptools_scm >= 3.4.1
%if %{with tests}
BuildRequires:	python3-inflect
BuildRequires:	python3-more_itertools >= 4.0.0
BuildRequires:	python3-pytest >= 6
# lint only
#BuildRequires:	python3-pytest-checkdocs >= 2.4
#BuildRequires:	python3-pytest-cov
#BuildRequires:	python3-pytest-enabler >= 2.2
#BuildRequires:	python3-pytest-mypy >= 0.9.1
#BuildRequires:	python3-pytest-ruff >= 0.2.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-furo
BuildRequires:	python3-jaraco.packaging >= 9.3
BuildRequires:	python3-rst.linker >= 1.9
#BuildRequires:	python3-sphinx-lint
BuildRequires:	sphinx-pdg-3 >= 3.5
%endif
Requires:	python3-jaraco
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jaraco.itertools module.

%description -l pl.UTF-8
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
%setup -q -n jaraco_itertools-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest jaraco
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html docs docs/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst
%{py3_sitescriptdir}/jaraco/itertools.py
%{py3_sitescriptdir}/jaraco/__pycache__/itertools.cpython-*.py[co]
%{py3_sitescriptdir}/jaraco_itertools-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif

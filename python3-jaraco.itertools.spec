# TODO: finish doc and tests (BRs)
#
# Conditional build:
%bcond_with	doc	# Sphinx documentation
%bcond_with	tests	# unit tests

Summary:	jaraco.itertools module
Summary(pl.UTF-8):	Moduł jaraco.itertools
Name:		python3-jaraco.itertools
Version:	6.2.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jaraco-itertools/
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.itertools/jaraco.itertools-%{version}.tar.gz
# Source0-md5:	d8d68e74c5d1582721c728b6c25020d0
URL:		https://pypi.org/project/jaraco.itertools/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:31.0.1
BuildRequires:	python3-setuptools_scm >= 1.15
%if %{with tests}
BuildRequires:	python3-inflect
BuildRequires:	python3-more_itertools >= 4.0.0
BuildRequires:	python3-pytest >= 6
BuildRequires:	python3-pytest-black >= 0.3.7
#BuildRequires:	python3-pytest-checkdocs >= 2.4
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-pytest-enabler >= 1.0.1
BuildRequires:	python3-pytest-flake8
BuildRequires:	python3-pytest-mypy >= 0.9.1
BuildRequires:	python3-six
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-jaraco.packaging >= 9
BuildRequires:	python3-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-jaraco
Requires:	python3-modules >= 1:3.7
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
%setup -q -n jaraco.itertools-%{version}

# create stub for setuptools
cat >setup.py <<EOF
import setuptools

setuptools.setup(use_scm_version=True)
EOF

%build
%py3_build

%if %{with tests}
cd build-3/lib
%{__python3} -m pytest
cd ../..
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/jaraco/itertools.py
%{py3_sitescriptdir}/jaraco/__pycache__/itertools.cpython-*.py[co]
%{py3_sitescriptdir}/jaraco.itertools-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif

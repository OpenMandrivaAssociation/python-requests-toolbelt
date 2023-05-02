Summary:	A utility belt for advanced users of python-requests
Name:		python-requests-toolbelt
Version:	1.0.0
Release:	1
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/requests-toolbelt/
Source0:	https://files.pythonhosted.org/packages/source/r/requests-toolbelt/requests-toolbelt-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:  python%{pyver}dist(betamax)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(pyopenssl)
BuildRequires:  python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

BuildArch:	noarch

%description
This is just a collection of utilities for python-requests, but don’t
really belong in requests proper. The minimum tested requests version
is 2.1.0. In reality, the toolbelt should work with 2.0.1 as well, but
some idiosyncracies prevent effective or sane testing on that version.

%files
%license LICENSE
%doc README.rst HISTORY.rst
%{py_sitedir}/requests_toolbelt
%{py_sitedir}/requests_toolbelt-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n requests-toolbelt-%{version}

%build
%py_build

%install
%py_install


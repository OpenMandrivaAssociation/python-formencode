%define module formencode
%define oname FormEncode
%bcond tests 1

Name:		python-formencode
Version:	2.1.1
Release:	1
Summary:	HTML form validation, generation, and convertion package  
Group:		Development/Python
License:	MIT
URL:		https://github.com/formencode/formencode
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-docutils
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(dnspython)
BuildRequires:	python%{pyver}dist(pycountry)
%endif

%description
%{name} validates and converts nested structures.
It allows for a declarative form of defining the validation,
and decoupled processes for filling and generating forms.

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%install -a
for file in %{buildroot}%{python_sitelib}/formencode/i18n/* ; do
    if [ -d $file ] ; then
        if [ -e $file/LC_MESSAGES/%{oname}.mo ] ; then
            mkdir -p %{buildroot}%{_datadir}/locale/`basename $file`/LC_MESSAGES/
            mv $file/LC_MESSAGES/%{oname}.mo %{buildroot}%{_datadir}/locale/`basename $file`/LC_MESSAGES/
        fi
    fi
done
rm -rf %{buildroot}%{python_sitelib}/formencode/i18n

%find_lang %{oname}

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
# These tests poll dns, skip them
skiptests+="not (test_doctests and _wrapper-formencode.validators-False-True)"
skiptests+=" and not test_unicode_ascii_subgroup and not test_i18n"
pytest -k "$skiptests"
%endif

%files -f %{oname}.lang
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info

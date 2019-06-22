%define srcname FormEncode

Name:		python-formencode
Version:	1.3.1
Release:	1
Summary:	HTML form validation, generation, and convertion package  
Group:		Development/Python
License:	Python
URL:		http://formencode.org/
Source0:	https://files.pythonhosted.org/packages/2f/53/707c2b9b65ea6bedde67c21cbf7c71394f4a198620d4e9c1771214b91dcc/FormEncode-1.3.1.tar.gz
%rename		python-formencode

BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-docutils
BuildRequires:	python-nose

%description
FormEncode validates and converts nested structures. It allows for a 
declarative form of defining the validation, and decoupled processes 
for filling and generating forms.

%files -f %{srcname}.lang
%doc PKG-INFO docs
%{python_sitelib}/formencode
%{python_sitelib}/%{srcname}-%{version}-py%{py_ver}.egg-info
%{python_sitelib}/docs/


#------------------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}

%build
%py_build

%install
%py_install


# Move l10n files in correct place like it's done on fedora
for file in %{buildroot}/%{python_sitelib}/formencode/i18n/* ; do
    if [ -d $file ] ; then
        if [ -e $file/LC_MESSAGES/%{srcname}.mo ] ; then
            mkdir -p %{buildroot}/%{_datadir}/locale/`basename $file`/LC_MESSAGES/
            mv $file/LC_MESSAGES/%{srcname}.mo %{buildroot}/%{_datadir}/locale/`basename $file`/LC_MESSAGES/
        fi
    fi
done
rm -rf %{buildroot}/%{python_sitelib}/formencode/i18n

%find_lang %{srcname}

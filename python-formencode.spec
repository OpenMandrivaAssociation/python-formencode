%define srcname FormEncode

Name:           python2-formencode
Version:        1.2.6
Release:        10
Summary:        HTML form validation, generation, and convertion package  
Group:          Development/Python
License:        Python
URL:            http://formencode.org/
Source0:        http://pypi.python.org/packages/source/F/FormEncode/%{srcname}-%{version}.zip

BuildArch:      noarch
BuildRequires: pkgconfig(python-2.7)
BuildRequires: python-docutils
BuildRequires: python-nose
BuildRequires: python2-distribute

%description
FormEncode validates and converts nested structures. It allows for a 
declarative form of defining the validation, and decoupled processes 
for filling and generating forms.

%files -f %{srcname}.lang
%doc PKG-INFO docs
%{python2_sitelib}/formencode
%{python2_sitelib}/%{srcname}-%{version}-py%{py2ver}.egg-info

#------------------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python2} setup.py build

%install
find . -type f -perm -0666 |xargs chmod 0644
%{__python2} setup.py install --skip-build --root %{buildroot}


# Move l10n files in correct place like it's done on fedora
for file in %{buildroot}/%{python2_sitelib}/formencode/i18n/* ; do
    if [ -d $file ] ; then
        if [ -e $file/LC_MESSAGES/%{srcname}.mo ] ; then
            mkdir -p %{buildroot}/%{_datadir}/locale/`basename $file`/LC_MESSAGES/
            mv $file/LC_MESSAGES/%{srcname}.mo %{buildroot}/%{_datadir}/locale/`basename $file`/LC_MESSAGES/
        fi
    fi
done
rm -rf %{buildroot}/%{python2_sitelib}/formencode/i18n

%find_lang %{srcname}

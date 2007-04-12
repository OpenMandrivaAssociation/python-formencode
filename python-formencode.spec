%define oname formencode
%define Oname FormEncode

%define name python-%oname
%define version 0.4
%define release 2

Summary:  Python module to validate and generate form
Name: %{name}
Version: %{version}
Release: %mkrel %{release}

Source0: http://cheeseshop.python.org/packages/source/F/%{Oname}/%{Oname}-%{version}.tar.bz2
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Url: http://formencode.org
BuildRequires: python-devel
BuildRequires: python-setuptools

%description
FormEncode is a validation and form generation package. The validation can be 
used separately from the form generation. The validation works on compound 
data structures, with all parts being nestable. It is separate from HTTP or 
any other input mechanism.

%prep
%setup -q -n %Oname-%version
perl -pi -e 's/^(use_setuptools)/#$1/' setup.py

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/ examples/
%py_sitedir/%{oname}
%py_sitedir/*.egg-info/


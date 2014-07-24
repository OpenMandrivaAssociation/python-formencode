%define oname formencode
%define Oname FormEncode

Summary:  Python module to validate and generate form
Name:    python-%oname
Version: 1.2.6
Release: 4

Source0: http://cheeseshop.python.org/packages/source/F/FormEncode/FormEncode-%{version}.zip
License: BSD
Group: Development/Python
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
%setup -q -n %Oname-%{version}
perl -pi -e 's/^(use_setuptools)/#$1/' setup.py

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}
find %{buildroot}%{py_puresitedir} -type f -exec chmod o-w {} \;

%files
%doc docs
%{py_puresitedir}/%{oname}
%{py_puresitedir}/*.egg-info

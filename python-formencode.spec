%define oname formencode
%define Oname FormEncode

Summary:  Python module to validate and generate form
Name:    python-%oname
Version: 1.2.6
Release: 1

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
%setup -q -n %Oname-%version
perl -pi -e 's/^(use_setuptools)/#$1/' setup.py

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --root=%{buildroot}
find %{buildroot}%py_puresitedir -type f -exec chmod o-w {} \;

%files
%doc docs
%py_puresitedir/%{oname}
%py_puresitedir/*.egg-info


%changelog
* Mon May 02 2011 Michael Scherer <misc@mandriva.org> 1.2.4-1mdv2011.0
+ Revision: 661926
- update to 1.2.4

* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 1.2.2-1mdv2011.0
+ Revision: 598146
- rebuild for py2.7

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.2-1mdv2010.0
+ Revision: 384250
- update to new version 1.2.2

* Sun Jan 11 2009 Funda Wang <fwang@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 328230
- New version 1.2.1

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.1-2mdv2009.1
+ Revision: 323713
- rebuild

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2009.1
+ Revision: 305838
- update to new version 1.1

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 1.0.1-1mdv2009.0
+ Revision: 280550
- New release

* Sat Jan 05 2008 Jérôme Soyer <saispo@mandriva.org> 0.9-1mdv2008.1
+ Revision: 145720
- New release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.1-1mdv2008.0
+ Revision: 52596
- update to new version 0.7.1


* Thu Aug 10 2006 Michael Scherer <misc@mandriva.org> 0.4-2mdv2007.0
- Rebuild for new extension
- add egg-info directory

* Sat Dec 10 2005 Michael Scherer <misc@mandriva.org> 0.4-1mdk
- initial package



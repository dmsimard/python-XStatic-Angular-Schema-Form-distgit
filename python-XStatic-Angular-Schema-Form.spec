%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name XStatic-Angular-Schema-Form

Name:           python-%{pypi_name}
Version:        0.8.13.0
Release:        1%{?dist}
Summary:        Angular-Schema-Form JavaScript library (XStatic packaging standard)

License:        MIT
URL:            https://github.com/json-schema-form/angular-schema-form
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/json-schema-form/angular-schema-form/development/LICENSE
BuildArch:      noarch

%description
Angular-Schema-Form JavaScript library packaged
for setuptools (easy_install) / pip.

Generate forms from JSON schemas using AngularJS.

%package -n python2-%{pypi_name}
Summary: Angular-Schema-Form JavaScript library (XStatic packaging standard)
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-XStatic
Requires:       xstatic-angular-schema-form-common = %{version}-%{release}

%description -n python2-%{pypi_name}
Angular-Schema-Form JavaScript library packaged
for setuptools (easy_install) / pip.

Generate forms from JSON schemas using AngularJS.

%package -n xstatic-angular-schema-form-common
Summary: Angular-Schema-Form JavaScript library (XStatic packaging standard)

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-angular-schema-form-common
Angular-Schema-Form JavaScript library packaged
for setuptools (easy_install) / pip.

This package contains the javascript files.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary: Angular-Schema-Form JavaScript library (XStatic packaging standard)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-angular-schema-form-common = %{version}-%{release}

%description -n python3-%{pypi_name}
Angular-Schema-Form JavaScript library packaged
for setuptools (easy_install) / pip.

Generate forms from JSON schemas using AngularJS.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} .

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_schema_form'|" xstatic/pkg/angular_schema_form/__init__.py

%build
%{__python2} setup.py build
%if 0%{?with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

# Move static files
mkdir -p %{buildroot}/%{_jsdir}/angular_schema_form
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_schema_form/data/bootstrap-decorator.js %{buildroot}/%{_jsdir}/angular_schema_form
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_schema_form/data/bootstrap-decorator.min.js %{buildroot}/%{_jsdir}/angular_schema_form
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_schema_form/data/schema-form.js %{buildroot}/%{_jsdir}/angular_schema_form
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_schema_form/data/schema-form.min.js %{buildroot}/%{_jsdir}/angular_schema_form
rm %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_schema_form/data/WHERE_IS_BOOTSTRAP_DECORATOR.md

rmdir %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_schema_form/data/

%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
# Remove static files, already created by the python2 subpkg
rm -rf %{buildroot}/%{python3_sitelib}/xstatic/pkg/angular_schema_form/data
%endif

%files -n python2-%{pypi_name}
%doc README.txt
%license LICENSE
%{python2_sitelib}/xstatic/pkg/angular_schema_form
%{python2_sitelib}/XStatic_Angular_Schema_Form-%{version}-py?.?.egg-info
%{python2_sitelib}/XStatic_Angular_Schema_Form-%{version}-py?.?-nspkg.pth

%files -n xstatic-angular-schema-form-common
%doc README.txt
%license LICENSE
%{_jsdir}/angular_schema_form

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.txt
%license LICENSE
%{python3_sitelib}/xstatic/pkg/angular_schema_form
%{python3_sitelib}/XStatic_Angular_Schema_Form-%{version}-py?.?.egg-info
%{python3_sitelib}/XStatic_Angular_Schema_Form-%{version}-py?.?-nspkg.pth
%endif

%changelog
* Fri Aug 5 2016 David Moreau Simard <dmsimard@redhat.com> - 0.8.13.0-1
- First version

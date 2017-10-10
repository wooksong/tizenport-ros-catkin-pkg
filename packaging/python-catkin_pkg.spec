Name:           python-catkin_pkg
Version:        0.3.7	
Release:        0
License:        BSD
Summary:        Catkin package library
Url:            http://wiki.ros.org/python-catkin_pkg
Group:          Development/Languages/Python
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  python-devel
BuildRequires:  python-argparse
Requires:       python-argparse
BuildRequires:  python-mock

%description
Library for retrieving information about catkin packages.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_bindir}/catkin_create_pkg
%{_bindir}/catkin_find_pkg
%{_bindir}/catkin_generate_changelog
%{_bindir}/catkin_tag_changelog
%{_bindir}/catkin_test_changelog
%{python_sitelib}/*

%changelog

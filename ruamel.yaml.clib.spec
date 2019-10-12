#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ruamel.yaml.clib
Version  : 0.2.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/92/28/612085de3fae9f82d62d80255d9f4cf05b1b341db1e180adcf28c1bf748d/ruamel.yaml.clib-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/92/28/612085de3fae9f82d62d80255d9f4cf05b1b341db1e180adcf28c1bf748d/ruamel.yaml.clib-0.2.0.tar.gz
Summary  : C version of reader, parser and emitter for ruamel.yaml derived from libyaml
Group    : Development/Tools
License  : MIT
Requires: ruamel.yaml.clib-license = %{version}-%{release}
Requires: ruamel.yaml.clib-python = %{version}-%{release}
Requires: ruamel.yaml.clib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev
BuildRequires : ruamel.yaml

%description
ruamel.yaml.clib
================
``ruamel.yaml.clib`` is the C based reader/scanner and emitter for ruamel.yaml

%package license
Summary: license components for the ruamel.yaml.clib package.
Group: Default

%description license
license components for the ruamel.yaml.clib package.


%package python
Summary: python components for the ruamel.yaml.clib package.
Group: Default
Requires: ruamel.yaml.clib-python3 = %{version}-%{release}

%description python
python components for the ruamel.yaml.clib package.


%package python3
Summary: python3 components for the ruamel.yaml.clib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ruamel.yaml.clib package.


%prep
%setup -q -n ruamel.yaml.clib-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570915769
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ruamel.yaml.clib
cp LICENSE %{buildroot}/usr/share/package-licenses/ruamel.yaml.clib/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ruamel.yaml.clib/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

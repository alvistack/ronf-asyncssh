# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-asyncssh
Epoch: 100
Version: 2.14.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Asynchronous SSHv2 client and server library
License: EPL-2.0
URL: https://github.com/ronf/asyncssh/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python 3.6+
asyncio framework.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-asyncssh
Summary: Asynchronous SSHv2 client and server library
Requires: python3
Requires: python3-cryptography >= 3.1
Requires: python3-typing-extensions >= 3.6
Provides: python3-asyncssh = %{epoch}:%{version}-%{release}
Provides: python3dist(asyncssh) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-asyncssh = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(asyncssh) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-asyncssh = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(asyncssh) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-asyncssh
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python 3.6+
asyncio framework.

%files -n python%{python3_version_nodots}-asyncssh
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-asyncssh
Summary: Asynchronous SSHv2 client and server library
Requires: python3
Requires: python3-cryptography >= 3.1
Requires: python3-typing-extensions >= 3.6
Provides: python3-asyncssh = %{epoch}:%{version}-%{release}
Provides: python3dist(asyncssh) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-asyncssh = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(asyncssh) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-asyncssh = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(asyncssh) = %{epoch}:%{version}-%{release}

%description -n python3-asyncssh
AsyncSSH is a Python package which provides an asynchronous client and
server implementation of the SSHv2 protocol on top of the Python 3.6+
asyncio framework.

%files -n python3-asyncssh
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog

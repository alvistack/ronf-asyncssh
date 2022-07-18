%global debug_package %{nil}

Name: python-asyncssh
Epoch: 100
Version: 2.10.1
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
Requires: python3-cryptography >= 2.8
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
Requires: python3-cryptography >= 2.8
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

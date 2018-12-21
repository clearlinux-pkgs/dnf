#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dnf
Version  : 3.3.0
Release  : 39
URL      : https://github.com/rpm-software-management/dnf/archive/3.3.0.tar.gz
Source0  : https://github.com/rpm-software-management/dnf/archive/3.3.0.tar.gz
Summary  : %{pkg_summary}
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0
Requires: dnf-bin = %{version}-%{release}
Requires: dnf-config = %{version}-%{release}
Requires: dnf-license = %{version}-%{release}
Requires: dnf-locales = %{version}-%{release}
Requires: dnf-man = %{version}-%{release}
Requires: dnf-python = %{version}-%{release}
Requires: dnf-python3 = %{version}-%{release}
Requires: dnf-services = %{version}-%{release}
Requires: dnf-plugins-core
Requires: gpgme
Requires: iniparse
Requires: libcomps
Requires: libdnf
Requires: librepo
Requires: pygobject
Requires: smartcols
BuildRequires : buildreq-cmake
BuildRequires : gettext-dev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-Import-configparser-module-directly.patch
Patch2: 0002-Set-EUID-instead-of-loginuid-for-swdb-history.patch
Patch3: 0003-Fix-spacing-issues-in-calcColumns.patch
Patch4: 0004-If-DNF-proxy-is-unset-leave-librepo-proxy-unset.patch
Patch5: 0005-Create-etc-dnf-modules.d-if-missing.patch
Patch6: nowarn.patch

%description
Hawkey tour package to test filelists handling.

%package bin
Summary: bin components for the dnf package.
Group: Binaries
Requires: dnf-config = %{version}-%{release}
Requires: dnf-license = %{version}-%{release}
Requires: dnf-man = %{version}-%{release}
Requires: dnf-services = %{version}-%{release}

%description bin
bin components for the dnf package.


%package config
Summary: config components for the dnf package.
Group: Default

%description config
config components for the dnf package.


%package license
Summary: license components for the dnf package.
Group: Default

%description license
license components for the dnf package.


%package locales
Summary: locales components for the dnf package.
Group: Default

%description locales
locales components for the dnf package.


%package man
Summary: man components for the dnf package.
Group: Default

%description man
man components for the dnf package.


%package python
Summary: python components for the dnf package.
Group: Default
Requires: dnf-python3 = %{version}-%{release}

%description python
python components for the dnf package.


%package python3
Summary: python3 components for the dnf package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dnf package.


%package services
Summary: services components for the dnf package.
Group: Systemd services

%description services
services components for the dnf package.


%prep
%setup -q -n dnf-3.3.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545410731
mkdir -p clr-build
pushd clr-build
%cmake .. -DPYTHON_DESIRED="3" -DWITH_MAN=1
make  %{?_smp_mflags} ; make doc-man
popd

%install
export SOURCE_DATE_EPOCH=1545410731
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dnf
cp COPYING %{buildroot}/usr/share/package-licenses/dnf/COPYING
pushd clr-build
%make_install
popd
%find_lang dnf
## install_append content
ln -s /usr/bin/dnf-3 %{buildroot}/usr/bin/dnf
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dnf
/usr/bin/dnf-3
/usr/bin/dnf-automatic-3

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/dnf-extra.conf
/usr/lib/tmpfiles.d/dnf.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dnf/COPYING

%files man
%defattr(0644,root,root,0755)
%exclude /usr/share/man/man5/yum.conf.5
%exclude /usr/share/man/man8/yum.8
/usr/share/man/man5/dnf.conf.5
/usr/share/man/man8/dnf.8
/usr/share/man/man8/dnf.automatic.8
/usr/share/man/man8/yum2dnf.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/dnf-automatic-download.service
%exclude /usr/lib/systemd/system/dnf-automatic-download.timer
%exclude /usr/lib/systemd/system/dnf-automatic-install.service
%exclude /usr/lib/systemd/system/dnf-automatic-install.timer
%exclude /usr/lib/systemd/system/dnf-automatic-notifyonly.service
%exclude /usr/lib/systemd/system/dnf-automatic-notifyonly.timer
%exclude /usr/lib/systemd/system/dnf-automatic.service
%exclude /usr/lib/systemd/system/dnf-automatic.timer
%exclude /usr/lib/systemd/system/dnf-makecache.service
%exclude /usr/lib/systemd/system/dnf-makecache.timer

%files locales -f dnf.lang
%defattr(-,root,root,-)


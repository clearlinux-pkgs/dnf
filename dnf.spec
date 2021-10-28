#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dnf
Version  : 4.8.0
Release  : 65
URL      : https://github.com/rpm-software-management/dnf/archive/4.8.0/dnf-4.8.0.tar.gz
Source0  : https://github.com/rpm-software-management/dnf/archive/4.8.0/dnf-4.8.0.tar.gz
Summary  : Next-generation version of the YUM package manager
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: dnf-bin = %{version}-%{release}
Requires: dnf-config = %{version}-%{release}
Requires: dnf-license = %{version}-%{release}
Requires: dnf-locales = %{version}-%{release}
Requires: dnf-man = %{version}-%{release}
Requires: dnf-python = %{version}-%{release}
Requires: dnf-python3 = %{version}-%{release}
Requires: dnf-plugins-core
Requires: gpgme
Requires: iniparse
Requires: libcomps
Requires: libdnf
Requires: librepo
Requires: pygobject
Requires: smartcols
BuildRequires : Sphinx
BuildRequires : buildreq-cmake
BuildRequires : dnf-plugins-core
BuildRequires : gettext-dev
BuildRequires : git
BuildRequires : gpgme
BuildRequires : iniparse
BuildRequires : libcomps
BuildRequires : libdnf
BuildRequires : librepo
BuildRequires : pygobject
BuildRequires : smartcols
Patch1: 0001-Fix-spacing-issues-in-calcColumns.patch
Patch2: 0002-Create-etc-dnf-modules.d-if-missing.patch
Patch3: 0003-sphinx-build-3-does-not-exist.patch
Patch4: 0004-Silence-already-installed-messages.patch
Patch5: 0005-Restore-debug-log-level-for-invalid-config-options.patch

%description
Dandified YUM (DNF) is the next upcoming major version of YUM. It does package
management using RPM, libsolv and hawkey libraries. For metadata handling and
package downloads it utilizes librepo. To process and effectively handle the
comps data it uses libcomps.

%package bin
Summary: bin components for the dnf package.
Group: Binaries
Requires: dnf-config = %{version}-%{release}
Requires: dnf-license = %{version}-%{release}

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


%prep
%setup -q -n dnf-4.8.0
cd %{_builddir}/dnf-4.8.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630449615
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DPYTHON_DESIRED="3" \
-DWITH_MAN=1
make  %{?_smp_mflags}  ; make doc-man
popd

%install
export SOURCE_DATE_EPOCH=1630449615
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dnf
cp %{_builddir}/dnf-4.8.0/COPYING %{buildroot}/usr/share/package-licenses/dnf/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd clr-build
%make_install
popd
%find_lang dnf
## Remove excluded files
rm -f %{buildroot}/usr/lib/systemd/system/*.service
rm -f %{buildroot}/usr/lib/systemd/system/*.timer
rm -f %{buildroot}/usr/share/man/man1/yum*
rm -f %{buildroot}/usr/share/man/man5/yum*
rm -f %{buildroot}/usr/share/man/man8/yum*
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
/usr/share/package-licenses/dnf/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/dnf-transaction-json.5
/usr/share/man/man5/dnf.conf.5
/usr/share/man/man7/dnf.modularity.7
/usr/share/man/man8/dnf-automatic.8
/usr/share/man/man8/dnf.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f dnf.lang
%defattr(-,root,root,-)


#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEE926C2BDACC177B (fabiano@fidencio.org)
#
Name     : osinfo-db-tools
Version  : 1.9.0
Release  : 15
URL      : https://releases.pagure.org/libosinfo/osinfo-db-tools-1.9.0.tar.xz
Source0  : https://releases.pagure.org/libosinfo/osinfo-db-tools-1.9.0.tar.xz
Source1  : https://releases.pagure.org/libosinfo/osinfo-db-tools-1.9.0.tar.xz.asc
Summary  : Tools for managing the osinfo database
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: osinfo-db-tools-bin = %{version}-%{release}
Requires: osinfo-db-tools-license = %{version}-%{release}
Requires: osinfo-db-tools-locales = %{version}-%{release}
Requires: osinfo-db-tools-man = %{version}-%{release}
Requires: osinfo-db-data
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : json-glib-dev
BuildRequires : libarchive-dev
BuildRequires : libsoup-dev
BuildRequires : osinfo-db-data
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libsoup-2.4)

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%package bin
Summary: bin components for the osinfo-db-tools package.
Group: Binaries
Requires: osinfo-db-tools-license = %{version}-%{release}

%description bin
bin components for the osinfo-db-tools package.


%package license
Summary: license components for the osinfo-db-tools package.
Group: Default

%description license
license components for the osinfo-db-tools package.


%package locales
Summary: locales components for the osinfo-db-tools package.
Group: Default

%description locales
locales components for the osinfo-db-tools package.


%package man
Summary: man components for the osinfo-db-tools package.
Group: Default

%description man
man components for the osinfo-db-tools package.


%prep
%setup -q -n osinfo-db-tools-1.9.0
cd %{_builddir}/osinfo-db-tools-1.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612811486
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/osinfo-db-tools
cp %{_builddir}/osinfo-db-tools-1.9.0/COPYING %{buildroot}/usr/share/package-licenses/osinfo-db-tools/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang osinfo-db-tools

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/osinfo-db-export
/usr/bin/osinfo-db-import
/usr/bin/osinfo-db-path
/usr/bin/osinfo-db-validate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/osinfo-db-tools/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/osinfo-db-export.1
/usr/share/man/man1/osinfo-db-import.1
/usr/share/man/man1/osinfo-db-path.1
/usr/share/man/man1/osinfo-db-validate.1

%files locales -f osinfo-db-tools.lang
%defattr(-,root,root,-)


%global commit 4a1a72821b9cdfbca81ef193ee2e93ded6adf3f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner delatbabel
%global project LogbookKonni-1.2
%global plugin logbookkonni

Name: opencpn-plugin-%{plugin}
Summary: Logbook plugin for OpenCPN
Version: 0.0
Release: 0.1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Supplements: opencpn%{_isa}

%description
Complex logbook for OpenCPN with a lot of features including a
customizable layout.  To use all the features, you will have to
download and install the layout files as instructed when you run the
plugin for the first time.

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so

%{_datadir}/opencpn/plugins/%{plugin}_pi

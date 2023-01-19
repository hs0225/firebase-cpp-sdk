Name: firebase-cpp-sdk
Version: 0.1 
Release: 1
Summary: firebase cpp sdk
Source: %{name}-%{version}.tar.gz
License: N/A 
 
BuildRequires: cmake, make, ninja, python3
BuildRequires: libopenssl1.1-devel
# BuildRequires: libgcrypt-devel, gobject-introspection-devel
BuildRequires: pkgconfig(openssl1.1)
# BuildRequires: pkgconfig(glib-2.0)

%define package_name    %{name}-%{version}
 
%description

 
%prep
%setup -q
 
%build
python3 -m ensurepip --default-pip
python3 -m pip install --no-index --find-links=./downloads/python/ absl-py
# python3 -m pip install --no-index --find-links=./downloads/python/ meson
export PATH="$HOME/.local/bin:$PATH"

# cd deps/libsecret
# meson _build
# ninja -C _build
# ninja -C _build install
# cd -

%define out_dir ./out_tizen
rm -rf %{out_dir}
mkdir -p %{out_dir}
cmake -B%{out_dir} -H. -G Ninja \
  -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT/%{_exec_prefix} -DFIREBASE_INCLUDE_FIRESTORE=OFF \
  -DTARGET_OS_TIZEN=ON
ninja -C %{out_dir} firebase_app

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
cmake --install %{out_dir}/app

%clean
rm -fr ./*.list
rm -fr ./*.manifest

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest packaging/%{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/*
%{_includedir}/*


Name: firebase-cpp-sdk
Version: 0.1 
Release: 1
Summary: firebase cpp sdk
Source: %{name}-%{version}.tar.gz
License: N/A 
 
BuildRequires: cmake, make, ninja, python

%define package_name    %{name}-%{version}
 
%description

 
%prep
%setup -q
 
%build
%define out_dir ./out
ls
mkdir -p %{out_dir}
cmake -B%{out_dir} -H. -G Ninja -DCMAKE_INSTALL_PREFIX=%{_exec_prefix}
ninja -C %{out_dir}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
CMAKE_INSTALL_PREFIX=%{_exec_prefix} cmake --install %{out_dir}

%clean
rm -fr ./*.list
rm -fr ./*.manifest

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/*
%{_includedir}/*


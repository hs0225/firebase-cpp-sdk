Name: firebase-cpp-sdk
Version: 0.1 
Release: 1
Summary: firebase cpp sdk
Source: %{name}-%{version}.tar.gz
License: N/A 
 
#BuildRequires: cmake
#BuildRequires: make

%define package_name    %{name}-%{version}
 
%description

 
%prep
 
#%setup -q
 
%build

%define out_dir out

mkdir -p %{out_dir} && cd %{out_dir}
cmake .. -G Ninja
ninja
cd -

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
cp %{out_dir}/storage/*.so $RPM_BUILD_ROOT/%{_libdir}
 
%files
%{_libdir}/*.so

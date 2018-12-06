%global goipath github.com/rainycape/memcache
%global commit  1031fa0ce2f20c1c0e1e1b51951d8ea02c84fa05
%gometa

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Memcache client library for the Go programming language
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/rainycape/memcache/pull/5
Patch0:         Use-Skipf-to-permit-formatting-directive.patch


%description
%{summary}.


%package devel
Summary:        %{summary}
BuildArch:      noarch


%description devel
%{summary}.

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup -p 1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 26 2018 Carl George <carl@george.computer> - 0-0.1.20181126git1031fa0
- Initial package

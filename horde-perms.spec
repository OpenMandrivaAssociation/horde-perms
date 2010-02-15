%define prj    Perms

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-perms
Version:       0.1.0
Release:       %mkrel 1
Summary:       Horde Permissions System
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
PreReq:        %{_bindir}/pear
Requires:      php-pear
Requires:      horde-framework
Requires:      horde-util
Requires:      horde-group
Requires:      horde-datatree
Requires:      horde-tree
Requires:      php-gettext
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde
BuildRoot:     %{_tmppath}/%{name}-%{version}

%description
The Perms package provides an interface to the Horde permissions system.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Perms
%{peardir}/Horde/Perms.php
%{peardir}/Horde/Perms/UI.php
%{peardir}/Horde/Perms/datatree.php
%{peardir}/Horde/Perms/sql.php

%define prj    Perms

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-perms
Version:       0.1.0
Release:       4
Summary:       Horde Permissions System
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear
Requires:      horde-framework
Requires:      horde-util
Requires:      horde-group
Requires:      horde-datatree
Requires:      horde-tree
Requires:      php-gettext
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

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


%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-3mdv2011.0
+ Revision: 564079
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-2mdv2010.1
+ Revision: 523037
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 509394
- removed Buildrequires -horde-framework
- replace PreReq with Requires(pre)
- Initial import



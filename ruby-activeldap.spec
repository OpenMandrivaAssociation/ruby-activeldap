%define rname activeldap
%define name ruby-%{rname}
%define version 0.7.2
%define release %mkrel 6

Summary: Object oriented interface to Ruby/LDAP
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://dataspill.org/posts/show/4
Source0: http://rubyforge.org/frs/download.php/1763/%{name}-%{version}.tar.bz2
License: GPL
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.8.1
Requires: ruby-ldap ruby-log4r
BuildRequires: ruby-devel
BuildArch: noarch

%description
Ruby/ActiveLDAP is an object-oriented interface to LDAP written in Ruby. It
is a wrapper around Ruby/LDAP with its interface inspired by ActiveRecord.

Ruby/ActiveLDAP dynamically parses the LDAP server's schema based on the 
objectClasses an entry has. It then exposes the LDAP attributes as methods
on the object. This means that if you update the objectClass on an object,
the methods/attributes available for changing are automatically updated.

%prep
%setup -q 
ruby setup.rb config --prefix=$RPM_BUILD_ROOT%{_prefix}
ruby setup.rb setup

%build

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
ruby setup.rb install
for f in `find %buildroot%{ruby_sitelibdir} . -name \*.rb`
do
        if head -n1 "$f" | grep '^#!' >/dev/null;
        then
                sed -i 's|/usr/local/bin|/usr/bin|' "$f"
                chmod 0755 "$f"
        else
                chmod 0644 "$f"
        fi
done

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/activeldap*
%doc COPYING README LICENSE CHANGES examples tests doc


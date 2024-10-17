%define rname activeldap

Summary: Object oriented interface to Ruby/LDAP
Name:    ruby-%{rname}
Version: 0.7.2
Release: 8
URL: https://dataspill.org/posts/show/4
Source0: http://rubyforge.org/frs/download.php/1763/%{name}-%{version}.tar.bz2
License: GPL
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.8.1
Requires: ruby-ldap
Requires: rubygem-log4r
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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.7.2-6mdv2010.0
+ Revision: 433494
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7.2-5mdv2009.0
+ Revision: 260402
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7.2-4mdv2009.0
+ Revision: 251575
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.7.2-2mdv2008.1
+ Revision: 140753
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 0.7.2-2mdv2008.0
+ Revision: 16782
- Use Development/Ruby group
- Use std macros


* Mon May 22 2006 Pascal Terjan <pterjan@mandriva.org> 0.7.2-1mdk
- New release 0.7.2

* Sun May 07 2006 Pascal Terjan <pterjan@mandriva.org> 0.7.1-1mdk
- 0.7.1

* Tue Jan 10 2006 Pascal Terjan <pterjan@mandriva.org> 0.6.0-1mdk
- 0.6.0
- mkrel
- fix perms

* Thu Mar 31 2005 Pascal Terjan <pterjan@mandrake.org> 0.5.5-2mdk
- lib64 fix

* Mon Feb 21 2005 Pascal Terjan <pterjan@mandrake.org> 0.5.5-1mdk
- 0.5.5

* Mon Jan 12 2004 Pascal Terjan <pterjan@mandrake.org> 0.5.3-1mdk 
- first mdk release


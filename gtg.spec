Name:           gtg
Version:        0.3
Release:        2
Group:          Development/Other
License:        GPLv3
Summary:        Getting Things GNOME! is an organizer for the GNOME desktop environment
Source:         https://launchpad.net/gtg/0.3/0.3/+download/%{name}-%{version}.tar.gz
URL:            http://gtg.fritalk.com/

BuildRequires: pyxdg
BuildRequires: python-devel
Requires:      python-configobj
Requires:      python-simplejson
Requires:      pygtk2.0
Requires:      pygtk2.0-libglade
Requires:      pyxdg
Requires:      python-gobject
Suggests: python-bugz
Suggests: python-evolution
Suggests: hamster-applet
Suggests: python-champlain
Suggests: python-clutter
Suggests: python-clutter-gtk
#Suggests:python-geoclue
BuildArch: noarch

%description
Getting Things Gnome! is an organizer for the GNOME desktop environment.

GTG focuses on usability and ease of use. Its main objective is to
provide a simple, powerful and flexible organization tool to the
GNOME desktop environment.

GTG uses a very handy text edition system for task creation and edition.
The task editor can automatically recognize meta-data such as tags
and subtasks only by the use of a very simple syntax.
If you wanna know more about this, please read Getting Started With GTG.

%prep
%setup -q

%build

%install
python setup.py install --root %{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README CHANGELOG
%{_bindir}/%{name}*
%{_bindir}/gtcli
%{_datadir}/%{name}
%{_mandir}/man1/gtg*
%{_mandir}/man1/gtcli*
%{python_sitelib}/GTG
%{python_sitelib}/%{name}-%{version}-py%{py_ver}.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.gnome.GTG.service
%{_iconsdir}/hicolor/*/apps/gtg.*
%{_datadir}/help/*/%{name}

%changelog
* Mon May 02 2011 Olivier Faurax <ofaurax@mandriva.org> 0.2.4-4mdv2011.0
+ Revision: 662744
- silent: bump release
- New suggests for plugins support

* Sat Nov 20 2010 Jani Välimaa <wally@mandriva.org> 0.2.4-3mdv2011.0
+ Revision: 599310
- add missing requires
- fix source tag
- fix typo in description
- fix install
- fix file list (don't own system dirs)

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.2.4-2mdv2011.0
+ Revision: 592472
- fix for python 2.7
- rebuild for python 2.7

* Mon Apr 12 2010 Olivier Faurax <ofaurax@mandriva.org> 0.2.4-1mdv2010.1
+ Revision: 533677
- new version 0.2.4

* Sat Mar 13 2010 Olivier Faurax <ofaurax@mandriva.org> 0.2.2-2mdv2010.1
+ Revision: 518750
- Better summary
- correct handling of lang files
- correct handling of man file

* Sat Mar 13 2010 Olivier Faurax <ofaurax@mandriva.org> 0.2.2-1mdv2010.1
+ Revision: 518618
- New version 0.2.2

* Sun Dec 20 2009 Olivier Faurax <ofaurax@mandriva.org> 0.2-1mdv2010.1
+ Revision: 480451
- version 0.2.0 -> 0.2 + new binay gtg_new_task
- new version: GTG 0.2.0

* Sun Dec 20 2009 Olivier Faurax <ofaurax@mandriva.org> 0.1.9-1mdv2010.1
+ Revision: 480300
- Added correct lib dir
- Missing python-devel
- Remove noarch, seems something is arch specific
- Missing pyxdg dependency (2)
- Setting as noarch
- Missing pyxdg dependency
- import gtg




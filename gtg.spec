Name:           gtg
Version:        0.2.4
Release:        %mkrel 3
Group:          Development/Other
License:        GPLv3
Summary:        Getting Things GNOME! is an organizer for the GNOME desktop environment
Source:         http://launchpad.net/gtg/0.2/%{version}/+download/%{name}-%{version}.tar.gz
URL:            http://gtg.fritalk.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%__rm -rf %{buildroot}
python setup.py install --root %{buildroot}

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README CHANGELOG
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_mandir}/man1/gtg*
%{python_sitelib}/GTG
%{python_sitelib}/%{name}-%{version}-py%{py_ver}.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.GTG.service
%{_iconsdir}/hicolor/*/apps/gtg.*

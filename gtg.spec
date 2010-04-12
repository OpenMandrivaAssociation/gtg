Name:           gtg
Version:        0.2.4
Release:        %mkrel 1
Group:          Development/Other
License:        GPLv3
Summary:        Getting Things GNOME! is an organizer for the GNOME desktop environment
Source:         gtg-%{version}.tar.gz
URL:            http://gtg.fritalk.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: pyxdg
BuildRequires: python-devel
Requires:      python-configobj

%description
Getting Things Gnome! is an organizer for the GNOME desktop environment.

GTG focuses on usability and ease of use. Its main objective is to
provide a simple, powerful and flexible organization tool to the
GNOME desktop environment.

GTG uses a very handy text edition system for task creation and edition.
The task editor can automatically recognize metadata such as tags
and subtasks only by the use of a very simple syntax.
If you wanna know more about this, please read Getting Started With GTG.

%prep
%setup -q

%build

%install
%__rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}%_prefix --install-lib=%{buildroot}%{_libdir}/python2.6/site-packages
%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%_bindir/%name
%_bindir/%{name}_new_task
%{py_platsitedir}
%{_prefix}/share/gtg
%{_prefix}/share/icons
%{_prefix}/share/dbus-1
%{_prefix}/share/applications
%_mandir/man1/gtg*



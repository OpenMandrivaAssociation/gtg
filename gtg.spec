Name:           gtg
Version:        0.1.9
Release:        %mkrel 1
Group:          Development/Other
License:        GPLv3
Summary:        Getting Things GNOME!
Source:         gtg-%{version}.tar.gz
URL:            http://gtg.fritalk.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

#BuildArch: noarch

BuildRequires: pyxdg

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
#make

%install
%__rm -rf %{buildroot}
#mkdir -p %{buildroot}%{_bindir}
python setup.py install --prefix=%{buildroot}%_prefix

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/%name
%{py_platsitedir}
%{_prefix}/share
%_mandir



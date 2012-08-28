%global modname mattd.plugins.taskwarrior

Name:           mattd-plugins-taskwarrior
Version:        0.0.5
Release:        1%{?dist}
Summary:        Taskwarrior plugin for Matt Daemon
Group:          Applications/Internet
License:        AGPLv3+
URL:            http://mattd.rtfd.org/
Source0:        http://pypi.python.org/packages/source/m/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  mattd

Requires:       mattd
Requires:       espeak
Requires:       task
Requires:       python-taskw
Requires:       python-sh

%description
Taskwarrior plugin for Matt Daemon.  Speak aloud reminders for yourself.

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%{__mkdir_p} %{buildroot}%{_datadir}/mattd/taskwarrior
%{__mkdir_p} %{buildroot}%{_datadir}/mattd/taskwarrior/data
%{__mkdir_p} %{buildroot}%{_sysconfdir}/mattd.d
%{__cp} production.ini %{buildroot}%{_sysconfdir}/mattd.d/taskwarrior.ini
%{__cp} production-taskrc %{buildroot}%{_datadir}/mattd/taskwarrior/taskrc

%files
%doc README.rst LICENSE

%config(noreplace) %{_sysconfdir}/mattd.d/taskwarrior.ini
%config(noreplace) %{_datadir}/mattd/taskwarrior/taskrc

%{python_sitelib}/mattd/plugins/taskwarrior
%{python_sitelib}/%{modname}-%{version}-py*.egg-info/
%{python_sitelib}/%{modname}-%{version}-py*.pth

%changelog
* Fri Aug 24 2012 Ralph Bean <rbean@redhat.com> - 0.0.5-1
- Initial packaging.

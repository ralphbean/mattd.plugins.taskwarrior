%global modname mattd.plugins.taskwarrior

Name:           mattd-plugins-taskwarrior
Version:        0.0.1
Release:        1%{?dist}
Summary:        Taskwarrior plugin for Matt Daemon
Group:          Applications/Internet
License:        AGPLv3+
URL:            http://mattd.rtfd.org/
Source0:        http://pypi.python.org/packages/source/m/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  mattd

Requires:       mattd
Requires:       espeak
Requires:       task
Requires:       python-taskw
Requires:       python-sh

%description
Taskwarrior plugin for Matt Daemon.  Speak aloud reminders for yourself.

For the terminally scatter-brained.

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%files
%doc README.rst LICENSE

%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py*.egg-info/

%changelog
* Fri Aug 24 2012 Ralph Bean <rbean@redhat.com> - 0.0.1-1
- Initial packaging.

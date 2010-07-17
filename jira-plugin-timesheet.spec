%define		plugin	timesheet
%include	/usr/lib/rpm/macros.java
Summary:	JIRA Timesheet report and portlet plugin
Name:		jira-plugin-%{plugin}
Version:	1.9
Release:	2
Epoch:		1
License:	BSD
Group:		Libraries/Java
Source0:	https://studio.plugins.atlassian.com/svn/TIME/jars/atlassian-jira-plugin-timesheet-%{version}.jar
# Source0-md5:	38d2c943b72c4d7bb3d2eba514d1df39
URL:		http://confluence.atlassian.com/display/JIRAEXT/Timesheet+report+and+portlet
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jira >= 4.0
Obsoletes:	jira-enterprise-plugin-timesheet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pluginsdir	%{_datadir}/jira/plugins
%define		pluginsdeploydir	%{_datadir}/jira/WEB-INF/lib

%description
JIRA Timesheet report and portlet plugin.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{pluginsdeploydir},%{pluginsdir}}
cp %{SOURCE0} $RPM_BUILD_ROOT%{pluginsdir}/plugin-%{plugin}-%{version}.jar
ln -s %{pluginsdir}/plugin-%{plugin}-%{version}.jar $RPM_BUILD_ROOT%{pluginsdeploydir}/plugin-%{plugin}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{pluginsdir}/plugin-%{plugin}-%{version}.jar
%{pluginsdeploydir}/plugin-%{plugin}-%{version}.jar

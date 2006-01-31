Summary:	Stream player for Mythtv
Summary(pl):	Odtwarzacz strumieni dla Mythtv
Name:		mythstream
Version:	0.16_5
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://home.kabelfoon.nl/~moongies/sw9vc4htz2/%{name}-v%{version}.tar.gz
# Source0-md5:	c0ec4451bfd959eba9d4eaedfa2dddb0
URL:		http://home.kabelfoon.nl/~moongies/streamtuned.html
BuildRequires:	kdelibs-devel
Requires:	mplayer
Requires:	mythtv-frontend-api
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MythStream is an unofficial plugin for MythTv. It plays audio and
video streams using mplayer as backend.

%description -l pl
MythStream jest nieoficjaln± wtyczk± do MythTv. Odtwarza strumienie
d¼wiêku i obrazu wykorzystuj±c mplayera.

%prep
%setup -q

cp %{_datadir}/mythtv/build/config.mak .
sed -i -e "1iinclude(`pwd`/config.mak)"  settings.pro

%build
export QTDIR="%{_prefix}"
qmake mythstream.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
export QTDIR="%{_prefix}"
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/mythtv/plugins/libmythstream.so
%dir %{_datadir}/mythtv/%{name}
%dir %{_datadir}/mythtv/%{name}/parsers
%attr(755,root,root) %{_datadir}/mythtv/%{name}/parsers/*.pl
%{_datadir}/mythtv/%{name}/parsers/*.xml
%{_datadir}/mythtv/%{name}/player.xml
%{_datadir}/mythtv/%{name}/streams.res
%{_datadir}/mythtv/streamconfigmenu.xml
%{_datadir}/mythtv/themes/*/*.png
%{_datadir}/mythtv/themes/*/*.xml

Summary:	setv4l - small tool for changing the picutre settings
Summary(pl):	setv4l - male narzedzie do zmiany ustawien obrazu
Name:		setv4l
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://members.chello.nl/~j.vreeken/setv4l/%{name}-%{version}.tar.gz
# Source0-md5:	95f02fe04766879f99e2a434b4558aaf
URL:		http://members.chello.nl/~j.vreeken/setv4l/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setv4l is a small command line utility for changing the picture
settings of a video 4 linux device. You change the following settings:
- brightness
- hue
- colour
- contrast
- whiteness

%description -l pl
setv4l jest malym narzedziem sluzacym do zmiany ustawiem obrazu. Mozna
nim zmienic nastepujace ustawienia:
- jaskrawo¶æ
- barwa
- color
- kontrast
- biel

%prep
%setup -q

%build
%{__make} \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install setv4l $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*

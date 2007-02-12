Summary:	setv4l - small tool for changing the picutre settings
Summary(pl.UTF-8):	setv4l - małe narzędzie do zmiany ustawień obrazu
Name:		setv4l
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/Console
Source0:	http://members.chello.nl/~j.vreeken/setv4l/%{name}-%{version}.tar.gz
# Source0-md5:	95f02fe04766879f99e2a434b4558aaf
URL:		http://members.chello.nl/~j.vreeken/setv4l/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setv4l is a small command line utility for changing the picture
settings of a Video 4 Linux device. You change the following settings:
- brightness
- hue
- colour
- contrast
- whiteness

%description -l pl.UTF-8
setv4l jest małym narzędziem służącym do zmiany ustawień obrazu. Można
nim zmienić następujące ustawienia:
- jaskrawość
- barwę
- kolor
- kontrast
- biel

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install setv4l $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*

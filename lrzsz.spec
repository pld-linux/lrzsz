Summary:	The lrz and lsz modem communications programs.
Summary(pl):	Programy lrz i lsz do transmisji modemowej.
Name:		lrzsz
Version:	0.12.20
Release:	3
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://tirka.ohse.de/uwe/releases/%{name}-%{version}.tar.gz
Patch0:		lrzsz-0.12.20-glibc21.patch
Patch1:		lrzsz-aclocal+DESTDIR.patch
BuildRoot:	/tmp/%{name}-%{version}-root
BuildRequires:	autoconf
BuildRequires:	automake

%description
Lrzsz (consisting of lrz and lsz) is a cosmetically modified
zmodem/ymodem/xmodem package built from the public-domain version of the
rzsz package. Lrzsz was created to provide a working GNU copylefted Zmodem
solution for Linux systems. You should install lrzsz if you're also
installing a Zmodem communications program that uses lrzsz.  If you're
installing minicom, you need to install lrzsz.

%description -l pl
Lrzsz (sk�adaj�cy si� z lrz i lsz) jest kosmetycznie poprawionym pakietem
zmodem/ymodem/xmodem budowanym z wersji public-domain pakietu rzsz. Lrzsz
zosta� stworzony �eby zapewni� dzia�aj�c� wersj� GNU implementacji Zmodemu
dla system�w Linuksowych. Powiniene� zainstalowa� lrzsz je�li instalujesz
jakiekolwiek programy do transfer�w Zmodemowych kt�re u�ywaj� lrzsz. Je�li
instalujesz minicoma - potrzebujesz te� lrzsz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mv aclocal.m4 acinclude.m4
aclocal
autoheader
autoconf
automake
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(644,root,root,755)
%{_bindir}/lsz
%{_bindir}/lsb
%{_bindir}/lsx
%{_bindir}/lrz
%{_bindir}/lrb
%{_bindir}/lrx
%{_mandir}/man1/lsz.1
%{_mandir}/man1/lrz.1

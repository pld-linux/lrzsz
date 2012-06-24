Summary:	The lrz and lsz modem communications programs
Summary(de):	lzrz - sz, rz und Co.
Summary(es):	Lzrz - sz, rz, y amigos
Summary(fr):	lzrz - sz, rz, et consorts
Summary(pl):	Programy lrz i lsz do transmisji modemowej
Summary(pt_BR):	Lzrz - sz, rz, e amigos
Summary(ru):	lrzsz - ��������� ��������� ������ �� ������ lrz � lsz
Summary(tr):	Modem protokolleri
Summary(uk):	lrzsz - �������� ��������� ���̦� �� ������ lrz �� lsz
Name:		lrzsz
Version:	0.12.20
Release:	12
License:	GPL
Group:		Applications/Communications
Source0:	ftp://tirka.ohse.de/uwe/releases/%{name}-%{version}.tar.gz
Patch0:		%{name}-glibc21.patch
Patch1:		%{name}-aclocal+DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lrzsz (consisting of lrz and lsz) is a cosmetically modified
zmodem/ymodem/xmodem package built from the public-domain version of
the rzsz package. Lrzsz was created to provide a working GNU
copylefted Zmodem solution for Linux systems. You should install lrzsz
if you're also installing a Zmodem communications program that uses
lrzsz. If you're installing minicom, you need to install lrzsz.

%description -l de
Diese Sammlung von Befehlen l��t sich zum Herunter- und Aufw�rtsladen
von Dateien anhand der Z-, X- und Y-Protokolle benutzen. Viele
Terminalprogramme (wie Minicom) setzen diese Programme f�r die
�bertragung von Dateien ein.

%description -l es
Esta colecci�n de comandos se pueden usar para bajar y actualizar
archivos usando los protocolos Z, X y Y. Muchos programas de terminal
(como el minicom) usan estos programas para transferir archivos.

%description -l fr
Cet ensemble de commande sert � t�l�charger des fichiers en utilisant
les protocoles Z, X et Y. De nombreux programmes de terminal (comme
minicom) utilisent ces programmes pour transf�rer les fichiers.

%description -l pl
Lrzsz (sk�adaj�cy si� z lrz i lsz) jest kosmetycznie poprawionym
pakietem zmodem/ymodem/xmodem budowanym z wersji public-domain pakietu
rzsz. Lrzsz zosta� stworzony �eby zapewni� dzia�aj�c� wersj� GNU
implementacji Zmodemu dla system�w Linuksowych. Powiniene�
zainstalowa� lrzsz je�li instalujesz jakiekolwiek programy do
transfer�w Zmodemowych kt�re u�ywaj� lrzsz. Je�li instalujesz minicoma
- potrzebujesz te� lrzsz.

%description -l pt_BR
Esta cole��o de comandos podem ser usados para baixar e atualizar
arquivos usando os protocolos Z, X e Y. Muitos programas de terminal
(como o minicom) usam estes programas para transferir arquivos.

%description -l ru
Lrzsz (��������� �� �������� lrz � lsz) - ��� "������������"
���������������� ����� �������� ��������� ������ �� ����������
zmodem/ymodem/xmodem, ����������� �� public-domain ������ ������ rzsz.

%description -l tr
Bu komutlar toplulu�u Z, X ve Y protokollerini kullanarak dosya
aktar�m� i�in kullan�labilir. Pek �ok u� birim program� (�rne�in
minicom) dosya ta��mak i�in bu programlar� kullan�r.

%description -l uk
Lrzsz (����������� � ������� lrz �� lsz) - �� "����������"
����Ʀ������� ����� ������� ��������� ���̦� �� ����������
zmodem/ymodem/xmodem, ����������� � public-domain ���Ӧ� ������ rzsz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure \
	--enable-syslog \
	--disable-pubdir \
	--program-transform-name=s/l//

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS COMPATABILITY NEWS README.* THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

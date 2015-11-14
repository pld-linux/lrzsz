Summary:	The rz and sz modem communications programs
Summary(de.UTF-8):	lzrz - sz, rz und Co
Summary(es.UTF-8):	Lzrz - sz, rz, y amigos
Summary(fr.UTF-8):	lzrz - sz, rz, et consorts
Summary(pl.UTF-8):	Programy lrz i lsz do transmisji modemowej
Summary(pt_BR.UTF-8):	Lzrz - sz, rz, e amigos
Summary(ru.UTF-8):	lrzsz - программы пересылки файлов по модему lrz и lsz
Summary(tr.UTF-8):	Modem protokolleri
Summary(uk.UTF-8):	lrzsz - програми пересилки файлів по модему lrz та lsz
Name:		lrzsz
Version:	0.12.21
Release:	2
License:	GPL v2+
Group:		Applications/Communications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	bbd4f0361378deb3e9094cd0117532e2
Patch0:		%{name}-glibc21.patch
Patch1:		%{name}-aclocal+DESTDIR.patch
Patch2:		%{name}-ac.patch
URL:		https://ohse.de/uwe/software/lrzsz.html
BuildRequires:	autoconf >= 2.12
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lrzsz (consisting of lrz and lsz) is a cosmetically modified
zmodem/ymodem/xmodem package built from the public-domain version of
the rzsz package. Lrzsz was created to provide a working GNU
copylefted Zmodem solution for Linux systems. You should install lrzsz
if you're also installing a Zmodem communications program that uses
lrzsz. If you're installing minicom, you need to install lrzsz.

%description -l de.UTF-8
Diese Sammlung von Befehlen läßt sich zum Herunter- und Aufwärtsladen
von Dateien anhand der Z-, X- und Y-Protokolle benutzen. Viele
Terminalprogramme (wie Minicom) setzen diese Programme für die
Übertragung von Dateien ein.

%description -l es.UTF-8
Esta colección de comandos se pueden usar para bajar y actualizar
archivos usando los protocolos Z, X y Y. Muchos programas de terminal
(como el minicom) usan estos programas para transferir archivos.

%description -l fr.UTF-8
Cet ensemble de commande sert à télécharger des fichiers en utilisant
les protocoles Z, X et Y. De nombreux programmes de terminal (comme
minicom) utilisent ces programmes pour transférer les fichiers.

%description -l pl.UTF-8
Lrzsz (składający się z lrz i lsz) jest kosmetycznie poprawionym
pakietem zmodem/ymodem/xmodem budowanym z wersji public-domain pakietu
rzsz. Lrzsz został stworzony żeby zapewnić działającą wersję GNU
implementacji Zmodemu dla systemów linuksowych. Należy zainstalować
lrzsz przy instalacji jakichkolwiek programów transmisji zmodemowych
(np. minicom), które używają lrzsz.

%description -l pt_BR.UTF-8
Esta coleção de comandos podem ser usados para baixar e atualizar
arquivos usando os protocolos Z, X e Y. Muitos programas de terminal
(como o minicom) usam estes programas para transferir arquivos.

%description -l ru.UTF-8
Lrzsz (состоящий из программ lrz и lsz) - это "косметически"
модифицированный пакет программ пересылки файлов по протоколам
zmodem/ymodem/xmodem, построенный из public-domain версии пакета rzsz.

%description -l tr.UTF-8
Bu komutlar topluluğu Z, X ve Y protokollerini kullanarak dosya
aktarımı için kullanılabilir. Pek çok uç birim programı (örneğin
minicom) dosya taşımak için bu programları kullanır.

%description -l uk.UTF-8
Lrzsz (складається з програм lrz та lsz) - це "косметично"
модифікований пакет програм пересилки файлів по протоколам
zmodem/ymodem/xmodem, побудований з public-domain версії пакету rzsz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_lib_nsl_gethostbyname=no \
	--enable-syslog \
	--disable-pubdir \
	--program-transform-name=s/l//

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COMPATABILITY ChangeLog NEWS README README.isdn4linux README.systems THANKS TODO
%attr(755,root,root) %{_bindir}/rb
%attr(755,root,root) %{_bindir}/rx
%attr(755,root,root) %{_bindir}/rz
%attr(755,root,root) %{_bindir}/sb
%attr(755,root,root) %{_bindir}/sx
%attr(755,root,root) %{_bindir}/sz
%{_mandir}/man1/rz.1*
%{_mandir}/man1/sz.1*

Summary: The lrz and lsz modem communications programs.
Name: lrzsz
Version: 0.12.20
Release: 2
Copyright: GPL
Group: Applications/Communications
Source: http://www.nrw.net/uwe/archive/lrzsz-0.12.20.tar.gz
Patch1: lrzsz-0.12.20-glibc21.patch
BuildRoot: /var/tmp/lrzsz-root

%description
Lrzsz (consisting of lrz and lsz) is a cosmetically modified
zmodem/ymodem/xmodem package built from the public-domain version of the
rzsz package.  Lrzsz was created to provide a working GNU copylefted
Zmodem solution for Linux systems.  

You should install lrzsz if you're also installing a Zmodem communications
program that uses lrzsz.  If you're installing minicom, you need to install
lrzsz.

%prep
%setup -q
%patch1 -p1 -b .glibc21

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s \
	./configure --disable-pubdir \
		--enable-syslog \
		--prefix=/usr \
		--program-transform-name=s/l//
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/sz
/usr/bin/sb
/usr/bin/sx
/usr/bin/rz
/usr/bin/rb
/usr/bin/rx
/usr/man/man1/sz.1
/usr/man/man1/rz.1
/usr/share/locale/*/LC_MESSAGES/*

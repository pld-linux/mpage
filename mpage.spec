Summary:	A tool for printing multiple pages of text on each printed page.
Summary(pl):	Narzêdzie pozwalaj±ce umie¶ciæ wiele strona na jednym wydruku.
Name:		mpage
Version:	2.4
Release:	8
Copyright:	BSD
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Source:		ftp://sunsite.unc.edu:/pub/Linux/system/printing/mpage24.tgz
Patch1:		mpage24-dvips.patch
Patch2:		mpage-make.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The mpage utility takes plain text files or PostScript(TM) documents
as input, reduces the size of the text, and prints the files on a
PostScript printer with several pages on each sheet of paper.  Mpage
is very useful for viewing large printouts without using up tons of
paper.  Mpage supports many different layout options for the printed
pages.

Mpage should be installed if you need a useful utility for viewing
long text documents without wasting paper.

%description -l pl
Mpage pobiera czyta pliki z czystym tekstem lub PostScriptem(TM), zmiejsza
rozmiar tekstu i drukuje na drukarce PostScriptowej umieszczaj±c wiele stron
na jednym wydruku. Mpage jest bardzo u¿yteczny do drukowania du¿ych plików
bez marnowania ton papieru. Mpage obs³uguje wiele opcji dotycz±cych wygl±du
drukowanych stron.

Zainstaluj mpage je¶li potrzebujesz narzêdzia do drukowania du¿ych dokumentów
bez marnowania papieru.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/mpage,%{_mandir}/man1}

make PREFIX=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf CHANGES Copyright README NEWS TODO $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/mpage
%{_mandir}/*/*
/usr/lib/mpage

Summary:	A tool for printing multiple pages of text on each printed page.
Summary(de):	plaziert mehrere Textseiten auf eine einzelne Postscript-Seite
Summary(fr):	Place plusieurs pages de texte sur une simple page postscript.
Summary(pl):	Narzêdzie pozwalaj±ce umie¶ciæ wiele strona na jednym wydruku.
Summary(tr):	Birden fazla metin sayfasýný tek bir PostScript sayfasýna yerleþtirir
Name:		mpage
Version:	2.5
Release:	1
License:	BSD
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Source0:	http://www.mesa.nl/pub/mpage/%{name}-%{version}.tgz
Patch0:		mpage-make.patch
URL:		http://www.mesa.nl/index_e.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mpage utility takes plain text files or PostScript(TM) documents
as input, reduces the size of the text, and prints the files on a
PostScript printer with several pages on each sheet of paper. Mpage is
very useful for viewing large printouts without using up tons of
paper. Mpage supports many different layout options for the printed
pages. Mpage should be installed if you need a useful utility for
viewing long text documents without wasting paper.

%description -l de
mpage formatiert mehrere Seiten ASCII-Text in eine einzelne
PostScript-Seite. Es unterstützt eine große Auswahl von Layouts.

%description -l fr
mpage formate plusieurs pages de texte ASCII en un seule en
PostScript. Il reconnait plusieurs mises en pages.

%description -l pl
Mpage pobiera czyta pliki z czystym tekstem lub PostScriptem(TM),
zmiejsza rozmiar tekstu i drukuje na drukarce PostScriptowej
umieszczaj±c wiele stron na jednym wydruku. Mpage jest bardzo
u¿yteczny do drukowania du¿ych plików bez marnowania ton papieru.
Mpage obs³uguje wiele opcji dotycz±cych wygl±du drukowanych stron.
Zainstaluj mpage je¶li potrzebujesz narzêdzia do drukowania du¿ych
dokumentów bez marnowania papieru.

%description -l tr
mpage çok sayfalý ASCII metinlerini tek bir PostScript sayfasýna
biçimler. Sayfanýn son þeklinin deðiþik biçimlerde elde edilebilmesine
olanak verir.

%prep
%setup -q
%patch0 -p1

%build
make OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/mpage,%{_mandir}/man1}

make PREFIX=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf CHANGES README NEWS TODO $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/mpage
%{_mandir}/*/*
%{_libdir}/mpage

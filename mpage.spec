Summary:	A tool for printing multiple pages of text on each printed page
Summary(de):	plaziert mehrere Textseiten auf eine einzelne Postscript-Seite
Summary(fr):	Place plusieurs pages de texte sur une simple page postscript
Summary(pl):	Narzêdzie pozwalaj±ce umie¶ciæ wiele stron na jednym wydruku
Summary(tr):	Birden fazla metin sayfasýný tek bir PostScript sayfasýna yerleþtirir
Name:		mpage
Version:	2.5.1
Release:	7
License:	BSD
Group:		Applications/Publishing
Source0:	http://www.mesa.nl/pub/mpage/%{name}251pre.tgz
# Source0-md5:	04460353ae61405a8fc58545bad143a9
Patch0:		%{name}-make.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-debian.patch
Patch3:		%{name}-tempfile.patch
Patch4:		%{name}-j.patch
Patch5:		%{name}-level3.patch
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
zmniejsza rozmiar tekstu i drukuje na drukarce postscriptowej
umieszczaj±c wiele stron na jednym wydruku. Mpage jest bardzo
u¿yteczny do drukowania du¿ych plików bez marnowania ton papieru.
Mpage obs³uguje wiele opcji dotycz±cych wygl±du drukowanych stron.
Warto zainstalowaæ mpage je¶li potrzebujemy narzêdzia do drukowania
du¿ych dokumentów bez marnowania papieru.

%description -l tr
mpage çok sayfalý ASCII metinlerini tek bir PostScript sayfasýna
biçimler. Sayfanýn son þeklinin deðiþik biçimlerde elde edilebilmesine
olanak verir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__make} \
	OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/mpage,%{_mandir}/man1}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README NEWS TODO
%attr(755,root,root) %{_bindir}/mpage
%{_mandir}/*/*
%{_libdir}/mpage

Summary:	A tool for printing multiple pages of text on each printed page
Summary(de.UTF-8):   plaziert mehrere Textseiten auf eine einzelne Postscript-Seite
Summary(fr.UTF-8):   Place plusieurs pages de texte sur une simple page postscript
Summary(pl.UTF-8):   Narzędzie pozwalające umieścić wiele stron na jednym wydruku
Summary(tr.UTF-8):   Birden fazla metin sayfasını tek bir PostScript sayfasına yerleştirir
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

%description -l de.UTF-8
mpage formatiert mehrere Seiten ASCII-Text in eine einzelne
PostScript-Seite. Es unterstützt eine große Auswahl von Layouts.

%description -l fr.UTF-8
mpage formate plusieurs pages de texte ASCII en un seule en
PostScript. Il reconnait plusieurs mises en pages.

%description -l pl.UTF-8
Mpage pobiera czyta pliki z czystym tekstem lub PostScriptem(TM),
zmniejsza rozmiar tekstu i drukuje na drukarce postscriptowej
umieszczając wiele stron na jednym wydruku. Mpage jest bardzo
użyteczny do drukowania dużych plików bez marnowania ton papieru.
Mpage obsługuje wiele opcji dotyczących wyglądu drukowanych stron.
Warto zainstalować mpage jeśli potrzebujemy narzędzia do drukowania
dużych dokumentów bez marnowania papieru.

%description -l tr.UTF-8
mpage çok sayfalı ASCII metinlerini tek bir PostScript sayfasına
biçimler. Sayfanın son şeklinin değişik biçimlerde elde edilebilmesine
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

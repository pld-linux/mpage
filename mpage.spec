Summary: A tool for printing multiple pages of text on each printed page.
Name: mpage
Version: 2.4
Release: 7
Copyright: BSD
Group: Applications/Publishing
Source: ftp://sunsite.unc.edu:/pub/Linux/system/printing/mpage24.tgz
Patch: mpage24-config.patch
Patch1: mpage24-dvips.patch
BuildRoot: /var/tmp/mpage-root

%description
The mpage utility takes plain text files or PostScript(TM) documents
as input, reduces the size of the text, and prints the files on a
PostScript printer with several pages on each sheet of paper.  Mpage
is very useful for viewing large printouts without using up tons of
paper.  Mpage supports many different layout options for the printed
pages.

Mpage should be installed if you need a useful utility for viewing
long text documents without wasting paper.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/mpage,man/man1}

make PREFIX=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/mpage

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES Copyright README NEWS TODO
/usr/bin/mpage
/usr/man/man1/mpage.1
/usr/lib/mpage

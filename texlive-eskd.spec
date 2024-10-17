Name:		texlive-eskd
Version:	15878
Release:	2
Summary:	Modern Russian typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eskd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class offers modern Russian text formatting, in accordance
with accepted design standards. Fonts not (apparently)
available on CTAN are required for use of the class.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eskd/eskd.cls
%doc %{_texmfdistdir}/doc/latex/eskd/README
%doc %{_texmfdistdir}/doc/latex/eskd/eskd.pdf
%doc %{_texmfdistdir}/doc/latex/eskd/example.eps
%doc %{_texmfdistdir}/doc/latex/eskd/example.tex
#- source
%doc %{_texmfdistdir}/source/latex/eskd/eskd.dtx
%doc %{_texmfdistdir}/source/latex/eskd/eskd.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eskd
# catalog-date 2007-02-14 08:57:40 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-eskd
Version:	20070214
Release:	9
Summary:	Modern Russian typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eskd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070214-2
+ Revision: 751578
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070214-1
+ Revision: 718367
- texlive-eskd
- texlive-eskd
- texlive-eskd
- texlive-eskd


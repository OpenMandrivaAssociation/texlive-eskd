Name:		texlive-eskd
Version:	20070214
Release:	1
Summary:	Modern Russian typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eskd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class offers modern Russian text formatting, in accordance
with accepted design standards. Fonts not (apparently)
available on CTAN are required for use of the class.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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

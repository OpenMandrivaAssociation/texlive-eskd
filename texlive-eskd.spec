%global tl_name eskd
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Modern Russian typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eskd
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eskd.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class offers modern Russian text formatting, in accordance with
accepted design standards. Fonts not (apparently) available on CTAN are
required for use of the class.


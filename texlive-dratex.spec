%global tl_name dratex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	General drawing macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/dratex
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dratex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dratex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A low level (DraTex.sty) and a high-level (AlDraTex.sty) drawing package
written entirely in TeX.


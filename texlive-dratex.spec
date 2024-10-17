Name:		texlive-dratex
Version:	15878
Release:	2
Summary:	General drawing macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/dratex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dratex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dratex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A low level (DraTex.sty) and a high-level (AlDraTex.sty)
drawing package written entirely in TeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/dratex/AlDraTex.sty
%{_texmfdistdir}/tex/generic/dratex/DraTex.sty
%{_texmfdistdir}/tex/generic/dratex/TeXProject.sty
%{_texmfdistdir}/tex/generic/dratex/wotree.sty
%doc %{_texmfdistdir}/doc/generic/dratex/Examples.tex
%doc %{_texmfdistdir}/doc/generic/dratex/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

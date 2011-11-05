# revision 15878
# category Package
# catalog-ctan /graphics/dratex
# catalog-date 2008-09-18 22:51:09 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-dratex
Version:	20080918
Release:	1
Summary:	General drawing macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/dratex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dratex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dratex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A low level (DraTex.sty) and a high-level (AlDraTex.sty)
drawing package written entirely in TeX.

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
%{_texmfdistdir}/tex/generic/dratex/AlDraTex.sty
%{_texmfdistdir}/tex/generic/dratex/DraTex.sty
%{_texmfdistdir}/tex/generic/dratex/TeXProject.sty
%{_texmfdistdir}/tex/generic/dratex/wotree.sty
%doc %{_texmfdistdir}/doc/generic/dratex/Examples.tex
%doc %{_texmfdistdir}/doc/generic/dratex/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

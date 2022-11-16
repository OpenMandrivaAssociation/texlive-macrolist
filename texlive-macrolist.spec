Name:		texlive-macrolist
Version:	60139
Release:	1
Summary:	List operations for LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/macrolist
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macrolist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macrolist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macrolist.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a list data structure and common list
functions such as \macrolistadd, \macrolistremove,
\macrolistforeach, as well as \macrolistremovelast (similar to
C++'s pop_back) and \macrolistjoin (similar to Javascript's
arr.join). Unlike most programming languages, the lists in this
package are 1-indexed, meaning the first element is numbered 1,
the second element numbered 2, and so on.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/macrolist
%{_texmfdistdir}/tex/latex/macrolist
%doc %{_texmfdistdir}/doc/latex/macrolist

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

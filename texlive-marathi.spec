Name:		texlive-marathi
Version:	61719
Release:	1
Summary:	Typeset Marathi language using XeLaTeX or LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/marathi
License:	gpl3+ other-free fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marathi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marathi.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marathi.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
luaa-laattek v jhii-laattek hyaaNcyaash mraatthiicaa sulbh
vaapr krnnyaasaatthii. laattek-vriil mraatthiicyaa
sthaanikiikrnnaace kaam hyaa aajnyaasNcaamaarpht kele jaaiil.
expex v blindtext hyaa aajnyaasNcaaNce sthaanikiikrnn tuurtaas
hyaa aajnyaasNcaamaarpht purvle jaat aahe. For conveniently
typesetting Marathi language with LuaLaTeX and XeLaTeX. This
package will provide localizations needed for the Marathi
language. Currently the package localizes package blindtext and
package expex.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/marathi
%{_texmfdistdir}/tex/latex/marathi
%doc %{_texmfdistdir}/doc/latex/marathi

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

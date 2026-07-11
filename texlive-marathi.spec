%global tl_name marathi
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Typeset Marathi language using XeLaTeX or LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/marathi
License:	gpl3+ other-free fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marathi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marathi.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marathi.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
luaa-laattek v jhii-laattek hyaaNcyaash mraatthiicaa sulbh vaapr
krnnyaasaatthii. laattek-vriil mraatthiicyaa sthaanikiikrnnaace kaam
hyaa aajnyaasNcaamaarpht kele jaaiil. expex v blindtext hyaa
aajnyaasNcaaNce sthaanikiikrnn tuurtaas hyaa aajnyaasNcaamaarpht purvle
jaat aahe. For conveniently typesetting Marathi language with LuaLaTeX
and XeLaTeX. This package will provide localizations needed for the
Marathi language. Currently the package localizes package blindtext and
package expex.


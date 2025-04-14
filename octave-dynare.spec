%global octpkg dynare

Summary:	Dynare is a software platform for handling a wide class of economic models, in 
Name:		octave-dynare
Version:	6.3
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/dynare/
Url:		https://www.dynare.org/
Source0:	https://www.dynare.org/release/source/dynare-%{version}.tar.xz
BuildRequires:	octave-devel >= 7.1.0
BuildRequires:	boost-devel
BuildRequires:	meson
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	octave-control
BuildRequires:	octave-io
BuildRequires:	octave-optim
BuildRequires:	octave-statistics
BuildRequires:	pkgconfig(libfl)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(matio)
BuildRequires:	slicot-devel
BuildRequires:	suitesparse
#BuildRequires:	x13as-devel
# docs
#BuildRequires:	latexmk
BuildRequires:	mathjax
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	texlive

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildSystem:	meson
BuildOption:	-Dbuild_for=octave
BuildOption:	-Dmathjax_path=/usr/share/javascript/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML
#BuildOption:	--buildtype=debugoptimized

%description
Dynare is a software platform for handling a wide class of economic 
models, in particular dynamic stochastic general equilibrium (DSGE) 
and overlapping generations (OLG) models. The models solved by Dynare 
include those relying on the rational expectations hypothesis, 
wherein agents form their expectations about the future in a way 
consistent with the model. But Dynare is also able to handle models 
where expectations are formed differently: on one extreme, models 
where agents perfectly anticipate the future; on the other extreme, 
models where agents have limited rationality or imperfect knowledge 
of the state of the economy and, hence, form their expectations 
through a learning process. In terms of types of agents, models 
solved by Dynare can incorporate consumers, productive firms, 
governments, monetary authorities, investors and financial 
intermediaries. Some degree of heterogeneity can be achieved by 
including several distinct classes of agents in each of the 
aforementioned agent categories.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*


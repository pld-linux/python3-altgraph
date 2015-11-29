# %bcond_without	tests	# do not perform "make test"

%define 	module	altgraph
Summary:	Graph (network) package
Name:		python-%{module}
Version:	0.10.1
Release:	1
License:	zlib/libpng
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/a/altgraph/altgraph-%{version}.tar.gz
# Source0-md5:	ebef6fff05ea80c6499ac302151a026f
URL:		http://pypi.python.org/pypi/altgraph
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
altgraph is a fork of graphlib: a graph (network) package for
constructing graphs, BFS and DFS traversals, topological sort,
shortest paths, etc. with graphviz output.

%prep
%setup -q -n altgraph-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}*.egg-info
%endif

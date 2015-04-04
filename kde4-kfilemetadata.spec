# $Revision:$, $Date:$
%define         _state          stable
%define         orgname		kfilemetadata
%define         qtver           4.8.3

Summary:	A library for extracting file metadata
Name:		kde4-kfilemetadata
Version:	4.14.3
Release:	2
License:	LGPLv2 or LGPLv3
Group:		X11/Applications
URL:		http://www.kde.org/
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	2e7143fd470bf84ac05475871119d9eb
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	ebook-tools-devel
BuildRequires:	exiv2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	poppler-qt4-devel
BuildRequires:	taglib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for extracting file metadata.

%package devel
Summary:	Developer files for %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
KFileMetaData development files and libraries.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
		-DHTML_INSTALL_DIR=%{_kdedocdir} \
		-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
		-DKDE4_ENABLE_FINAL=OFF \
		../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkfilemetadata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkfilemetadata.so.?
%attr(755,root,root) %{_libdir}/kde4/kfilemetadata_*.so
%{_datadir}/kde4/services/kfilemetadata_*.desktop
%{_datadir}/kde4/servicetypes/kfilemetadata*.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/kfilemetadata
%attr(755,root,root) %{_libdir}/libkfilemetadata.so
%{_libdir}/cmake/KFileMetaData

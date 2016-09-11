%define		_state		stable
%define		orgname		kfilemetadata
%define		qt_ver		4.8.3

Summary:	A library for extracting file metadata
Summary(pl.UTF-8):	Biblioteka do wydobywania metadanych plików
Name:		kde4-kfilemetadata
Version:	4.14.3
Release:	4
License:	LGPL v2.1 or LGPL v3
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	2e7143fd470bf84ac05475871119d9eb
URL:		http://www.kde.org/
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	ebook-tools-devel
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	ffmpeg-devel >= 1.0
BuildRequires:	kde4-kdegraphics-mobipocket-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	poppler-qt4-devel >= 0.12.1
BuildRequires:	taglib-devel
Requires:	exiv2-libs >= 0.21
Requires:	ffmpeg-libs >= 1.0
Requires:	kde4-kdelibs >= %{version}
Requires:	poppler-qt4 >= 0.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for extracting file metadata.

%description -l pl.UTF-8
Biblioteka do wydobywania metadanych plików.

%package devel
Summary:	Developer files for KFileMetaData library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki KFileMetaData
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qt_ver}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
KFileMetaData development files.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki KFileMetaData.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkfilemetadata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkfilemetadata.so.4
%attr(755,root,root) %{_libdir}/kde4/kfilemetadata_*.so
%{_datadir}/kde4/services/kfilemetadata_*.desktop
%{_datadir}/kde4/servicetypes/kfilemetadata*.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/kfilemetadata
%attr(755,root,root) %{_libdir}/libkfilemetadata.so
%{_libdir}/cmake/KFileMetaData

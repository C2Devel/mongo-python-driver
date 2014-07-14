%define __python /usr/bin/python
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define pkgname pymongo

# Fix private-shared-object-provides error
%{?filter_setup:
%filter_provides_in %{python_sitearch}.*\.so$
%filter_setup
}

Summary:  Python interface to MongoDB
Name:     python-mongo
Version:  2.6.3
Release:  CROC3%{?dist}
Provides: %name = %version-%release
License:  GPL
Group:    Development/Libraries
URL:      http://api.mongodb.org/python/

Source0:  pymongo.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  python, python-devel, python-setuptools, python-nose1.1
BuildRequires:  gcc, make

%description
PyMongo is a Python distribution containing tools for working
with MongoDB, and is the recommended way to work with MongoDB
from Python.


%prep
%setup -q -n %{pkgname}


%build
%__python setup.py build


%install
[ %buildroot = "/" ] || rm -rf %buildroot

%__python setup.py install \
	--skip-build \
	--root="%buildroot" \
	--install-lib="%python_sitearch"

rm -rf -- %buildroot/%python_sitearch/*.egg-info


## Test uses active mongodb connection
## TODO: run mongodb-server to complete all tests
# %check
# nosetests1.1


%files
%defattr(-, root, root, 0755)
%python_sitearch/bson
%python_sitearch/gridfs
%python_sitearch/pymongo


%clean
[ %buildroot = "/" ] || rm -rf %buildroot


%changelog
* Mon Jul 14 2014 Mikhail Ushanov <gm.mephisto@gmail.com> - 2.6.3-CROC3
- Remove 'Epoch'
- Added Makefile for native build in Koji
- Really build with C extension

* Thu Oct 24 2013 Dmitry Konishchev <konishchev@gmail.com> - 2.6.3-CROC2
- Replace CROC patches for write concern with write concern backport patches
  from PyMongo 2.7.

* Mon Oct 21 2013 Dmitry Konishchev <konishchev@gmail.com> - 2.6.3-CROC1
- New version.
- Build the module with C extension.
- Add CROC patches for write concern.

* Thu Sep 19 2013 Dmitry Konishchev <konishchev@gmail.com> - 2.6.2-CROC1
- New version.
- Fix the epoch.

* Fri Jan 25 2013 Dmitry Konishchev <konishchev@gmail.com> - 2.4.2-CROC1
- New version.

* Fri Dec 7 2012 Dmitry Konishchev <konishchev@gmail.com> - 2.4.1-CROC1
- New version.

* Thu Nov 29 2012 Dmitry Konishchev <konishchev@gmail.com> - 2.4-CROC1
- New version.

* Mon Nov 19 2012 Dmitry Konishchev <konishchev@gmail.com> - 2.3-CROC1
- New version.

* Mon Nov 15 2010 Alexey Gladkov <legion@altlinux.ru> - 1.9-croc1.20101115
- New development snapshot.

* Mon Jul 12 2010 Alexey Gladkov <legion@altlinux.ru> - 1.7-croc1
- Initial package.

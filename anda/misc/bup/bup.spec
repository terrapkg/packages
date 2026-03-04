Name:			bup
Version:		0.33.9
Release:		1%?dist
Summary:		Efficient backup system based on the git packfile format
License:		LGPL-2.0-only
URL:			https://bup.github.io
Source0:		https://github.com/bup/bup/archive/refs/tags/%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:  python3-devel
BuildRequires:	gcc-c++ git-core
BuildRequires:  pandoc
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(libacl)
Requires:		python3

%description
bup is a program that backs things up. It's short for "backup." Can you believe that nobody else has named an open source program "bup" after all this time? Me neither.

%package doc
Summary:	HTML documentations for %name
BuildArch:	noarch
%description doc
HTML documentations for %name.

%prep
%autosetup

%build
./configure
%make_build

%install
%make_install PREFIX=%_prefix LIBDIR=%_libdir/bup

%files doc
%license LICENSE
%doc %_pkgdocdir/bup-bloom.1.html
%doc %_pkgdocdir/bup-cat-file.1.html
%doc %_pkgdocdir/bup-config.5.html
%doc %_pkgdocdir/bup-daemon.1.html
%doc %_pkgdocdir/bup-damage.1.html
%doc %_pkgdocdir/bup-drecurse.1.html
%doc %_pkgdocdir/bup-features.1.html
%doc %_pkgdocdir/bup-fsck.1.html
%doc %_pkgdocdir/bup-ftp.1.html
%doc %_pkgdocdir/bup-fuse.1.html
%doc %_pkgdocdir/bup-gc.1.html
%doc %_pkgdocdir/bup-get.1.html
%doc %_pkgdocdir/bup-help.1.html
%doc %_pkgdocdir/bup-import-duplicity.1.html
%doc %_pkgdocdir/bup-import-rdiff-backup.1.html
%doc %_pkgdocdir/bup-import-rsnapshot.1.html
%doc %_pkgdocdir/bup-index.1.html
%doc %_pkgdocdir/bup-init.1.html
%doc %_pkgdocdir/bup-join.1.html
%doc %_pkgdocdir/bup-ls.1.html
%doc %_pkgdocdir/bup-margin.1.html
%doc %_pkgdocdir/bup-memtest.1.html
%doc %_pkgdocdir/bup-meta.1.html
%doc %_pkgdocdir/bup-midx.1.html
%doc %_pkgdocdir/bup-mux.1.html
%doc %_pkgdocdir/bup-on.1.html
%doc %_pkgdocdir/bup-prune-older.1.html
%doc %_pkgdocdir/bup-random.1.html
%doc %_pkgdocdir/bup-restore.1.html
%doc %_pkgdocdir/bup-rm.1.html
%doc %_pkgdocdir/bup-save.1.html
%doc %_pkgdocdir/bup-server.1.html
%doc %_pkgdocdir/bup-split.1.html
%doc %_pkgdocdir/bup-tag.1.html
%doc %_pkgdocdir/bup-tick.1.html
%doc %_pkgdocdir/bup-validate-object-links.1.html
%doc %_pkgdocdir/bup-validate-ref-links.1.html
%doc %_pkgdocdir/bup-web.1.html
%doc %_pkgdocdir/bup.1.html

%files
%license LICENSE
%doc README.md DESIGN HACKING 
%_bindir/bup
%_libdir/bup/
%_mandir/man1/bup-bloom.1.*
%_mandir/man1/bup-cat-file.1.*
%_mandir/man1/bup-daemon.1.*
%_mandir/man1/bup-damage.1.*
%_mandir/man1/bup-drecurse.1.*
%_mandir/man1/bup-features.1.*
%_mandir/man1/bup-fsck.1.*
%_mandir/man1/bup-ftp.1.*
%_mandir/man1/bup-fuse.1.*
%_mandir/man1/bup-gc.1.*
%_mandir/man1/bup-get.1.*
%_mandir/man1/bup-help.1.*
%_mandir/man1/bup-import-duplicity.1.*
%_mandir/man1/bup-import-rdiff-backup.1.*
%_mandir/man1/bup-import-rsnapshot.1.*
%_mandir/man1/bup-index.1.*
%_mandir/man1/bup-init.1.*
%_mandir/man1/bup-join.1.*
%_mandir/man1/bup-ls.1.*
%_mandir/man1/bup-margin.1.*
%_mandir/man1/bup-memtest.1.*
%_mandir/man1/bup-meta.1.*
%_mandir/man1/bup-midx.1.*
%_mandir/man1/bup-mux.1.*
%_mandir/man1/bup-on.1.*
%_mandir/man1/bup-prune-older.1.*
%_mandir/man1/bup-random.1.*
%_mandir/man1/bup-restore.1.*
%_mandir/man1/bup-rm.1.*
%_mandir/man1/bup-save.1.*
%_mandir/man1/bup-server.1.*
%_mandir/man1/bup-split.1.*
%_mandir/man1/bup-tag.1.*
%_mandir/man1/bup-tick.1.*
%_mandir/man1/bup-validate-object-links.1.*
%_mandir/man1/bup-validate-ref-links.1.*
%_mandir/man1/bup-web.1.*
%_mandir/man1/bup.1.*
%_mandir/man5/bup-config.5.*

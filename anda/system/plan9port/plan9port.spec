%global commit cb7001c8d27f22f7229be302f53012bb1db52418
%global commit_date 20260208
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define _unpackaged_files_terminate_build 0

Name:           plan9port
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Plan 9 from User Space
URL:            https://9fans.github.io/plan9port/
Source0:        https://github.com/9fans/plan9port/archive/%commit/armillary-%commit.tar.gz
Source1:        acme.desktop
License:        MIT AND bzip2-1.0.6
BuildRequires:  gcc
BuildRequires:  perl
BuildRequires:  libXt-devel
BuildRequires:  fontconfig-devel
BuildRequires:  desktop-file-utils
Packager:       Owen Zimmerman <owen@fyralabs.com>
AutoReq:        0
Conflicts:      bash
Conflicts:      grep
Conflicts:      gawk
Conflicts:      unzip
Conflicts:      file
Conflicts:      sed
Conflicts:      tar
Conflicts:      diffutils
Conflicts:      bzip2
Conflicts:      shadow-utils
Conflicts:      procps-ng
Conflicts:      zip
Conflicts:      flex
Conflicts:      ed
Conflicts:      time
Conflicts:      gzip
Conflicts:      ImageMagick
Conflicts:      bc
Conflicts:      groff-base
Conflicts:      openssh-clients
Conflicts:      util-linux
Conflicts:      rubygem-bundler
Conflicts:      stack
Conflicts:      coreutils
Conflicts:      binutils
Conflicts:      glibc-common

%description
A port of many Plan 9 libraries and programs to Unix.

%package devel
%pkg_devel_files

%prep
%autosetup -n %{name}-%{commit}

%build
./INSTALL

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/
cp -r bin/*                            %{buildroot}%{_bindir}/
cp -r man/*                            %{buildroot}%{_mandir}/
install -Dm644 include/*.h          -t %{buildroot}%{_includedir}/
install -Dm644 lib/*.a              -t %{buildroot}%{_libdir}/
%desktop_file_install %{SOURCE1}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/acme.desktop

%files
%doc README.md CONTRIBUTING.md CONTRIBUTORS
%license LICENSE src/cmd/bzip2/LICENSE
%{_appsdir}/acme.desktop
%{_bindir}/9
%{_bindir}/9.rc
%{_bindir}/9ar
%{_bindir}/9c
%{_bindir}/9fs
%{_bindir}/9l
%{_bindir}/B
%{_bindir}/E
%{_bindir}/Getdir
%{_bindir}/adict
%{_bindir}/awd
%{_bindir}/bundle
%{_bindir}/disk/mkext
%{_bindir}/disk/mkfs
%{_bindir}/doctype
%{_bindir}/fossil/fossil
%{_bindir}/fossil/flchk
%{_bindir}/fossil/flfmt
%{_bindir}/fossil/conf
%{_bindir}/fossil/last
%{_bindir}/fossil/view
%{_bindir}/fs/tarfs
%{_bindir}/fs/tpfs
%{_bindir}/fs/v6fs
%{_bindir}/fs/32vfs
%{_bindir}/fs/cpiofs
%{_bindir}/fs/tapfs
%{_bindir}/fs/v10fs
%{_bindir}/fs/zipfs
%{_bindir}/g
%{_bindir}/ipso
%{_bindir}/kill
%{_bindir}/label
%{_bindir}/lc
%{_bindir}/lookman
%{_bindir}/macedit
%{_bindir}/man
%{_bindir}/mount
%{_bindir}/nobs
%{_bindir}/nroff
%{_bindir}/osxvers
%{_bindir}/ps
%{_bindir}/psfonts
%{_bindir}/psu
%{_bindir}/psv
%{_bindir}/quote1
%{_bindir}/quote2
%{_bindir}/samsave
%{_bindir}/sig
%{_bindir}/slay
%{_bindir}/soelim
%{_bindir}/spell
%{_bindir}/src
%{_bindir}/ssam
%{_bindir}/stack
%{_bindir}/start
%{_bindir}/stop
%{_bindir}/tref
%{_bindir}/troff2png
%{_bindir}/u
%{_bindir}/u.rc
%{_bindir}/unmount
%{_bindir}/upas/isspam
%{_bindir}/upas/msgcat
%{_bindir}/upas/spam
%{_bindir}/upas/spambox
%{_bindir}/upas/unspam
%{_bindir}/upas/unspambox
%{_bindir}/venti/copy
%{_bindir}/venti/read
%{_bindir}/venti/ro
%{_bindir}/venti/sync
%{_bindir}/venti/write
%{_bindir}/venti/dump
%{_bindir}/venti/venti
%{_bindir}/venti/buildindex
%{_bindir}/venti/checkarenas
%{_bindir}/venti/checkindex
%{_bindir}/venti/clumpstats
%{_bindir}/venti/conf
%{_bindir}/venti/findscore
%{_bindir}/venti/fixarenas
%{_bindir}/venti/fmtarenas
%{_bindir}/venti/fmtbloom
%{_bindir}/venti/fmtindex
%{_bindir}/venti/fmtisect
%{_bindir}/venti/mirrorarenas
%{_bindir}/venti/printarena
%{_bindir}/venti/printarenapart
%{_bindir}/venti/rdarena
%{_bindir}/venti/syncindex
%{_bindir}/venti/verifyarena
%{_bindir}/venti/wrarena
%{_bindir}/vmount
%{_bindir}/vwhois
%{_bindir}/web
%{_bindir}/wintext
%{_bindir}/wmail
%{_bindir}/yesterday
%{_bindir}/yacc
%{_bindir}/9import
%{_bindir}/9p
%{_bindir}/9pserve
%{_bindir}/acmeevent
%{_bindir}/ascii
%{_bindir}/auxclog
%{_bindir}/basename
%{_bindir}/bc
%{_bindir}/cal
%{_bindir}/calendar
%{_bindir}/cat
%{_bindir}/cleanname
%{_bindir}/cmp
%{_bindir}/col
%{_bindir}/comm
%{_bindir}/core
%{_bindir}/date
%{_bindir}/dc
%{_bindir}/dd
%{_bindir}/delatex
%{_bindir}/deroff
%{_bindir}/dial
%{_bindir}/du
%{_bindir}/echo
%{_bindir}/ed
%{_bindir}/factor
%{_bindir}/file
%{_bindir}/fmt
%{_bindir}/fortune
%{_bindir}/freq
%{_bindir}/fsize
%{_bindir}/getflags
%{_bindir}/hget
%{_bindir}/hist
%{_bindir}/idiff
%{_bindir}/import
%{_bindir}/join
%{_bindir}/listen1
%{_bindir}/look
%{_bindir}/ls
%{_bindir}/md5sum
%{_bindir}/mkdir
%{_bindir}/mntgen
%{_bindir}/mtime
%{_bindir}/namespace
%{_bindir}/netkey
%{_bindir}/news
%{_bindir}/pbd
%{_bindir}/p
%{_bindir}/pr
%{_bindir}/primes
%{_bindir}/ramfs
%{_bindir}/read
%{_bindir}/readcons
%{_bindir}/resample
%{_bindir}/rm
%{_bindir}/sed
%{_bindir}/seq
%{_bindir}/sftpcache
%{_bindir}/sha1sum
%{_bindir}/sleep
%{_bindir}/sort
%{_bindir}/split
%{_bindir}/srv
%{_bindir}/strings
%{_bindir}/sum
%{_bindir}/tail
%{_bindir}/tar
%{_bindir}/tee
%{_bindir}/test
%{_bindir}/time
%{_bindir}/touch
%{_bindir}/tr
%{_bindir}/unicode
%{_bindir}/uniq
%{_bindir}/units
%{_bindir}/unutf
%{_bindir}/usage
%{_bindir}/wc
%{_bindir}/xd
%{_bindir}/zerotrunc
%{_bindir}/lex
%{_bindir}/dump9660
%{_bindir}/mk9660
%{_bindir}/9660srv
%{_bindir}/9pfuse
%{_bindir}/9term
%{_bindir}/win
%{_bindir}/acid
%{_bindir}/acidtypes
%{_bindir}/acme
%{_bindir}/Mail
%{_bindir}/astro
%{_bindir}/asn12dsa
%{_bindir}/asn12rsa
%{_bindir}/dsagen
%{_bindir}/dsasign
%{_bindir}/dsa2pub
%{_bindir}/dsa2ssh
%{_bindir}/passwd
%{_bindir}/pemdecode
%{_bindir}/pemencode
%{_bindir}/rsagen
%{_bindir}/rsafill
%{_bindir}/rsa2csr
%{_bindir}/rsa2pub
%{_bindir}/rsa2ssh
%{_bindir}/rsa2x509
%{_bindir}/ssh-agent
%{_bindir}/factotum
%{_bindir}/aescbc
%{_bindir}/secstore
%{_bindir}/secstored
%{_bindir}/secuser
%{_bindir}/auxstats
%{_bindir}/awk
%{_bindir}/bzip2
%{_bindir}/bunzip2
%{_bindir}/cb
%{_bindir}/compress
%{_bindir}/zcat
%{_bindir}/uncompress
%{_bindir}/db
%{_bindir}/mklatinkbd
%{_bindir}/devdraw
%{_bindir}/dict
%{_bindir}/diff
%{_bindir}/clock
%{_bindir}/cmapcube
%{_bindir}/colors
%{_bindir}/crop
%{_bindir}/gview
%{_bindir}/iconv
%{_bindir}/img
%{_bindir}/mc
%{_bindir}/stats
%{_bindir}/statusbar
%{_bindir}/tcolors
%{_bindir}/tweak
%{_bindir}/eqn
%{_bindir}/fontsrv
%{_bindir}/grap
%{_bindir}/graph
%{_bindir}/grep
%{_bindir}/gzip
%{_bindir}/gunzip
%{_bindir}/zip
%{_bindir}/unzip
%{_bindir}/hoc
%{_bindir}/htmlfmt
%{_bindir}/htmlroff
%{_bindir}/jpg
%{_bindir}/gif
%{_bindir}/togif
%{_bindir}/ppm
%{_bindir}/toppm
%{_bindir}/png
%{_bindir}/topng
%{_bindir}/yuv
%{_bindir}/ico
%{_bindir}/toico
%{_bindir}/bmp
%{_bindir}/mapd
%{_bindir}/mk
%{_bindir}/dns
%{_bindir}/dnsquery
%{_bindir}/dnsdebug
%{_bindir}/dnstcp
%{_bindir}/ndbmkdb
%{_bindir}/ndbquery
%{_bindir}/ndbmkhash
%{_bindir}/ndbmkhosts
%{_bindir}/ndbipquery
%{_bindir}/Netfiles
%{_bindir}/netfileget
%{_bindir}/netfileput
%{_bindir}/netfilestat
%{_bindir}/netfilelib.rc
%{_bindir}/page
%{_bindir}/paint
%{_bindir}/pic
%{_bindir}/plot
%{_bindir}/plumber
%{_bindir}/plumb
%{_bindir}/tr2post
%{_bindir}/psdownload
%{_bindir}/proof
%{_bindir}/rc
%{_bindir}/rio
%{_bindir}/winwatch
%{_bindir}/xshove
%{_bindir}/sam
%{_bindir}/samterm
%{_bindir}/scat
%{_bindir}/sprog
%{_bindir}/svgpic
%{_bindir}/tbl
%{_bindir}/tcs
%{_bindir}/tpic
%{_bindir}/troff
%{_bindir}/troff2html
%{_bindir}/vac
%{_bindir}/vacfs
%{_bindir}/unvac
%{_bindir}/disknfs
%{_bindir}/vbackup
%{_bindir}/vcat
%{_bindir}/vmount0
%{_bindir}/vnfs
%{_mandir}/man1/0intro.1.*
%{_mandir}/man1/9.1.*
%{_mandir}/man1/9c.1.*
%{_mandir}/man1/9p.1.*
%{_mandir}/man1/9term.1.*
%{_mandir}/man1/acid.1.*
%{_mandir}/man1/acme.1.*
%{_mandir}/man1/acmeevent.1.*
%{_mandir}/man1/ascii.1.*
%{_mandir}/man1/astro.1.*
%{_mandir}/man1/awk.1.*
%{_mandir}/man1/basename.1.*
%{_mandir}/man1/bc.1.*
%{_mandir}/man1/bundle.1.*
%{_mandir}/man1/cal.1.*
%{_mandir}/man1/calendar.1.*
%{_mandir}/man1/cat.1.*
%{_mandir}/man1/cleanname.1.*
%{_mandir}/man1/clog.1.*
%{_mandir}/man1/cmp.1.*
%{_mandir}/man1/col.1.*
%{_mandir}/man1/colors.1.*
%{_mandir}/man1/comm.1.*
%{_mandir}/man1/compress.1.*
%{_mandir}/man1/core.1.*
%{_mandir}/man1/crop.1.*
%{_mandir}/man1/date.1.*
%{_mandir}/man1/db.1.*
%{_mandir}/man1/dc.1.*
%{_mandir}/man1/dd.1.*
%{_mandir}/man1/deroff.1.*
%{_mandir}/man1/devdraw.1.*
%{_mandir}/man1/dial.1.*
%{_mandir}/man1/dict.1.*
%{_mandir}/man1/diff.1.*
%{_mandir}/man1/doctype.1.*
%{_mandir}/man1/echo.1.*
%{_mandir}/man1/ed.1.*
%{_mandir}/man1/eqn.1.*
%{_mandir}/man1/factor.1.*
%{_mandir}/man1/fmt.1.*
%{_mandir}/man1/fortune.1.*
%{_mandir}/man1/freq.1.*
%{_mandir}/man1/fsize.1.*
%{_mandir}/man1/git.1.*
%{_mandir}/man1/grap.1.*
%{_mandir}/man1/graph.1.*
%{_mandir}/man1/grep.1.*
%{_mandir}/man1/gview.1.*
%{_mandir}/man1/gzip.1.*
%{_mandir}/man1/hget.1.*
%{_mandir}/man1/hist.1.*
%{_mandir}/man1/hoc.1.*
%{_mandir}/man1/htmlroff.1.*
%{_mandir}/man1/idiff.1.*
%{_mandir}/man1/install.1.*
%{_mandir}/man1/join.1.*
%{_mandir}/man1/jpg.1.*
%{_mandir}/man1/kill.1.*
%{_mandir}/man1/label.1.*
%{_mandir}/man1/lex.1.*
%{_mandir}/man1/look.1.*
%{_mandir}/man1/ls.1.*
%{_mandir}/man1/man.1.*
%{_mandir}/man1/map.1.*
%{_mandir}/man1/mc.1.*
%{_mandir}/man1/mk.1.*
%{_mandir}/man1/mk9660.1.*
%{_mandir}/man1/mkdir.1.*
%{_mandir}/man1/mount.1.*
%{_mandir}/man1/namespace.1.*
%{_mandir}/man1/ndb.1.*
%{_mandir}/man1/netfiles.1.*
%{_mandir}/man1/news.1.*
%{_mandir}/man1/p.1.*
%{_mandir}/man1/page.1.*
%{_mandir}/man1/paint.1.*
%{_mandir}/man1/passwd.1.*
%{_mandir}/man1/pem.1.*
%{_mandir}/man1/pic.1.*
%{_mandir}/man1/plot.1.*
%{_mandir}/man1/plumb.1.*
%{_mandir}/man1/pr.1.*
%{_mandir}/man1/proof.1.*
%{_mandir}/man1/ps.1.*
%{_mandir}/man1/psfonts.1.*
%{_mandir}/man1/pwd.1.*
%{_mandir}/man1/rc.1.*
%{_mandir}/man1/readcons.1.*
%{_mandir}/man1/resample.1.*
%{_mandir}/man1/rio.1.*
%{_mandir}/man1/rm.1.*
%{_mandir}/man1/rsa.1.*
%{_mandir}/man1/sam.1.*
%{_mandir}/man1/scat.1.*
%{_mandir}/man1/secstore.1.*
%{_mandir}/man1/secstored.1.*
%{_mandir}/man1/sed.1.*
%{_mandir}/man1/seq.1.*
%{_mandir}/man1/sftpcache.1.*
%{_mandir}/man1/sleep.1.*
%{_mandir}/man1/snarfer.1.*
%{_mandir}/man1/soelim.1.*
%{_mandir}/man1/sort.1.*
%{_mandir}/man1/spell.1.*
%{_mandir}/man1/split.1.*
%{_mandir}/man1/src.1.*
%{_mandir}/man1/ssam.1.*
%{_mandir}/man1/ssh-agent.1.*
%{_mandir}/man1/stats.1.*
%{_mandir}/man1/strings.1.*
%{_mandir}/man1/sum.1.*
%{_mandir}/man1/tail.1.*
%{_mandir}/man1/tar.1.*
%{_mandir}/man1/tbl.1.*
%{_mandir}/man1/tcs.1.*
%{_mandir}/man1/tee.1.*
%{_mandir}/man1/test.1.*
%{_mandir}/man1/time.1.*
%{_mandir}/man1/touch.1.*
%{_mandir}/man1/tr.1.*
%{_mandir}/man1/tr2post.1.*
%{_mandir}/man1/troff.1.*
%{_mandir}/man1/troff2html.1.*
%{_mandir}/man1/tweak.1.*
%{_mandir}/man1/uniq.1.*
%{_mandir}/man1/units.1.*
%{_mandir}/man1/vac.1.*
%{_mandir}/man1/venti.1.*
%{_mandir}/man1/wc.1.*
%{_mandir}/man1/web.1.*
%{_mandir}/man1/wintext.1.*
%{_mandir}/man1/winwatch.1.*
%{_mandir}/man1/xd.1.*
%{_mandir}/man1/yacc.1.*
%{_mandir}/man1/yesterday.1.*
%{_mandir}/man3/0intro.3.*
%{_mandir}/man3/9p-cmdbuf.3.*
%{_mandir}/man3/9p-fid.3.*
%{_mandir}/man3/9p-file.3.*
%{_mandir}/man3/9p-intmap.3.*
%{_mandir}/man3/9p.3.*
%{_mandir}/man3/9pclient.3.*
%{_mandir}/man3/acme.3.*
%{_mandir}/man3/addpt.3.*
%{_mandir}/man3/aes.3.*
%{_mandir}/man3/allocimage.3.*
%{_mandir}/man3/arg.3.*
%{_mandir}/man3/arith3.3.*
%{_mandir}/man3/atof.3.*
%{_mandir}/man3/auth.3.*
%{_mandir}/man3/authsrv.3.*
%{_mandir}/man3/avl.3.*
%{_mandir}/man3/bin.3.*
%{_mandir}/man3/bio.3.*
%{_mandir}/man3/blowfish.3.*
%{_mandir}/man3/cachechars.3.*
%{_mandir}/man3/cleanname.3.*
%{_mandir}/man3/color.3.*
%{_mandir}/man3/complete.3.*
%{_mandir}/man3/cputime.3.*
%{_mandir}/man3/ctime.3.*
%{_mandir}/man3/des.3.*
%{_mandir}/man3/dial.3.*
%{_mandir}/man3/dirread.3.*
%{_mandir}/man3/draw.3.*
%{_mandir}/man3/drawfcall.3.*
%{_mandir}/man3/dsa.3.*
%{_mandir}/man3/dup.3.*
%{_mandir}/man3/elgamal.3.*
%{_mandir}/man3/encode.3.*
%{_mandir}/man3/encrypt.3.*
%{_mandir}/man3/errstr.3.*
%{_mandir}/man3/event.3.*
%{_mandir}/man3/exec.3.*
%{_mandir}/man3/exits.3.*
%{_mandir}/man3/fcall.3.*
%{_mandir}/man3/flate.3.*
%{_mandir}/man3/fmtinstall.3.*
%{_mandir}/man3/frame.3.*
%{_mandir}/man3/genrandom.3.*
%{_mandir}/man3/get9root.3.*
%{_mandir}/man3/getcallerpc.3.*
%{_mandir}/man3/getenv.3.*
%{_mandir}/man3/getfields.3.*
%{_mandir}/man3/getns.3.*
%{_mandir}/man3/getsnarf.3.*
%{_mandir}/man3/getuser.3.*
%{_mandir}/man3/getwd.3.*
%{_mandir}/man3/graphics.3.*
%{_mandir}/man3/html.3.*
%{_mandir}/man3/ioproc.3.*
%{_mandir}/man3/ip.3.*
%{_mandir}/man3/isalpharune.3.*
%{_mandir}/man3/keyboard.3.*
%{_mandir}/man3/lock.3.*
%{_mandir}/man3/mach-cmd.3.*
%{_mandir}/man3/mach-file.3.*
%{_mandir}/man3/mach-map.3.*
%{_mandir}/man3/mach-stack.3.*
%{_mandir}/man3/mach-swap.3.*
%{_mandir}/man3/mach-symbol.3.*
%{_mandir}/man3/mach.3.*
%{_mandir}/man3/malloc.3.*
%{_mandir}/man3/matrix.3.*
%{_mandir}/man3/memdraw.3.*
%{_mandir}/man3/memlayer.3.*
%{_mandir}/man3/memory.3.*
%{_mandir}/man3/mouse.3.*
%{_mandir}/man3/mousescrollsize.3.*
%{_mandir}/man3/mp.3.*
%{_mandir}/man3/muldiv.3.*
%{_mandir}/man3/mux.3.*
%{_mandir}/man3/nan.3.*
%{_mandir}/man3/ndb.3.*
%{_mandir}/man3/needstack.3.*
%{_mandir}/man3/notify.3.*
%{_mandir}/man3/open.3.*
%{_mandir}/man3/opentemp.3.*
%{_mandir}/man3/pipe.3.*
%{_mandir}/man3/plumb.3.*
%{_mandir}/man3/post9pservice.3.*
%{_mandir}/man3/postnote.3.*
%{_mandir}/man3/prime.3.*
%{_mandir}/man3/print.3.*
%{_mandir}/man3/proto.3.*
%{_mandir}/man3/pushtls.3.*
%{_mandir}/man3/qball.3.*
%{_mandir}/man3/quaternion.3.*
%{_mandir}/man3/quote.3.*
%{_mandir}/man3/rand.3.*
%{_mandir}/man3/rc4.3.*
%{_mandir}/man3/read.3.*
%{_mandir}/man3/readcolmap.3.*
%{_mandir}/man3/readcons.3.*
%{_mandir}/man3/regexp.3.*
%{_mandir}/man3/rfork.3.*
%{_mandir}/man3/rsa.3.*
%{_mandir}/man3/rune.3.*
%{_mandir}/man3/runestrcat.3.*
%{_mandir}/man3/searchpath.3.*
%{_mandir}/man3/sechash.3.*
%{_mandir}/man3/seek.3.*
%{_mandir}/man3/sendfd.3.*
%{_mandir}/man3/setjmp.3.*
%{_mandir}/man3/sleep.3.*
%{_mandir}/man3/stat.3.*
%{_mandir}/man3/strcat.3.*
%{_mandir}/man3/string.3.*
%{_mandir}/man3/stringsize.3.*
%{_mandir}/man3/subfont.3.*
%{_mandir}/man3/sysfatal.3.*
%{_mandir}/man3/thread.3.*
%{_mandir}/man3/time.3.*
%{_mandir}/man3/udpread.3.*
%{_mandir}/man3/venti-cache.3.*
%{_mandir}/man3/venti-client.3.*
%{_mandir}/man3/venti-conn.3.*
%{_mandir}/man3/venti-fcall.3.*
%{_mandir}/man3/venti-file.3.*
%{_mandir}/man3/venti-log.3.*
%{_mandir}/man3/venti-mem.3.*
%{_mandir}/man3/venti-packet.3.*
%{_mandir}/man3/venti-server.3.*
%{_mandir}/man3/venti-zero.3.*
%{_mandir}/man3/venti.3.*
%{_mandir}/man3/wait.3.*
%{_mandir}/man3/wctl.3.*
%{_mandir}/man3/window.3.*
%{_mandir}/man4/0intro.4.*
%{_mandir}/man4/9import.4.*
%{_mandir}/man4/9pfuse.4.*
%{_mandir}/man4/9pserve.4.*
%{_mandir}/man4/acme.4.*
%{_mandir}/man4/factotum.4.*
%{_mandir}/man4/fontsrv.4.*
%{_mandir}/man4/fossil.4.*
%{_mandir}/man4/import.4.*
%{_mandir}/man4/mntgen.4.*
%{_mandir}/man4/plumber.4.*
%{_mandir}/man4/ramfs.4.*
%{_mandir}/man4/smugfs.4.*
%{_mandir}/man4/srv.4.*
%{_mandir}/man4/tapefs.4.*
%{_mandir}/man4/vacfs.4.*
%{_mandir}/man7/0intro.7.*
%{_mandir}/man7/color.7.*
%{_mandir}/man7/face.7.*
%{_mandir}/man7/font.7.*
%{_mandir}/man7/htmlroff.7.*
%{_mandir}/man7/image.7.*
%{_mandir}/man7/keyboard.7.*
%{_mandir}/man7/man.7.*
%{_mandir}/man7/map.7.*
%{_mandir}/man7/mhtml.7.*
%{_mandir}/man7/mpictures.7.*
%{_mandir}/man7/ms.7.*
%{_mandir}/man7/ndb.7.*
%{_mandir}/man7/plot.7.*
%{_mandir}/man7/plumb.7.*
%{_mandir}/man7/regexp.7.*
%{_mandir}/man7/thumbprint.7.*
%{_mandir}/man7/utf.7.*
%{_mandir}/man7/venti.7.*
%{_mandir}/man8/fossilcons.8.*
%{_mandir}/man8/getflags.8.*
%{_mandir}/man8/listen1.8.*
%{_mandir}/man8/mkfs.8.*
%{_mandir}/man8/vbackup.8.*
%{_mandir}/man8/venti-backup.8.*
%{_mandir}/man8/venti-fmt.8.*
%{_mandir}/man8/venti.8.*

%changelog
* Sun Feb 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit

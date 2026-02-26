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
Conflicts:      rubygem-bundler
Conflicts:      stack
Conflicts:      fossil

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
install -Dm755 bin/9                        %{buildroot}%{_bindir}/9
install -Dm755 bin/9.rc                     %{buildroot}%{_bindir}/9.rc
install -Dm755 bin/9ar                      %{buildroot}%{_bindir}/9ar
install -Dm755 bin/9c                       %{buildroot}%{_bindir}/9c
install -Dm755 bin/9fs                      %{buildroot}%{_bindir}/9fs
install -Dm755 bin/9l                       %{buildroot}%{_bindir}/9l
install -Dm755 bin/B                        %{buildroot}%{_bindir}/B
install -Dm755 bin/E                        %{buildroot}%{_bindir}/E
install -Dm755 bin/Getdir                   %{buildroot}%{_bindir}/Getdir
install -Dm755 bin/adict                    %{buildroot}%{_bindir}/adict
install -Dm755 bin/awd                      %{buildroot}%{_bindir}/awd
install -Dm755 bin/bundle                   %{buildroot}%{_bindir}/bundle
install -Dm755 bin/disk/mkext               %{buildroot}%{_bindir}/disk/mkext
install -Dm755 bin/disk/mkfs                %{buildroot}%{_bindir}/disk/9mkfs
install -Dm755 bin/doctype                  %{buildroot}%{_bindir}/doctype
install -Dm755 bin/fossil/fossil            %{buildroot}%{_bindir}/fossil/fossil
install -Dm755 bin/fossil/flchk             %{buildroot}%{_bindir}/fossil/flchk
install -Dm755 bin/fossil/flfmt             %{buildroot}%{_bindir}/fossil/flfmt
install -Dm755 bin/fossil/conf              %{buildroot}%{_bindir}/fossil/conf
install -Dm755 bin/fossil/last              %{buildroot}%{_bindir}/fossil/9last
install -Dm755 bin/fossil/view               %{buildroot}%{_bindir}/fossil/9view
install -Dm755 bin/fs/tarfs                 %{buildroot}%{_bindir}/fs/tarfs
install -Dm755 bin/fs/tpfs                  %{buildroot}%{_bindir}/fs/tpfs
install -Dm755 bin/fs/v6fs                  %{buildroot}%{_bindir}/fs/v6fs
install -Dm755 bin/fs/32vfs                 %{buildroot}%{_bindir}/fs/32vfs
install -Dm755 bin/fs/cpiofs                %{buildroot}%{_bindir}/fs/cpiofs
install -Dm755 bin/fs/tapfs                 %{buildroot}%{_bindir}/fs/tapfs
install -Dm755 bin/fs/v10fs                 %{buildroot}%{_bindir}/fs/v10fs
install -Dm755 bin/fs/zipfs                 %{buildroot}%{_bindir}/fs/zipfs
install -Dm755 bin/g                        %{buildroot}%{_bindir}/g
install -Dm755 bin/ipso                     %{buildroot}%{_bindir}/ipso
install -Dm755 bin/kill                     %{buildroot}%{_bindir}/9kill
install -Dm755 bin/label                    %{buildroot}%{_bindir}/label
install -Dm755 bin/lc                       %{buildroot}%{_bindir}/lc
install -Dm755 bin/lookman                  %{buildroot}%{_bindir}/lookman
install -Dm755 bin/macedit                  %{buildroot}%{_bindir}/macedit
install -Dm755 bin/man                      %{buildroot}%{_bindir}/9man
install -Dm755 bin/mount                    %{buildroot}%{_bindir}/9mount
install -Dm755 bin/nobs                     %{buildroot}%{_bindir}/nobs
install -Dm755 bin/nroff                    %{buildroot}%{_bindir}/9nroff
install -Dm755 bin/osxvers                  %{buildroot}%{_bindir}/osxvers
install -Dm755 bin/ps                       %{buildroot}%{_bindir}/9ps
install -Dm755 bin/psfonts                  %{buildroot}%{_bindir}/psfonts
install -Dm755 bin/psu                      %{buildroot}%{_bindir}/psu
install -Dm755 bin/psv                      %{buildroot}%{_bindir}/psv
install -Dm755 bin/quote1                   %{buildroot}%{_bindir}/quote1
install -Dm755 bin/quote2                   %{buildroot}%{_bindir}/quote2
install -Dm755 bin/samsave                  %{buildroot}%{_bindir}/samsave
install -Dm755 bin/sig                      %{buildroot}%{_bindir}/sig
install -Dm755 bin/slay                     %{buildroot}%{_bindir}/slay
install -Dm755 bin/soelim                   %{buildroot}%{_bindir}/9soelim
install -Dm755 bin/spell                    %{buildroot}%{_bindir}/spell
install -Dm755 bin/src                      %{buildroot}%{_bindir}/src
install -Dm755 bin/ssam                     %{buildroot}%{_bindir}/ssam
install -Dm755 bin/stack                    %{buildroot}%{_bindir}/stack
install -Dm755 bin/start                    %{buildroot}%{_bindir}/start
install -Dm755 bin/stop                     %{buildroot}%{_bindir}/stop
install -Dm755 bin/tref                     %{buildroot}%{_bindir}/tref
install -Dm755 bin/troff2png                %{buildroot}%{_bindir}/troff2png
install -Dm755 bin/u                        %{buildroot}%{_bindir}/u
install -Dm755 bin/u.rc                     %{buildroot}%{_bindir}/u.rc
install -Dm755 bin/unmount                  %{buildroot}%{_bindir}/unmount
install -Dm755 bin/upas/isspam              %{buildroot}%{_bindir}/upas/isspam
install -Dm755 bin/upas/msgcat              %{buildroot}%{_bindir}/upas/9msgcat
install -Dm755 bin/upas/spam                %{buildroot}%{_bindir}/upas/spam
install -Dm755 bin/upas/spambox             %{buildroot}%{_bindir}/upas/spambox
install -Dm755 bin/upas/unspam              %{buildroot}%{_bindir}/upas/unspam
install -Dm755 bin/upas/unspambox           %{buildroot}%{_bindir}/upas/unspambox
install -Dm755 bin/venti/copy               %{buildroot}%{_bindir}/venti/copy
install -Dm755 bin/venti/read               %{buildroot}%{_bindir}/venti/9read
install -Dm755 bin/venti/ro                 %{buildroot}%{_bindir}/venti/ro
install -Dm755 bin/venti/sync               %{buildroot}%{_bindir}/venti/9sync
install -Dm755 bin/venti/write              %{buildroot}%{_bindir}/venti/9write
install -Dm755 bin/venti/dump               %{buildroot}%{_bindir}/venti/dump
install -Dm755 bin/venti/venti              %{buildroot}%{_bindir}/venti/venti
install -Dm755 bin/venti/buildindex         %{buildroot}%{_bindir}/venti/buildindex
install -Dm755 bin/venti/checkarenas        %{buildroot}%{_bindir}/venti/checkarenas
install -Dm755 bin/venti/checkindex         %{buildroot}%{_bindir}/venti/checkindex
install -Dm755 bin/venti/clumpstats         %{buildroot}%{_bindir}/venti/clumpstats
install -Dm755 bin/venti/conf               %{buildroot}%{_bindir}/venti/conf
install -Dm755 bin/venti/findscore          %{buildroot}%{_bindir}/venti/findscore
install -Dm755 bin/venti/fixarenas          %{buildroot}%{_bindir}/venti/fixarenas
install -Dm755 bin/venti/fmtarenas          %{buildroot}%{_bindir}/venti/fmtarenas
install -Dm755 bin/venti/fmtbloom           %{buildroot}%{_bindir}/venti/fmtbloom
install -Dm755 bin/venti/fmtindex           %{buildroot}%{_bindir}/venti/fmtindex
install -Dm755 bin/venti/fmtisect           %{buildroot}%{_bindir}/venti/fmtisect
install -Dm755 bin/venti/mirrorarenas       %{buildroot}%{_bindir}/venti/mirrorarenas
install -Dm755 bin/venti/printarena         %{buildroot}%{_bindir}/venti/printarena
install -Dm755 bin/venti/printarenapart     %{buildroot}%{_bindir}/venti/printarenapart
install -Dm755 bin/venti/rdarena            %{buildroot}%{_bindir}/venti/rdarena
install -Dm755 bin/venti/syncindex          %{buildroot}%{_bindir}/venti/syncindex
install -Dm755 bin/venti/verifyarena        %{buildroot}%{_bindir}/venti/verifyarena
install -Dm755 bin/venti/wrarena            %{buildroot}%{_bindir}/venti/wrarena
install -Dm755 bin/vmount                   %{buildroot}%{_bindir}/vmount
install -Dm755 bin/vwhois                   %{buildroot}%{_bindir}/vwhois
install -Dm755 bin/web                      %{buildroot}%{_bindir}/web
install -Dm755 bin/wintext                  %{buildroot}%{_bindir}/wintext
install -Dm755 bin/wmail                    %{buildroot}%{_bindir}/wmail
install -Dm755 bin/yesterday                %{buildroot}%{_bindir}/yesterday
install -Dm755 bin/yacc                     %{buildroot}%{_bindir}/yacc
install -Dm755 bin/import                   %{buildroot}%{_bindir}/9import
install -Dm755 bin/9p                       %{buildroot}%{_bindir}/9p
install -Dm755 bin/9pserve                  %{buildroot}%{_bindir}/9pserve
install -Dm755 bin/acmeevent                %{buildroot}%{_bindir}/acmeevent
install -Dm755 bin/ascii                    %{buildroot}%{_bindir}/ascii
install -Dm755 bin/auxclog                  %{buildroot}%{_bindir}/auxclog
install -Dm755 bin/basename                 %{buildroot}%{_bindir}/9basename
install -Dm755 bin/bc                       %{buildroot}%{_bindir}/9bc
install -Dm755 bin/cal                      %{buildroot}%{_bindir}/9cal
install -Dm755 bin/calendar                 %{buildroot}%{_bindir}/calendar
install -Dm755 bin/cat                      %{buildroot}%{_bindir}/9cat
install -Dm755 bin/cleanname                %{buildroot}%{_bindir}/cleanname
install -Dm755 bin/cmp                      %{buildroot}%{_bindir}/9cmp
install -Dm755 bin/col                      %{buildroot}%{_bindir}/9col
install -Dm755 bin/comm                     %{buildroot}%{_bindir}/9comm
install -Dm755 bin/core                     %{buildroot}%{_bindir}/core
install -Dm755 bin/date                     %{buildroot}%{_bindir}/9date
install -Dm755 bin/dc                       %{buildroot}%{_bindir}/9dc
install -Dm755 bin/dd                       %{buildroot}%{_bindir}/9dd
install -Dm755 bin/delatex                  %{buildroot}%{_bindir}/delatex
install -Dm755 bin/deroff                   %{buildroot}%{_bindir}/deroff
install -Dm755 bin/dial                     %{buildroot}%{_bindir}/dial
install -Dm755 bin/du                       %{buildroot}%{_bindir}/9du
install -Dm755 bin/echo                     %{buildroot}%{_bindir}/9echo
install -Dm755 bin/ed                       %{buildroot}%{_bindir}/9ed
install -Dm755 bin/factor                   %{buildroot}%{_bindir}/9factor
install -Dm755 bin/file                     %{buildroot}%{_bindir}/9file
install -Dm755 bin/fmt                      %{buildroot}%{_bindir}/9fmt
install -Dm755 bin/fortune                  %{buildroot}%{_bindir}/fortune
install -Dm755 bin/freq                     %{buildroot}%{_bindir}/freq
install -Dm755 bin/fsize                    %{buildroot}%{_bindir}/fsize
install -Dm755 bin/getflags                 %{buildroot}%{_bindir}/getflags
install -Dm755 bin/hget                     %{buildroot}%{_bindir}/hget
install -Dm755 bin/hist                     %{buildroot}%{_bindir}/hist
install -Dm755 bin/idiff                    %{buildroot}%{_bindir}/idiff
install -Dm755 bin/import                   %{buildroot}%{_bindir}/9import
install -Dm755 bin/join                     %{buildroot}%{_bindir}/9join
install -Dm755 bin/listen1                  %{buildroot}%{_bindir}/listen1
install -Dm755 bin/look                     %{buildroot}%{_bindir}/9look
install -Dm755 bin/ls                       %{buildroot}%{_bindir}/9ls
install -Dm755 bin/md5sum                   %{buildroot}%{_bindir}/9md5sum
install -Dm755 bin/mkdir                    %{buildroot}%{_bindir}/9mkdir
install -Dm755 bin/mntgen                   %{buildroot}%{_bindir}/mntgen
install -Dm755 bin/mtime                    %{buildroot}%{_bindir}/mtime
install -Dm755 bin/namespace                %{buildroot}%{_bindir}/namespace
install -Dm755 bin/netkey                   %{buildroot}%{_bindir}/netkey
install -Dm755 bin/news                     %{buildroot}%{_bindir}/news
install -Dm755 bin/pbd                      %{buildroot}%{_bindir}/pbd
install -Dm755 bin/p                        %{buildroot}%{_bindir}/p
install -Dm755 bin/pr                       %{buildroot}%{_bindir}/9pr
install -Dm755 bin/primes                   %{buildroot}%{_bindir}/primes
install -Dm755 bin/ramfs                    %{buildroot}%{_bindir}/ramfs
install -Dm755 bin/read                     %{buildroot}%{_bindir}/read
install -Dm755 bin/readcons                 %{buildroot}%{_bindir}/readcons
install -Dm755 bin/resample                 %{buildroot}%{_bindir}/resample
install -Dm755 bin/rm                       %{buildroot}%{_bindir}/9rm
install -Dm755 bin/sed                      %{buildroot}%{_bindir}/9sed
install -Dm755 bin/seq                      %{buildroot}%{_bindir}/9seq
install -Dm755 bin/sftpcache                %{buildroot}%{_bindir}/sftpcache
install -Dm755 bin/sha1sum                  %{buildroot}%{_bindir}/9sha1sum
install -Dm755 bin/sleep                    %{buildroot}%{_bindir}/9sleep
install -Dm755 bin/sort                     %{buildroot}%{_bindir}/9sort
install -Dm755 bin/split                    %{buildroot}%{_bindir}/9split
install -Dm755 bin/srv                      %{buildroot}%{_bindir}/srv
install -Dm755 bin/strings                  %{buildroot}%{_bindir}/9strings
install -Dm755 bin/sum                      %{buildroot}%{_bindir}/9sum
install -Dm755 bin/tail                     %{buildroot}%{_bindir}/9tail
install -Dm755 bin/tar                      %{buildroot}%{_bindir}/9tar
install -Dm755 bin/tee                      %{buildroot}%{_bindir}/9tee
install -Dm755 bin/test                     %{buildroot}%{_bindir}/9test
install -Dm755 bin/time                     %{buildroot}%{_bindir}/9time
install -Dm755 bin/touch                    %{buildroot}%{_bindir}/9touch
install -Dm755 bin/tr                       %{buildroot}%{_bindir}/9tr
install -Dm755 bin/unicode                  %{buildroot}%{_bindir}/unicode
install -Dm755 bin/uniq                     %{buildroot}%{_bindir}/9uniq
install -Dm755 bin/units                    %{buildroot}%{_bindir}/units
install -Dm755 bin/unutf                    %{buildroot}%{_bindir}/unutf
install -Dm755 bin/usage                    %{buildroot}%{_bindir}/usage
install -Dm755 bin/wc                       %{buildroot}%{_bindir}/9wc
install -Dm755 bin/xd                       %{buildroot}%{_bindir}/xd
install -Dm755 bin/zerotrunc                %{buildroot}%{_bindir}/zerotrunc
install -Dm755 bin/lex                      %{buildroot}%{_bindir}/9lex
install -Dm755 bin/dump9660                 %{buildroot}%{_bindir}/dump9660
install -Dm755 bin/mk9660                   %{buildroot}%{_bindir}/mk9660
install -Dm755 bin/9660srv                  %{buildroot}%{_bindir}/9660srv
install -Dm755 bin/9pfuse                   %{buildroot}%{_bindir}/9pfuse
install -Dm755 bin/9term                    %{buildroot}%{_bindir}/9term
install -Dm755 bin/win                      %{buildroot}%{_bindir}/win
install -Dm755 bin/acid                     %{buildroot}%{_bindir}/acid
install -Dm755 bin/acidtypes                %{buildroot}%{_bindir}/acidtypes
install -Dm755 bin/acme                     %{buildroot}%{_bindir}/acme
install -Dm755 bin/Mail                     %{buildroot}%{_bindir}/Mail
install -Dm755 bin/astro                    %{buildroot}%{_bindir}/astro
install -Dm755 bin/asn12dsa                 %{buildroot}%{_bindir}/asn12dsa
install -Dm755 bin/asn12rsa                 %{buildroot}%{_bindir}/asn12rsa
install -Dm755 bin/dsagen                   %{buildroot}%{_bindir}/dsagen
install -Dm755 bin/dsasign                  %{buildroot}%{_bindir}/dsasign
install -Dm755 bin/dsa2pub                  %{buildroot}%{_bindir}/dsa2pub
install -Dm755 bin/dsa2ssh                  %{buildroot}%{_bindir}/dsa2ssh
install -Dm755 bin/passwd                   %{buildroot}%{_bindir}/9passwd
install -Dm755 bin/pemdecode                %{buildroot}%{_bindir}/pemdecode
install -Dm755 bin/pemencode                %{buildroot}%{_bindir}/pemencode
install -Dm755 bin/rsagen                   %{buildroot}%{_bindir}/rsagen
install -Dm755 bin/rsafill                  %{buildroot}%{_bindir}/rsafill
install -Dm755 bin/rsa2csr                  %{buildroot}%{_bindir}/rsa2csr
install -Dm755 bin/rsa2pub                  %{buildroot}%{_bindir}/rsa2pub
install -Dm755 bin/rsa2ssh                  %{buildroot}%{_bindir}/rsa2ssh
install -Dm755 bin/rsa2x509                 %{buildroot}%{_bindir}/rsa2x509
install -Dm755 bin/ssh-agent                %{buildroot}%{_bindir}/9ssh-agent
install -Dm755 bin/factotum                 %{buildroot}%{_bindir}/factotum
install -Dm755 bin/aescbc                   %{buildroot}%{_bindir}/aescbc
install -Dm755 bin/secstore                 %{buildroot}%{_bindir}/secstore
install -Dm755 bin/secstored                %{buildroot}%{_bindir}/secstored
install -Dm755 bin/secuser                  %{buildroot}%{_bindir}/secuser
install -Dm755 bin/auxstats                 %{buildroot}%{_bindir}/auxstats
install -Dm755 bin/awk                      %{buildroot}%{_bindir}/9awk
install -Dm755 bin/bzip2                    %{buildroot}%{_bindir}/9bzip2
install -Dm755 bin/bunzip2                  %{buildroot}%{_bindir}/9bunzip2
install -Dm755 bin/cb                       %{buildroot}%{_bindir}/cb
install -Dm755 bin/compress                 %{buildroot}%{_bindir}/compress
install -Dm755 bin/zcat                     %{buildroot}%{_bindir}/9zcat
install -Dm755 bin/uncompress               %{buildroot}%{_bindir}/uncompress
install -Dm755 bin/db                       %{buildroot}%{_bindir}/db
install -Dm755 bin/mklatinkbd               %{buildroot}%{_bindir}/mklatinkbd
install -Dm755 bin/devdraw                  %{buildroot}%{_bindir}/devdraw
install -Dm755 bin/dict                     %{buildroot}%{_bindir}/dict
install -Dm755 bin/diff                     %{buildroot}%{_bindir}/9diff
install -Dm755 bin/clock                    %{buildroot}%{_bindir}/9clock
install -Dm755 bin/cmapcube                 %{buildroot}%{_bindir}/cmapcube
install -Dm755 bin/colors                   %{buildroot}%{_bindir}/colors
install -Dm755 bin/crop                     %{buildroot}%{_bindir}/crop
install -Dm755 bin/gview                    %{buildroot}%{_bindir}/9gview
install -Dm755 bin/iconv                    %{buildroot}%{_bindir}/9iconv
install -Dm755 bin/img                      %{buildroot}%{_bindir}/img
install -Dm755 bin/mc                       %{buildroot}%{_bindir}/mc
install -Dm755 bin/stats                    %{buildroot}%{_bindir}/stats
install -Dm755 bin/statusbar                %{buildroot}%{_bindir}/statusbar
install -Dm755 bin/tcolors                  %{buildroot}%{_bindir}/tcolors
install -Dm755 bin/tweak                    %{buildroot}%{_bindir}/tweak
install -Dm755 bin/eqn                      %{buildroot}%{_bindir}/9eqn
install -Dm755 bin/fontsrv                  %{buildroot}%{_bindir}/fontsrv
install -Dm755 bin/grap                     %{buildroot}%{_bindir}/grap
install -Dm755 bin/graph                    %{buildroot}%{_bindir}/graph
install -Dm755 bin/grep                     %{buildroot}%{_bindir}/9grep
install -Dm755 bin/gzip                     %{buildroot}%{_bindir}/9gzip
install -Dm755 bin/gunzip                   %{buildroot}%{_bindir}/9gunzip
install -Dm755 bin/zip                      %{buildroot}%{_bindir}/9zip
install -Dm755 bin/unzip                    %{buildroot}%{_bindir}/9unzip
install -Dm755 bin/hoc                      %{buildroot}%{_bindir}/hoc
install -Dm755 bin/htmlfmt                  %{buildroot}%{_bindir}/htmlfmt
install -Dm755 bin/htmlroff                 %{buildroot}%{_bindir}/htmlroff
install -Dm755 bin/jpg                      %{buildroot}%{_bindir}/jpg
install -Dm755 bin/gif                      %{buildroot}%{_bindir}/gif
install -Dm755 bin/togif                    %{buildroot}%{_bindir}/togif
install -Dm755 bin/ppm                      %{buildroot}%{_bindir}/ppm
install -Dm755 bin/toppm                    %{buildroot}%{_bindir}/toppm
install -Dm755 bin/png                      %{buildroot}%{_bindir}/png
install -Dm755 bin/topng                    %{buildroot}%{_bindir}/topng
install -Dm755 bin/yuv                      %{buildroot}%{_bindir}/yuv
install -Dm755 bin/ico                      %{buildroot}%{_bindir}/ico
install -Dm755 bin/toico                    %{buildroot}%{_bindir}/toico
install -Dm755 bin/bmp                      %{buildroot}%{_bindir}/bmp
install -Dm755 bin/mapd                     %{buildroot}%{_bindir}/mapd
install -Dm755 bin/mk                       %{buildroot}%{_bindir}/mk
install -Dm755 bin/dns                      %{buildroot}%{_bindir}/dns
install -Dm755 bin/dnsquery                 %{buildroot}%{_bindir}/dnsquery
install -Dm755 bin/dnsdebug                 %{buildroot}%{_bindir}/dnsdebug
install -Dm755 bin/dnstcp                   %{buildroot}%{_bindir}/dnstcp
install -Dm755 bin/ndbmkdb                  %{buildroot}%{_bindir}/ndbmkdb
install -Dm755 bin/ndbquery                 %{buildroot}%{_bindir}/ndbquery
install -Dm755 bin/ndbmkhash                %{buildroot}%{_bindir}/ndbmkhash
install -Dm755 bin/ndbmkhosts               %{buildroot}%{_bindir}/ndbmkhosts
install -Dm755 bin/ndbipquery               %{buildroot}%{_bindir}/ndbipquery
install -Dm755 bin/Netfiles                 %{buildroot}%{_bindir}/Netfiles
install -Dm755 bin/netfileget               %{buildroot}%{_bindir}/netfileget
install -Dm755 bin/netfileput               %{buildroot}%{_bindir}/netfileput
install -Dm755 bin/netfilestat              %{buildroot}%{_bindir}/netfilestat
install -Dm755 bin/netfilelib.rc            %{buildroot}%{_bindir}/netfilelib.rc
install -Dm755 bin/page                     %{buildroot}%{_bindir}/page
install -Dm755 bin/paint                    %{buildroot}%{_bindir}/paint
install -Dm755 bin/pic                      %{buildroot}%{_bindir}/9pic
install -Dm755 bin/plot                     %{buildroot}%{_bindir}/plot
install -Dm755 bin/plumber                  %{buildroot}%{_bindir}/plumber
install -Dm755 bin/plumb                    %{buildroot}%{_bindir}/plumb
install -Dm755 bin/tr2post                  %{buildroot}%{_bindir}/tr2post
install -Dm755 bin/psdownload               %{buildroot}%{_bindir}/psdownload
install -Dm755 bin/proof                    %{buildroot}%{_bindir}/proof
install -Dm755 bin/rc                       %{buildroot}%{_bindir}/rc
install -Dm755 bin/rio                      %{buildroot}%{_bindir}/rio
install -Dm755 bin/winwatch                 %{buildroot}%{_bindir}/winwatch
install -Dm755 bin/xshove                   %{buildroot}%{_bindir}/xshove
install -Dm755 bin/sam                      %{buildroot}%{_bindir}/sam
install -Dm755 bin/samterm                  %{buildroot}%{_bindir}/samterm
install -Dm755 bin/scat                     %{buildroot}%{_bindir}/scat
install -Dm755 bin/sprog                    %{buildroot}%{_bindir}/sprog
install -Dm755 bin/svgpic                   %{buildroot}%{_bindir}/svgpic
install -Dm755 bin/tbl                      %{buildroot}%{_bindir}/9tbl
install -Dm755 bin/tcs                      %{buildroot}%{_bindir}/tcs
install -Dm755 bin/tpic                     %{buildroot}%{_bindir}/tpic
install -Dm755 bin/troff                    %{buildroot}%{_bindir}/9troff
install -Dm755 bin/troff2html               %{buildroot}%{_bindir}/troff2html
install -Dm755 bin/vac                      %{buildroot}%{_bindir}/vac
install -Dm755 bin/vacfs                    %{buildroot}%{_bindir}/vacfs
install -Dm755 bin/unvac                    %{buildroot}%{_bindir}/unvac
install -Dm755 bin/disknfs                  %{buildroot}%{_bindir}/disknfs
install -Dm755 bin/vbackup                  %{buildroot}%{_bindir}/vbackup
install -Dm755 bin/vcat                     %{buildroot}%{_bindir}/vcat
install -Dm755 bin/vmount0                  %{buildroot}%{_bindir}/vmount0
install -Dm755 bin/vnfs                     %{buildroot}%{_bindir}/vnfs
cp -r man/*                                 %{buildroot}%{_mandir}/
install -Dm644 include/*.h               -t %{buildroot}%{_includedir}/
install -Dm644 lib/*.a                   -t %{buildroot}%{_libdir}/
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
%{_bindir}/disk/9mkfs
%{_bindir}/doctype
%{_bindir}/fossil/fossil
%{_bindir}/fossil/flchk
%{_bindir}/fossil/flfmt
%{_bindir}/fossil/conf
%{_bindir}/fossil/9last
%{_bindir}/fossil/9view
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
%{_bindir}/9kill
%{_bindir}/label
%{_bindir}/lc
%{_bindir}/lookman
%{_bindir}/macedit
%{_bindir}/9man
%{_bindir}/9mount
%{_bindir}/nobs
%{_bindir}/9nroff
%{_bindir}/osxvers
%{_bindir}/9ps
%{_bindir}/psfonts
%{_bindir}/psu
%{_bindir}/psv
%{_bindir}/quote1
%{_bindir}/quote2
%{_bindir}/samsave
%{_bindir}/sig
%{_bindir}/slay
%{_bindir}/9soelim
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
%{_bindir}/upas/9msgcat
%{_bindir}/upas/spam
%{_bindir}/upas/spambox
%{_bindir}/upas/unspam
%{_bindir}/upas/unspambox
%{_bindir}/venti/copy
%{_bindir}/venti/9read
%{_bindir}/venti/ro
%{_bindir}/venti/9sync
%{_bindir}/venti/9write
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
%{_bindir}/9basename
%{_bindir}/9bc
%{_bindir}/9cal
%{_bindir}/calendar
%{_bindir}/9cat
%{_bindir}/cleanname
%{_bindir}/9cmp
%{_bindir}/9col
%{_bindir}/9comm
%{_bindir}/core
%{_bindir}/9date
%{_bindir}/9dc
%{_bindir}/9dd
%{_bindir}/delatex
%{_bindir}/deroff
%{_bindir}/dial
%{_bindir}/9du
%{_bindir}/9echo
%{_bindir}/9ed
%{_bindir}/9factor
%{_bindir}/9file
%{_bindir}/9fmt
%{_bindir}/fortune
%{_bindir}/freq
%{_bindir}/fsize
%{_bindir}/getflags
%{_bindir}/hget
%{_bindir}/hist
%{_bindir}/idiff
%{_bindir}/9import
%{_bindir}/9join
%{_bindir}/listen1
%{_bindir}/9look
%{_bindir}/9ls
%{_bindir}/9md5sum
%{_bindir}/9mkdir
%{_bindir}/mntgen
%{_bindir}/mtime
%{_bindir}/namespace
%{_bindir}/netkey
%{_bindir}/news
%{_bindir}/pbd
%{_bindir}/p
%{_bindir}/9pr
%{_bindir}/primes
%{_bindir}/ramfs
%{_bindir}/read
%{_bindir}/readcons
%{_bindir}/resample
%{_bindir}/9rm
%{_bindir}/9sed
%{_bindir}/9seq
%{_bindir}/sftpcache
%{_bindir}/9sha1sum
%{_bindir}/9sleep
%{_bindir}/9sort
%{_bindir}/9split
%{_bindir}/srv
%{_bindir}/9strings
%{_bindir}/9sum
%{_bindir}/9tail
%{_bindir}/9tar
%{_bindir}/9tee
%{_bindir}/9test
%{_bindir}/9time
%{_bindir}/9touch
%{_bindir}/9tr
%{_bindir}/unicode
%{_bindir}/9uniq
%{_bindir}/units
%{_bindir}/unutf
%{_bindir}/usage
%{_bindir}/9wc
%{_bindir}/xd
%{_bindir}/zerotrunc
%{_bindir}/9lex
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
%{_bindir}/9passwd
%{_bindir}/pemdecode
%{_bindir}/pemencode
%{_bindir}/rsagen
%{_bindir}/rsafill
%{_bindir}/rsa2csr
%{_bindir}/rsa2pub
%{_bindir}/rsa2ssh
%{_bindir}/rsa2x509
%{_bindir}/9ssh-agent
%{_bindir}/factotum
%{_bindir}/aescbc
%{_bindir}/secstore
%{_bindir}/secstored
%{_bindir}/secuser
%{_bindir}/auxstats
%{_bindir}/9awk
%{_bindir}/9bzip2
%{_bindir}/9bunzip2
%{_bindir}/cb
%{_bindir}/compress
%{_bindir}/9zcat
%{_bindir}/uncompress
%{_bindir}/db
%{_bindir}/mklatinkbd
%{_bindir}/devdraw
%{_bindir}/dict
%{_bindir}/9diff
%{_bindir}/9clock
%{_bindir}/cmapcube
%{_bindir}/colors
%{_bindir}/crop
%{_bindir}/9gview
%{_bindir}/9iconv
%{_bindir}/img
%{_bindir}/mc
%{_bindir}/stats
%{_bindir}/statusbar
%{_bindir}/tcolors
%{_bindir}/tweak
%{_bindir}/9eqn
%{_bindir}/fontsrv
%{_bindir}/grap
%{_bindir}/graph
%{_bindir}/9grep
%{_bindir}/9gzip
%{_bindir}/9gunzip
%{_bindir}/9zip
%{_bindir}/9unzip
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
%{_bindir}/9pic
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
%{_bindir}/9tbl
%{_bindir}/tcs
%{_bindir}/tpic
%{_bindir}/9troff
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

%global commit 337c6acbfed51d8d9f08598c6cd398f53abcca7d
%global commit_date 20260711
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           plan9port
Version:        0~%{commit_date}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Plan 9 from User Space
URL:            https://9fans.github.io/plan9port/
Source0:        https://github.com/9fans/plan9port/archive/%{commit}/plan9port-%{commit}.tar.gz
Source1:        acme.desktop
Source2:        sam.desktop
License:        MIT AND bzip2-1.0.6
BuildRequires:  gcc
BuildRequires:  perl
BuildRequires:  libXt-devel
BuildRequires:  fontconfig-devel
BuildRequires:  desktop-file-utils
Packager:       Owen Zimmerman <owen@fyralabs.com>
AutoReq:        0
Conflicts:      rubygem-bundler
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
install -Dm755 bin/fossil/view              %{buildroot}%{_bindir}/fossil/9view
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
install -Dm755 bin/stack                    %{buildroot}%{_bindir}/9stack
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
install -Dm755 bin/venti/read               %{buildroot}%{_bindir}/venti/venti-9read
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
install -Dm755 bin/fortune                  %{buildroot}%{_bindir}/9fortune
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
install -Dm755 bin/read                     %{buildroot}%{_bindir}/9read
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

install -Dm644 man/man1/0intro.1          %{buildroot}%{_mandir}/man1/0intro.1
install -Dm644 man/man1/9.1               %{buildroot}%{_mandir}/man1/9.1
install -Dm644 man/man1/9c.1              %{buildroot}%{_mandir}/man1/9c.1
install -Dm644 man/man1/9p.1              %{buildroot}%{_mandir}/man1/9p.1
install -Dm644 man/man1/9term.1           %{buildroot}%{_mandir}/man1/9term.1
install -Dm644 man/man1/acid.1            %{buildroot}%{_mandir}/man1/9acid.1
install -Dm644 man/man1/acme.1            %{buildroot}%{_mandir}/man1/acme.1
install -Dm644 man/man1/acmeevent.1       %{buildroot}%{_mandir}/man1/acmeevent.1
install -Dm644 man/man1/ascii.1           %{buildroot}%{_mandir}/man1/9ascii.1
install -Dm644 man/man1/astro.1           %{buildroot}%{_mandir}/man1/9astro.1
install -Dm644 man/man1/awk.1             %{buildroot}%{_mandir}/man1/9awk.1
install -Dm644 man/man1/basename.1        %{buildroot}%{_mandir}/man1/9basename.1
install -Dm644 man/man1/bc.1              %{buildroot}%{_mandir}/man1/9bc.1
install -Dm644 man/man1/bundle.1          %{buildroot}%{_mandir}/man1/9bundle.1
install -Dm644 man/man1/cal.1             %{buildroot}%{_mandir}/man1/9cal.1
install -Dm644 man/man1/calendar.1        %{buildroot}%{_mandir}/man1/9calendar.1
install -Dm644 man/man1/cat.1             %{buildroot}%{_mandir}/man1/9cat.1
install -Dm644 man/man1/cleanname.1       %{buildroot}%{_mandir}/man1/9cleanname.1
install -Dm644 man/man1/clog.1            %{buildroot}%{_mandir}/man1/9clog.1
install -Dm644 man/man1/cmp.1             %{buildroot}%{_mandir}/man1/9cmp.1
install -Dm644 man/man1/col.1             %{buildroot}%{_mandir}/man1/9col.1
install -Dm644 man/man1/colors.1          %{buildroot}%{_mandir}/man1/9colors.1
install -Dm644 man/man1/comm.1            %{buildroot}%{_mandir}/man1/9comm.1
install -Dm644 man/man1/compress.1        %{buildroot}%{_mandir}/man1/9compress.1
install -Dm644 man/man1/core.1            %{buildroot}%{_mandir}/man1/9core.1
install -Dm644 man/man1/crop.1            %{buildroot}%{_mandir}/man1/9crop.1
install -Dm644 man/man1/date.1            %{buildroot}%{_mandir}/man1/9date.1
install -Dm644 man/man1/db.1              %{buildroot}%{_mandir}/man1/9db.1
install -Dm644 man/man1/dc.1              %{buildroot}%{_mandir}/man1/9dc.1
install -Dm644 man/man1/dd.1              %{buildroot}%{_mandir}/man1/9dd.1
install -Dm644 man/man1/deroff.1          %{buildroot}%{_mandir}/man1/9deroff.1
install -Dm644 man/man1/devdraw.1         %{buildroot}%{_mandir}/man1/9devdraw.1
install -Dm644 man/man1/dial.1            %{buildroot}%{_mandir}/man1/9dial.1
install -Dm644 man/man1/dict.1            %{buildroot}%{_mandir}/man1/9dict.1
install -Dm644 man/man1/diff.1            %{buildroot}%{_mandir}/man1/9diff.1
install -Dm644 man/man1/doctype.1         %{buildroot}%{_mandir}/man1/9doctype.1
install -Dm644 man/man1/echo.1            %{buildroot}%{_mandir}/man1/9echo.1
install -Dm644 man/man1/ed.1              %{buildroot}%{_mandir}/man1/9ed.1
install -Dm644 man/man1/eqn.1             %{buildroot}%{_mandir}/man1/9eqn.1
install -Dm644 man/man1/factor.1          %{buildroot}%{_mandir}/man1/9factor.1
install -Dm644 man/man1/fmt.1             %{buildroot}%{_mandir}/man1/9fmt.1
install -Dm644 man/man1/fortune.1         %{buildroot}%{_mandir}/man1/9fortune.1
install -Dm644 man/man1/freq.1            %{buildroot}%{_mandir}/man1/9freq.1
install -Dm644 man/man1/fsize.1           %{buildroot}%{_mandir}/man1/9fsize.1
install -Dm644 man/man1/git.1             %{buildroot}%{_mandir}/man1/9git.1
install -Dm644 man/man1/grap.1            %{buildroot}%{_mandir}/man1/9grap.1
install -Dm644 man/man1/graph.1           %{buildroot}%{_mandir}/man1/9graph.1
install -Dm644 man/man1/grep.1            %{buildroot}%{_mandir}/man1/9grep.1
install -Dm644 man/man1/gview.1           %{buildroot}%{_mandir}/man1/9gview.1
install -Dm644 man/man1/gzip.1            %{buildroot}%{_mandir}/man1/9gzip.1
install -Dm644 man/man1/hget.1            %{buildroot}%{_mandir}/man1/9hget.1
install -Dm644 man/man1/hist.1            %{buildroot}%{_mandir}/man1/9hist.1
install -Dm644 man/man1/hoc.1             %{buildroot}%{_mandir}/man1/9hoc.1
install -Dm644 man/man1/htmlroff.1        %{buildroot}%{_mandir}/man1/9htmlroff.1
install -Dm644 man/man1/idiff.1           %{buildroot}%{_mandir}/man1/9idiff.1
install -Dm644 man/man1/install.1         %{buildroot}%{_mandir}/man1/9install.1
install -Dm644 man/man1/join.1            %{buildroot}%{_mandir}/man1/9join.1
install -Dm644 man/man1/jpg.1             %{buildroot}%{_mandir}/man1/9jpg.1
install -Dm644 man/man1/kill.1            %{buildroot}%{_mandir}/man1/9kill.1
install -Dm644 man/man1/label.1           %{buildroot}%{_mandir}/man1/9label.1
install -Dm644 man/man1/lex.1             %{buildroot}%{_mandir}/man1/9lex.1
install -Dm644 man/man1/look.1            %{buildroot}%{_mandir}/man1/9look.1
install -Dm644 man/man1/ls.1              %{buildroot}%{_mandir}/man1/9ls.1
install -Dm644 man/man1/man.1             %{buildroot}%{_mandir}/man1/9man.1
install -Dm644 man/man1/map.1             %{buildroot}%{_mandir}/man1/9map.1
install -Dm644 man/man1/mc.1              %{buildroot}%{_mandir}/man1/9mc.1
install -Dm644 man/man1/mk.1              %{buildroot}%{_mandir}/man1/9mk.1
install -Dm644 man/man1/mk9660.1          %{buildroot}%{_mandir}/man1/9mk9660.1
install -Dm644 man/man1/mkdir.1           %{buildroot}%{_mandir}/man1/9mkdir.1
install -Dm644 man/man1/mount.1           %{buildroot}%{_mandir}/man1/9mount.1
install -Dm644 man/man1/namespace.1       %{buildroot}%{_mandir}/man1/9namespace.1
install -Dm644 man/man1/ndb.1             %{buildroot}%{_mandir}/man1/9ndb.1
install -Dm644 man/man1/netfiles.1        %{buildroot}%{_mandir}/man1/9netfiles.1
install -Dm644 man/man1/news.1            %{buildroot}%{_mandir}/man1/9news.1
install -Dm644 man/man1/p.1               %{buildroot}%{_mandir}/man1/9p.1
install -Dm644 man/man1/page.1            %{buildroot}%{_mandir}/man1/9page.1
install -Dm644 man/man1/paint.1           %{buildroot}%{_mandir}/man1/9paint.1
install -Dm644 man/man1/passwd.1          %{buildroot}%{_mandir}/man1/9passwd.1
install -Dm644 man/man1/pem.1             %{buildroot}%{_mandir}/man1/9pem.1
install -Dm644 man/man1/pic.1             %{buildroot}%{_mandir}/man1/9pic.1
install -Dm644 man/man1/plot.1            %{buildroot}%{_mandir}/man1/9plot.1
install -Dm644 man/man1/plumb.1           %{buildroot}%{_mandir}/man1/9plumb.1
install -Dm644 man/man1/pr.1              %{buildroot}%{_mandir}/man1/9pr.1
install -Dm644 man/man1/proof.1           %{buildroot}%{_mandir}/man1/9proof.1
install -Dm644 man/man1/ps.1              %{buildroot}%{_mandir}/man1/9ps.1
install -Dm644 man/man1/psfonts.1         %{buildroot}%{_mandir}/man1/9psfonts.1
install -Dm644 man/man1/pwd.1             %{buildroot}%{_mandir}/man1/9pwd.1
install -Dm644 man/man1/rc.1              %{buildroot}%{_mandir}/man1/9rc.1
install -Dm644 man/man1/readcons.1        %{buildroot}%{_mandir}/man1/9readcons.1
install -Dm644 man/man1/resample.1        %{buildroot}%{_mandir}/man1/9resample.1
install -Dm644 man/man1/rio.1             %{buildroot}%{_mandir}/man1/9rio.1
install -Dm644 man/man1/rm.1              %{buildroot}%{_mandir}/man1/9rm.1
install -Dm644 man/man1/rsa.1             %{buildroot}%{_mandir}/man1/9rsa.1
install -Dm644 man/man1/sam.1             %{buildroot}%{_mandir}/man1/9sam.1
install -Dm644 man/man1/scat.1            %{buildroot}%{_mandir}/man1/9scat.1
install -Dm644 man/man1/secstore.1        %{buildroot}%{_mandir}/man1/9secstore.1
install -Dm644 man/man1/secstored.1       %{buildroot}%{_mandir}/man1/9secstored.1
install -Dm644 man/man1/sed.1             %{buildroot}%{_mandir}/man1/9sed.1
install -Dm644 man/man1/seq.1             %{buildroot}%{_mandir}/man1/9seq.1
install -Dm644 man/man1/sftpcache.1       %{buildroot}%{_mandir}/man1/9sftpcache.1
install -Dm644 man/man1/sleep.1           %{buildroot}%{_mandir}/man1/9sleep.1
install -Dm644 man/man1/snarfer.1         %{buildroot}%{_mandir}/man1/9snarfer.1
install -Dm644 man/man1/soelim.1          %{buildroot}%{_mandir}/man1/9soelim.1
install -Dm644 man/man1/sort.1            %{buildroot}%{_mandir}/man1/9sort.1
install -Dm644 man/man1/spell.1           %{buildroot}%{_mandir}/man1/9spell.1
install -Dm644 man/man1/split.1           %{buildroot}%{_mandir}/man1/9split.1
install -Dm644 man/man1/src.1             %{buildroot}%{_mandir}/man1/9src.1
install -Dm644 man/man1/ssam.1            %{buildroot}%{_mandir}/man1/9ssam.1
install -Dm644 man/man1/ssh-agent.1       %{buildroot}%{_mandir}/man1/9ssh-agent.1
install -Dm644 man/man1/stats.1           %{buildroot}%{_mandir}/man1/9stats.1
install -Dm644 man/man1/strings.1         %{buildroot}%{_mandir}/man1/9strings.1
install -Dm644 man/man1/sum.1             %{buildroot}%{_mandir}/man1/9sum.1
install -Dm644 man/man1/tail.1            %{buildroot}%{_mandir}/man1/9tail.1
install -Dm644 man/man1/tar.1             %{buildroot}%{_mandir}/man1/9tar.1
install -Dm644 man/man1/tbl.1             %{buildroot}%{_mandir}/man1/9tbl.1
install -Dm644 man/man1/tcs.1             %{buildroot}%{_mandir}/man1/9tcs.1
install -Dm644 man/man1/tee.1             %{buildroot}%{_mandir}/man1/9tee.1
install -Dm644 man/man1/test.1            %{buildroot}%{_mandir}/man1/9test.1
install -Dm644 man/man1/time.1            %{buildroot}%{_mandir}/man1/9time.1
install -Dm644 man/man1/touch.1           %{buildroot}%{_mandir}/man1/9touch.1
install -Dm644 man/man1/tr.1              %{buildroot}%{_mandir}/man1/9tr.1
install -Dm644 man/man1/tr2post.1         %{buildroot}%{_mandir}/man1/9tr2post.1
install -Dm644 man/man1/troff.1           %{buildroot}%{_mandir}/man1/9troff.1
install -Dm644 man/man1/troff2html.1      %{buildroot}%{_mandir}/man1/9troff2html.1
install -Dm644 man/man1/tweak.1           %{buildroot}%{_mandir}/man1/9tweak.1
install -Dm644 man/man1/uniq.1            %{buildroot}%{_mandir}/man1/9uniq.1
install -Dm644 man/man1/units.1           %{buildroot}%{_mandir}/man1/9units.1
install -Dm644 man/man1/vac.1             %{buildroot}%{_mandir}/man1/9vac.1
install -Dm644 man/man1/venti.1           %{buildroot}%{_mandir}/man1/9venti.1
install -Dm644 man/man1/wc.1              %{buildroot}%{_mandir}/man1/9wc.1
install -Dm644 man/man1/web.1             %{buildroot}%{_mandir}/man1/9web.1
install -Dm644 man/man1/wintext.1         %{buildroot}%{_mandir}/man1/9wintext.1
install -Dm644 man/man1/winwatch.1        %{buildroot}%{_mandir}/man1/9winwatch.1
install -Dm644 man/man1/xd.1              %{buildroot}%{_mandir}/man1/9xd.1
install -Dm644 man/man1/yacc.1            %{buildroot}%{_mandir}/man1/9yacc.1
install -Dm644 man/man1/yesterday.1       %{buildroot}%{_mandir}/man1/9yesterday.1
install -Dm644 man/man3/0intro.3          %{buildroot}%{_mandir}/man3/0intro.3
install -Dm644 man/man3/9p-cmdbuf.3       %{buildroot}%{_mandir}/man3/9p-cmdbuf.3
install -Dm644 man/man3/9p-fid.3          %{buildroot}%{_mandir}/man3/9p-fid.3
install -Dm644 man/man3/9p-file.3         %{buildroot}%{_mandir}/man3/9p-file.3
install -Dm644 man/man3/9p-intmap.3       %{buildroot}%{_mandir}/man3/9p-intmap.3
install -Dm644 man/man3/9p.3              %{buildroot}%{_mandir}/man3/9p.3
install -Dm644 man/man3/9pclient.3        %{buildroot}%{_mandir}/man3/9pclient.3
install -Dm644 man/man3/acme.3            %{buildroot}%{_mandir}/man3/acme.3
install -Dm644 man/man3/addpt.3           %{buildroot}%{_mandir}/man3/addpt.3
install -Dm644 man/man3/aes.3             %{buildroot}%{_mandir}/man3/9aes.3
install -Dm644 man/man3/allocimage.3      %{buildroot}%{_mandir}/man3/9allocimage.3
install -Dm644 man/man3/arg.3             %{buildroot}%{_mandir}/man3/9arg.3
install -Dm644 man/man3/arith3.3          %{buildroot}%{_mandir}/man3/9arith3.3
install -Dm644 man/man3/atof.3            %{buildroot}%{_mandir}/man3/9atof.3
install -Dm644 man/man3/auth.3            %{buildroot}%{_mandir}/man3/9auth.3
install -Dm644 man/man3/authsrv.3         %{buildroot}%{_mandir}/man3/9authsrv.3
install -Dm644 man/man3/avl.3             %{buildroot}%{_mandir}/man3/9avl.3
install -Dm644 man/man3/bin.3             %{buildroot}%{_mandir}/man3/9bin.3
install -Dm644 man/man3/bio.3             %{buildroot}%{_mandir}/man3/9bio.3
install -Dm644 man/man3/blowfish.3        %{buildroot}%{_mandir}/man3/9blowfish.3
install -Dm644 man/man3/cachechars.3      %{buildroot}%{_mandir}/man3/9cachechars.3
install -Dm644 man/man3/cleanname.3       %{buildroot}%{_mandir}/man3/9cleanname.3
install -Dm644 man/man3/color.3           %{buildroot}%{_mandir}/man3/9color.3
install -Dm644 man/man3/complete.3        %{buildroot}%{_mandir}/man3/9complete.3
install -Dm644 man/man3/cputime.3         %{buildroot}%{_mandir}/man3/9cputime.3
install -Dm644 man/man3/ctime.3           %{buildroot}%{_mandir}/man3/9ctime.3
install -Dm644 man/man3/des.3             %{buildroot}%{_mandir}/man3/9des.3
install -Dm644 man/man3/dial.3            %{buildroot}%{_mandir}/man3/9dial.3
install -Dm644 man/man3/dirread.3         %{buildroot}%{_mandir}/man3/9dirread.3
install -Dm644 man/man3/draw.3            %{buildroot}%{_mandir}/man3/9draw.3
install -Dm644 man/man3/drawfcall.3       %{buildroot}%{_mandir}/man3/9drawfcall.3
install -Dm644 man/man3/dsa.3             %{buildroot}%{_mandir}/man3/9dsa.3
install -Dm644 man/man3/dup.3             %{buildroot}%{_mandir}/man3/9dup.3
install -Dm644 man/man3/elgamal.3         %{buildroot}%{_mandir}/man3/9elgamal.3
install -Dm644 man/man3/encode.3          %{buildroot}%{_mandir}/man3/9encode.3
install -Dm644 man/man3/encrypt.3         %{buildroot}%{_mandir}/man3/9encrypt.3
install -Dm644 man/man3/errstr.3          %{buildroot}%{_mandir}/man3/9errstr.3
install -Dm644 man/man3/event.3           %{buildroot}%{_mandir}/man3/9event.3
install -Dm644 man/man3/exec.3            %{buildroot}%{_mandir}/man3/9exec.3
install -Dm644 man/man3/exits.3           %{buildroot}%{_mandir}/man3/9exits.3
install -Dm644 man/man3/fcall.3           %{buildroot}%{_mandir}/man3/9fcall.3
install -Dm644 man/man3/flate.3           %{buildroot}%{_mandir}/man3/9flate.3
install -Dm644 man/man3/fmtinstall.3      %{buildroot}%{_mandir}/man3/9fmtinstall.3
install -Dm644 man/man3/frame.3           %{buildroot}%{_mandir}/man3/9frame.3
install -Dm644 man/man3/genrandom.3       %{buildroot}%{_mandir}/man3/9genrandom.3
install -Dm644 man/man3/get9root.3        %{buildroot}%{_mandir}/man3/9get9root.3
install -Dm644 man/man3/getcallerpc.3     %{buildroot}%{_mandir}/man3/9getcallerpc.3
install -Dm644 man/man3/getenv.3          %{buildroot}%{_mandir}/man3/9getenv.3
install -Dm644 man/man3/getfields.3       %{buildroot}%{_mandir}/man3/9getfields.3
install -Dm644 man/man3/getns.3           %{buildroot}%{_mandir}/man3/9getns.3
install -Dm644 man/man3/getsnarf.3        %{buildroot}%{_mandir}/man3/9getsnarf.3
install -Dm644 man/man3/getuser.3         %{buildroot}%{_mandir}/man3/9getuser.3
install -Dm644 man/man3/getwd.3           %{buildroot}%{_mandir}/man3/9getwd.3
install -Dm644 man/man3/graphics.3        %{buildroot}%{_mandir}/man3/9graphics.3
install -Dm644 man/man3/html.3            %{buildroot}%{_mandir}/man3/9html.3
install -Dm644 man/man3/ioproc.3          %{buildroot}%{_mandir}/man3/9ioproc.3
install -Dm644 man/man3/ip.3              %{buildroot}%{_mandir}/man3/9ip.3
install -Dm644 man/man3/isalpharune.3     %{buildroot}%{_mandir}/man3/9isalpharune.3
install -Dm644 man/man3/keyboard.3        %{buildroot}%{_mandir}/man3/9keyboard.3
install -Dm644 man/man3/lock.3            %{buildroot}%{_mandir}/man3/9lock.3
install -Dm644 man/man3/mach-cmd.3        %{buildroot}%{_mandir}/man3/9mach-cmd.3
install -Dm644 man/man3/mach-file.3       %{buildroot}%{_mandir}/man3/9mach-file.3
install -Dm644 man/man3/mach-map.3        %{buildroot}%{_mandir}/man3/9mach-map.3
install -Dm644 man/man3/mach-stack.3      %{buildroot}%{_mandir}/man3/9mach-stack.3
install -Dm644 man/man3/mach-swap.3       %{buildroot}%{_mandir}/man3/9mach-swap.3
install -Dm644 man/man3/mach-symbol.3     %{buildroot}%{_mandir}/man3/9mach-symbol.3
install -Dm644 man/man3/mach.3            %{buildroot}%{_mandir}/man3/9mach.3
install -Dm644 man/man3/malloc.3          %{buildroot}%{_mandir}/man3/9malloc.3
install -Dm644 man/man3/matrix.3          %{buildroot}%{_mandir}/man3/9matrix.3
install -Dm644 man/man3/memdraw.3         %{buildroot}%{_mandir}/man3/9memdraw.3
install -Dm644 man/man3/memlayer.3        %{buildroot}%{_mandir}/man3/9memlayer.3
install -Dm644 man/man3/memory.3          %{buildroot}%{_mandir}/man3/9memory.3
install -Dm644 man/man3/mouse.3           %{buildroot}%{_mandir}/man3/9mouse.3
install -Dm644 man/man3/mousescrollsize.3 %{buildroot}%{_mandir}/man3/9mousescrollsize.3
install -Dm644 man/man3/mp.3              %{buildroot}%{_mandir}/man3/9mp.3
install -Dm644 man/man3/muldiv.3          %{buildroot}%{_mandir}/man3/9muldiv.3
install -Dm644 man/man3/mux.3             %{buildroot}%{_mandir}/man3/9mux.3
install -Dm644 man/man3/nan.3             %{buildroot}%{_mandir}/man3/9nan.3
install -Dm644 man/man3/ndb.3             %{buildroot}%{_mandir}/man3/9ndb.3
install -Dm644 man/man3/needstack.3       %{buildroot}%{_mandir}/man3/9needstack.3
install -Dm644 man/man3/notify.3          %{buildroot}%{_mandir}/man3/9notify.3
install -Dm644 man/man3/open.3            %{buildroot}%{_mandir}/man3/9open.3
install -Dm644 man/man3/opentemp.3        %{buildroot}%{_mandir}/man3/9opentemp.3
install -Dm644 man/man3/pipe.3            %{buildroot}%{_mandir}/man3/9pipe.3
install -Dm644 man/man3/plumb.3           %{buildroot}%{_mandir}/man3/9plumb.3
install -Dm644 man/man3/post9pservice.3   %{buildroot}%{_mandir}/man3/9post9pservice.3
install -Dm644 man/man3/postnote.3        %{buildroot}%{_mandir}/man3/9postnote.3
install -Dm644 man/man3/prime.3           %{buildroot}%{_mandir}/man3/9prime.3
install -Dm644 man/man3/print.3           %{buildroot}%{_mandir}/man3/9print.3
install -Dm644 man/man3/proto.3           %{buildroot}%{_mandir}/man3/9proto.3
install -Dm644 man/man3/pushtls.3         %{buildroot}%{_mandir}/man3/9pushtls.3
install -Dm644 man/man3/qball.3           %{buildroot}%{_mandir}/man3/9qball.3
install -Dm644 man/man3/quaternion.3      %{buildroot}%{_mandir}/man3/9quaternion.3
install -Dm644 man/man3/quote.3           %{buildroot}%{_mandir}/man3/9quote.3
install -Dm644 man/man3/rand.3            %{buildroot}%{_mandir}/man3/9rand.3
install -Dm644 man/man3/rc4.3             %{buildroot}%{_mandir}/man3/9rc4.3
install -Dm644 man/man3/read.3            %{buildroot}%{_mandir}/man3/9read.3
install -Dm644 man/man3/readcolmap.3      %{buildroot}%{_mandir}/man3/9readcolmap.3
install -Dm644 man/man3/readcons.3        %{buildroot}%{_mandir}/man3/9readcons.3
install -Dm644 man/man3/regexp.3          %{buildroot}%{_mandir}/man3/9regexp.3
install -Dm644 man/man3/rfork.3           %{buildroot}%{_mandir}/man3/9rfork.3
install -Dm644 man/man3/rsa.3             %{buildroot}%{_mandir}/man3/9rsa.3
install -Dm644 man/man3/rune.3            %{buildroot}%{_mandir}/man3/9rune.3
install -Dm644 man/man3/runestrcat.3      %{buildroot}%{_mandir}/man3/9runestrcat.3
install -Dm644 man/man3/searchpath.3      %{buildroot}%{_mandir}/man3/9searchpath.3
install -Dm644 man/man3/sechash.3         %{buildroot}%{_mandir}/man3/9sechash.3
install -Dm644 man/man3/seek.3            %{buildroot}%{_mandir}/man3/9seek.3
install -Dm644 man/man3/sendfd.3          %{buildroot}%{_mandir}/man3/9sendfd.3
install -Dm644 man/man3/setjmp.3          %{buildroot}%{_mandir}/man3/9setjmp.3
install -Dm644 man/man3/sleep.3           %{buildroot}%{_mandir}/man3/9sleep.3
install -Dm644 man/man3/stat.3            %{buildroot}%{_mandir}/man3/9stat.3
install -Dm644 man/man3/strcat.3          %{buildroot}%{_mandir}/man3/9strcat.3
install -Dm644 man/man3/string.3          %{buildroot}%{_mandir}/man3/9string.3
install -Dm644 man/man3/stringsize.3      %{buildroot}%{_mandir}/man3/9stringsize.3
install -Dm644 man/man3/subfont.3         %{buildroot}%{_mandir}/man3/9subfont.3
install -Dm644 man/man3/sysfatal.3        %{buildroot}%{_mandir}/man3/9sysfatal.3
install -Dm644 man/man3/thread.3          %{buildroot}%{_mandir}/man3/9thread.3
install -Dm644 man/man3/time.3            %{buildroot}%{_mandir}/man3/9time.3
install -Dm644 man/man3/udpread.3         %{buildroot}%{_mandir}/man3/9udpread.3
install -Dm644 man/man3/venti-cache.3     %{buildroot}%{_mandir}/man3/9venti-cache.3
install -Dm644 man/man3/venti-client.3    %{buildroot}%{_mandir}/man3/9venti-client.3
install -Dm644 man/man3/venti-conn.3      %{buildroot}%{_mandir}/man3/9venti-conn.3
install -Dm644 man/man3/venti-fcall.3     %{buildroot}%{_mandir}/man3/9venti-fcall.3
install -Dm644 man/man3/venti-file.3      %{buildroot}%{_mandir}/man3/9venti-file.3
install -Dm644 man/man3/venti-log.3       %{buildroot}%{_mandir}/man3/9venti-log.3
install -Dm644 man/man3/venti-mem.3       %{buildroot}%{_mandir}/man3/9venti-mem.3
install -Dm644 man/man3/venti-packet.3    %{buildroot}%{_mandir}/man3/9venti-packet.3
install -Dm644 man/man3/venti-server.3    %{buildroot}%{_mandir}/man3/9venti-server.3
install -Dm644 man/man3/venti-zero.3      %{buildroot}%{_mandir}/man3/9venti-zero.3
install -Dm644 man/man3/venti.3           %{buildroot}%{_mandir}/man3/9venti.3
install -Dm644 man/man3/wait.3            %{buildroot}%{_mandir}/man3/9wait.3
install -Dm644 man/man3/wctl.3            %{buildroot}%{_mandir}/man3/9wctl.3
install -Dm644 man/man3/window.3          %{buildroot}%{_mandir}/man3/9window.3
install -Dm644 man/man4/0intro.4          %{buildroot}%{_mandir}/man4/90intro.4
install -Dm644 man/man4/9import.4         %{buildroot}%{_mandir}/man4/99import.4
install -Dm644 man/man4/9pfuse.4          %{buildroot}%{_mandir}/man4/99pfuse.4
install -Dm644 man/man4/9pserve.4         %{buildroot}%{_mandir}/man4/99pserve.4
install -Dm644 man/man4/acme.4            %{buildroot}%{_mandir}/man4/9acme.4
install -Dm644 man/man4/factotum.4        %{buildroot}%{_mandir}/man4/9factotum.4
install -Dm644 man/man4/fontsrv.4         %{buildroot}%{_mandir}/man4/9fontsrv.4
install -Dm644 man/man4/fossil.4          %{buildroot}%{_mandir}/man4/9fossil.4
install -Dm644 man/man4/import.4          %{buildroot}%{_mandir}/man4/9import.4
install -Dm644 man/man4/mntgen.4          %{buildroot}%{_mandir}/man4/9mntgen.4
install -Dm644 man/man4/plumber.4         %{buildroot}%{_mandir}/man4/9plumber.4
install -Dm644 man/man4/ramfs.4           %{buildroot}%{_mandir}/man4/9ramfs.4
install -Dm644 man/man4/smugfs.4          %{buildroot}%{_mandir}/man4/9smugfs.4
install -Dm644 man/man4/srv.4             %{buildroot}%{_mandir}/man4/9srv.4
install -Dm644 man/man4/tapefs.4          %{buildroot}%{_mandir}/man4/9tapefs.4
install -Dm644 man/man4/vacfs.4           %{buildroot}%{_mandir}/man4/9vacfs.4
install -Dm644 man/man7/0intro.7          %{buildroot}%{_mandir}/man7/90intro.7
install -Dm644 man/man7/color.7           %{buildroot}%{_mandir}/man7/9color.7
install -Dm644 man/man7/face.7            %{buildroot}%{_mandir}/man7/9face.7
install -Dm644 man/man7/font.7            %{buildroot}%{_mandir}/man7/9font.7
install -Dm644 man/man7/htmlroff.7        %{buildroot}%{_mandir}/man7/9htmlroff.7
install -Dm644 man/man7/image.7           %{buildroot}%{_mandir}/man7/9image.7
install -Dm644 man/man7/keyboard.7        %{buildroot}%{_mandir}/man7/9keyboard.7
install -Dm644 man/man7/man.7             %{buildroot}%{_mandir}/man7/9man.7
install -Dm644 man/man7/map.7             %{buildroot}%{_mandir}/man7/9map.7
install -Dm644 man/man7/mhtml.7           %{buildroot}%{_mandir}/man7/9mhtml.7
install -Dm644 man/man7/mpictures.7       %{buildroot}%{_mandir}/man7/9mpictures.7
install -Dm644 man/man7/ms.7              %{buildroot}%{_mandir}/man7/9ms.7
install -Dm644 man/man7/ndb.7             %{buildroot}%{_mandir}/man7/9ndb.7
install -Dm644 man/man7/plot.7            %{buildroot}%{_mandir}/man7/9plot.7
install -Dm644 man/man7/plumb.7           %{buildroot}%{_mandir}/man7/9plumb.7
install -Dm644 man/man7/regexp.7          %{buildroot}%{_mandir}/man7/9regexp.7
install -Dm644 man/man7/thumbprint.7      %{buildroot}%{_mandir}/man7/9thumbprint.7
install -Dm644 man/man7/utf.7             %{buildroot}%{_mandir}/man7/9utf.7
install -Dm644 man/man7/venti.7           %{buildroot}%{_mandir}/man7/9venti.7
install -Dm644 man/man8/fossilcons.8      %{buildroot}%{_mandir}/man8/9fossilcons.8
install -Dm644 man/man8/getflags.8        %{buildroot}%{_mandir}/man8/9getflags.8
install -Dm644 man/man8/listen1.8         %{buildroot}%{_mandir}/man8/9listen1.8
install -Dm644 man/man8/mkfs.8            %{buildroot}%{_mandir}/man8/9mkfs.8
install -Dm644 man/man8/vbackup.8         %{buildroot}%{_mandir}/man8/9vbackup.8
install -Dm644 man/man8/venti-backup.8    %{buildroot}%{_mandir}/man8/9venti-backup.8
install -Dm644 man/man8/venti-fmt.8       %{buildroot}%{_mandir}/man8/9venti-fmt.8
install -Dm644 man/man8/venti.8           %{buildroot}%{_mandir}/man8/9venti.8

install -Dm644 include/*.h               -t %{buildroot}%{_includedir}/
install -Dm644 lib/*.a                   -t %{buildroot}%{_libdir}/

%desktop_file_install %{S:1}
%desktop_file_install %{S:2}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/acme.desktop
%desktop_file_validate %{buildroot}%{_appsdir}/sam.desktop

%files
%doc README.md CONTRIBUTING.md CONTRIBUTORS
%license LICENSE src/cmd/bzip2/LICENSE
%{_appsdir}/acme.desktop
%{_appsdir}/sam.desktop
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
%{_bindir}/9stack
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
%{_bindir}/venti/venti-9read
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
%{_bindir}/9fortune
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
%{_bindir}/9read
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
%{_mandir}/man1/9acid.1.*
%{_mandir}/man1/acme.1.*
%{_mandir}/man1/acmeevent.1.*
%{_mandir}/man1/9ascii.1.*
%{_mandir}/man1/9astro.1.*
%{_mandir}/man1/9awk.1.*
%{_mandir}/man1/9basename.1.*
%{_mandir}/man1/9bc.1.*
%{_mandir}/man1/9bundle.1.*
%{_mandir}/man1/9cal.1.*
%{_mandir}/man1/9calendar.1.*
%{_mandir}/man1/9cat.1.*
%{_mandir}/man1/9cleanname.1.*
%{_mandir}/man1/9clog.1.*
%{_mandir}/man1/9cmp.1.*
%{_mandir}/man1/9col.1.*
%{_mandir}/man1/9colors.1.*
%{_mandir}/man1/9comm.1.*
%{_mandir}/man1/9compress.1.*
%{_mandir}/man1/9core.1.*
%{_mandir}/man1/9crop.1.*
%{_mandir}/man1/9date.1.*
%{_mandir}/man1/9db.1.*
%{_mandir}/man1/9dc.1.*
%{_mandir}/man1/9dd.1.*
%{_mandir}/man1/9deroff.1.*
%{_mandir}/man1/9devdraw.1.*
%{_mandir}/man1/9dial.1.*
%{_mandir}/man1/9dict.1.*
%{_mandir}/man1/9diff.1.*
%{_mandir}/man1/9doctype.1.*
%{_mandir}/man1/9echo.1.*
%{_mandir}/man1/9ed.1.*
%{_mandir}/man1/9eqn.1.*
%{_mandir}/man1/9factor.1.*
%{_mandir}/man1/9fmt.1.*
%{_mandir}/man1/9fortune.1.*
%{_mandir}/man1/9freq.1.*
%{_mandir}/man1/9fsize.1.*
%{_mandir}/man1/9git.1.*
%{_mandir}/man1/9grap.1.*
%{_mandir}/man1/9graph.1.*
%{_mandir}/man1/9grep.1.*
%{_mandir}/man1/9gview.1.*
%{_mandir}/man1/9gzip.1.*
%{_mandir}/man1/9hget.1.*
%{_mandir}/man1/9hist.1.*
%{_mandir}/man1/9hoc.1.*
%{_mandir}/man1/9htmlroff.1.*
%{_mandir}/man1/9idiff.1.*
%{_mandir}/man1/9install.1.*
%{_mandir}/man1/9join.1.*
%{_mandir}/man1/9jpg.1.*
%{_mandir}/man1/9kill.1.*
%{_mandir}/man1/9label.1.*
%{_mandir}/man1/9lex.1.*
%{_mandir}/man1/9look.1.*
%{_mandir}/man1/9ls.1.*
%{_mandir}/man1/9man.1.*
%{_mandir}/man1/9map.1.*
%{_mandir}/man1/9mc.1.*
%{_mandir}/man1/9mk.1.*
%{_mandir}/man1/9mk9660.1.*
%{_mandir}/man1/9mkdir.1.*
%{_mandir}/man1/9mount.1.*
%{_mandir}/man1/9namespace.1.*
%{_mandir}/man1/9ndb.1.*
%{_mandir}/man1/9netfiles.1.*
%{_mandir}/man1/9news.1.*
%{_mandir}/man1/9p.1.*
%{_mandir}/man1/9page.1.*
%{_mandir}/man1/9paint.1.*
%{_mandir}/man1/9passwd.1.*
%{_mandir}/man1/9pem.1.*
%{_mandir}/man1/9pic.1.*
%{_mandir}/man1/9plot.1.*
%{_mandir}/man1/9plumb.1.*
%{_mandir}/man1/9pr.1.*
%{_mandir}/man1/9proof.1.*
%{_mandir}/man1/9ps.1.*
%{_mandir}/man1/9psfonts.1.*
%{_mandir}/man1/9pwd.1.*
%{_mandir}/man1/9rc.1.*
%{_mandir}/man1/9readcons.1.*
%{_mandir}/man1/9resample.1.*
%{_mandir}/man1/9rio.1.*
%{_mandir}/man1/9rm.1.*
%{_mandir}/man1/9rsa.1.*
%{_mandir}/man1/9sam.1.*
%{_mandir}/man1/9scat.1.*
%{_mandir}/man1/9secstore.1.*
%{_mandir}/man1/9secstored.1.*
%{_mandir}/man1/9sed.1.*
%{_mandir}/man1/9seq.1.*
%{_mandir}/man1/9sftpcache.1.*
%{_mandir}/man1/9sleep.1.*
%{_mandir}/man1/9snarfer.1.*
%{_mandir}/man1/9soelim.1.*
%{_mandir}/man1/9sort.1.*
%{_mandir}/man1/9spell.1.*
%{_mandir}/man1/9split.1.*
%{_mandir}/man1/9src.1.*
%{_mandir}/man1/9ssam.1.*
%{_mandir}/man1/9ssh-agent.1.*
%{_mandir}/man1/9stats.1.*
%{_mandir}/man1/9strings.1.*
%{_mandir}/man1/9sum.1.*
%{_mandir}/man1/9tail.1.*
%{_mandir}/man1/9tar.1.*
%{_mandir}/man1/9tbl.1.*
%{_mandir}/man1/9tcs.1.*
%{_mandir}/man1/9tee.1.*
%{_mandir}/man1/9test.1.*
%{_mandir}/man1/9time.1.*
%{_mandir}/man1/9touch.1.*
%{_mandir}/man1/9tr.1.*
%{_mandir}/man1/9tr2post.1.*
%{_mandir}/man1/9troff.1.*
%{_mandir}/man1/9troff2html.1.*
%{_mandir}/man1/9tweak.1.*
%{_mandir}/man1/9uniq.1.*
%{_mandir}/man1/9units.1.*
%{_mandir}/man1/9vac.1.*
%{_mandir}/man1/9venti.1.*
%{_mandir}/man1/9wc.1.*
%{_mandir}/man1/9web.1.*
%{_mandir}/man1/9wintext.1.*
%{_mandir}/man1/9winwatch.1.*
%{_mandir}/man1/9xd.1.*
%{_mandir}/man1/9yacc.1.*
%{_mandir}/man1/9yesterday.1.*
%{_mandir}/man3/0intro.3.*
%{_mandir}/man3/9p-cmdbuf.3.*
%{_mandir}/man3/9p-fid.3.*
%{_mandir}/man3/9p-file.3.*
%{_mandir}/man3/9p-intmap.3.*
%{_mandir}/man3/9p.3.*
%{_mandir}/man3/9pclient.3.*
%{_mandir}/man3/acme.3.*
%{_mandir}/man3/addpt.3.*
%{_mandir}/man3/9aes.3.*
%{_mandir}/man3/9allocimage.3.*
%{_mandir}/man3/9arg.3.*
%{_mandir}/man3/9arith3.3.*
%{_mandir}/man3/9atof.3.*
%{_mandir}/man3/9auth.3.*
%{_mandir}/man3/9authsrv.3.*
%{_mandir}/man3/9avl.3.*
%{_mandir}/man3/9bin.3.*
%{_mandir}/man3/9bio.3.*
%{_mandir}/man3/9blowfish.3.*
%{_mandir}/man3/9cachechars.3.*
%{_mandir}/man3/9cleanname.3.*
%{_mandir}/man3/9color.3.*
%{_mandir}/man3/9complete.3.*
%{_mandir}/man3/9cputime.3.*
%{_mandir}/man3/9ctime.3.*
%{_mandir}/man3/9des.3.*
%{_mandir}/man3/9dial.3.*
%{_mandir}/man3/9dirread.3.*
%{_mandir}/man3/9draw.3.*
%{_mandir}/man3/9drawfcall.3.*
%{_mandir}/man3/9dsa.3.*
%{_mandir}/man3/9dup.3.*
%{_mandir}/man3/9elgamal.3.*
%{_mandir}/man3/9encode.3.*
%{_mandir}/man3/9encrypt.3.*
%{_mandir}/man3/9errstr.3.*
%{_mandir}/man3/9event.3.*
%{_mandir}/man3/9exec.3.*
%{_mandir}/man3/9exits.3.*
%{_mandir}/man3/9fcall.3.*
%{_mandir}/man3/9flate.3.*
%{_mandir}/man3/9fmtinstall.3.*
%{_mandir}/man3/9frame.3.*
%{_mandir}/man3/9genrandom.3.*
%{_mandir}/man3/9get9root.3.*
%{_mandir}/man3/9getcallerpc.3.*
%{_mandir}/man3/9getenv.3.*
%{_mandir}/man3/9getfields.3.*
%{_mandir}/man3/9getns.3.*
%{_mandir}/man3/9getsnarf.3.*
%{_mandir}/man3/9getuser.3.*
%{_mandir}/man3/9getwd.3.*
%{_mandir}/man3/9graphics.3.*
%{_mandir}/man3/9html.3.*
%{_mandir}/man3/9ioproc.3.*
%{_mandir}/man3/9ip.3.*
%{_mandir}/man3/9isalpharune.3.*
%{_mandir}/man3/9keyboard.3.*
%{_mandir}/man3/9lock.3.*
%{_mandir}/man3/9mach-cmd.3.*
%{_mandir}/man3/9mach-file.3.*
%{_mandir}/man3/9mach-map.3.*
%{_mandir}/man3/9mach-stack.3.*
%{_mandir}/man3/9mach-swap.3.*
%{_mandir}/man3/9mach-symbol.3.*
%{_mandir}/man3/9mach.3.*
%{_mandir}/man3/9malloc.3.*
%{_mandir}/man3/9matrix.3.*
%{_mandir}/man3/9memdraw.3.*
%{_mandir}/man3/9memlayer.3.*
%{_mandir}/man3/9memory.3.*
%{_mandir}/man3/9mouse.3.*
%{_mandir}/man3/9mousescrollsize.3.*
%{_mandir}/man3/9mp.3.*
%{_mandir}/man3/9muldiv.3.*
%{_mandir}/man3/9mux.3.*
%{_mandir}/man3/9nan.3.*
%{_mandir}/man3/9ndb.3.*
%{_mandir}/man3/9needstack.3.*
%{_mandir}/man3/9notify.3.*
%{_mandir}/man3/9open.3.*
%{_mandir}/man3/9opentemp.3.*
%{_mandir}/man3/9pipe.3.*
%{_mandir}/man3/9plumb.3.*
%{_mandir}/man3/9post9pservice.3.*
%{_mandir}/man3/9postnote.3.*
%{_mandir}/man3/9prime.3.*
%{_mandir}/man3/9print.3.*
%{_mandir}/man3/9proto.3.*
%{_mandir}/man3/9pushtls.3.*
%{_mandir}/man3/9qball.3.*
%{_mandir}/man3/9quaternion.3.*
%{_mandir}/man3/9quote.3.*
%{_mandir}/man3/9rand.3.*
%{_mandir}/man3/9rc4.3.*
%{_mandir}/man3/9read.3.*
%{_mandir}/man3/9readcolmap.3.*
%{_mandir}/man3/9readcons.3.*
%{_mandir}/man3/9regexp.3.*
%{_mandir}/man3/9rfork.3.*
%{_mandir}/man3/9rsa.3.*
%{_mandir}/man3/9rune.3.*
%{_mandir}/man3/9runestrcat.3.*
%{_mandir}/man3/9searchpath.3.*
%{_mandir}/man3/9sechash.3.*
%{_mandir}/man3/9seek.3.*
%{_mandir}/man3/9sendfd.3.*
%{_mandir}/man3/9setjmp.3.*
%{_mandir}/man3/9sleep.3.*
%{_mandir}/man3/9stat.3.*
%{_mandir}/man3/9strcat.3.*
%{_mandir}/man3/9string.3.*
%{_mandir}/man3/9stringsize.3.*
%{_mandir}/man3/9subfont.3.*
%{_mandir}/man3/9sysfatal.3.*
%{_mandir}/man3/9thread.3.*
%{_mandir}/man3/9time.3.*
%{_mandir}/man3/9udpread.3.*
%{_mandir}/man3/9venti-cache.3.*
%{_mandir}/man3/9venti-client.3.*
%{_mandir}/man3/9venti-conn.3.*
%{_mandir}/man3/9venti-fcall.3.*
%{_mandir}/man3/9venti-file.3.*
%{_mandir}/man3/9venti-log.3.*
%{_mandir}/man3/9venti-mem.3.*
%{_mandir}/man3/9venti-packet.3.*
%{_mandir}/man3/9venti-server.3.*
%{_mandir}/man3/9venti-zero.3.*
%{_mandir}/man3/9venti.3.*
%{_mandir}/man3/9wait.3.*
%{_mandir}/man3/9wctl.3.*
%{_mandir}/man3/9window.3.*
%{_mandir}/man4/90intro.4.*
%{_mandir}/man4/99import.4.*
%{_mandir}/man4/99pfuse.4.*
%{_mandir}/man4/99pserve.4.*
%{_mandir}/man4/9acme.4.*
%{_mandir}/man4/9factotum.4.*
%{_mandir}/man4/9fontsrv.4.*
%{_mandir}/man4/9fossil.4.*
%{_mandir}/man4/9import.4.*
%{_mandir}/man4/9mntgen.4.*
%{_mandir}/man4/9plumber.4.*
%{_mandir}/man4/9ramfs.4.*
%{_mandir}/man4/9smugfs.4.*
%{_mandir}/man4/9srv.4.*
%{_mandir}/man4/9tapefs.4.*
%{_mandir}/man4/9vacfs.4.*
%{_mandir}/man7/90intro.7.*
%{_mandir}/man7/9color.7.*
%{_mandir}/man7/9face.7.*
%{_mandir}/man7/9font.7.*
%{_mandir}/man7/9htmlroff.7.*
%{_mandir}/man7/9image.7.*
%{_mandir}/man7/9keyboard.7.*
%{_mandir}/man7/9man.7.*
%{_mandir}/man7/9map.7.*
%{_mandir}/man7/9mhtml.7.*
%{_mandir}/man7/9mpictures.7.*
%{_mandir}/man7/9ms.7.*
%{_mandir}/man7/9ndb.7.*
%{_mandir}/man7/9plot.7.*
%{_mandir}/man7/9plumb.7.*
%{_mandir}/man7/9regexp.7.*
%{_mandir}/man7/9thumbprint.7.*
%{_mandir}/man7/9utf.7.*
%{_mandir}/man7/9venti.7.*
%{_mandir}/man8/9fossilcons.8.*
%{_mandir}/man8/9getflags.8.*
%{_mandir}/man8/9listen1.8.*
%{_mandir}/man8/9mkfs.8.*
%{_mandir}/man8/9vbackup.8.*
%{_mandir}/man8/9venti-backup.8.*
%{_mandir}/man8/9venti-fmt.8.*
%{_mandir}/man8/9venti.8.*
%{_libdir}/*

%changelog
* Fri Aug 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Remove conflictions

* Sun Feb 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit

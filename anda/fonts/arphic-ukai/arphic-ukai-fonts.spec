Name:       arphic-ukai-fonts
Version:    0.2.20080216.2
Release:    %autorelease
URL:        https://www.freedesktop.org/wiki/Software/CJKUnifonts
Source0:	https://deb.debian.org/debian/pool/main/f/fonts-arphic-ukai/fonts-arphic-ukai_%{version}.orig.tar.bz2
License:    custom
Summary:    A fat looking, rounded and cute Japanese font
BuildRequires: unzip

%description
%{summary}.


%prep
%setup -n fonts-arphic-ukai-%{version}


%install
install -D -m644 ukai.ttc %{buildroot}/%{_datadir}/fonts/TTF/ukai.ttc


%clean
rm -rf $RPM_BUILD_ROOT


%post
{
	if test -x /sbin/conf.d/SuSEconfig.fonts ; then
		# This is a SUSE system. Use proprietary SuSE tools...
		if test "$YAST_IS_RUNNING" != "instsys" ; then
			if test -x /sbin/SuSEconfig -a -f /sbin/conf.d/SuSEconfig.fonts ; then
				/sbin/SuSEconfig --module fonts
			else
				echo -e "\nERROR: SuSEconfig or requested SuSEconfig module not present!\n" ; exit 1
			fi
		fi

		if test -x /sbin/conf.d/SuSEconfig.pango ; then
			if test "$YAST_IS_RUNNING" != "instsys" ; then 
				if test -x /sbin/SuSEconfig -a -f /sbin/conf.d/SuSEconfig.pango ; then
					/sbin/SuSEconfig --module pango
				else
					echo -e "\nERROR: SuSEconfig or requested SuSEconfig module not present!\n" ; exit 1
				fi
			fi
		fi
	else
		# Use regular open standards methods...
		ttmkfdir -d %{prefix}/%{name} \
			-o %{prefix}/%{name}/fonts.scale
		umask 133
		/usr/X11R6/bin/mkfontdir %{prefix}/%{name}
		/usr/sbin/chkfontpath -q -a %{prefix}/%{name}
		[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache
	fi
} &> /dev/null || :


%preun
{
	if [ "$1" = "0" ]; then
		cd %{prefix}/%{name}
		rm -f fonts.dir fonts.scale fonts.cache*
	fi
} &> /dev/null || :

%postun

{
	if test -x /sbin/conf.d/SuSEconfig.fonts ; then
		# This is a SUSE system. Use proprietary SuSE tools...
		if test "$YAST_IS_RUNNING" != "instsys" ; then
			if test -x /sbin/SuSEconfig -a -f /sbin/conf.d/SuSEconfig.fonts ; then
				/sbin/SuSEconfig --module fonts
			else
				echo -e "\nERROR: SuSEconfig or requested SuSEconfig module not present!\n" ; exit 1
			fi
		fi

		if test -x /sbin/conf.d/SuSEconfig.pango ; then
			if test "$YAST_IS_RUNNING" != "instsys" ; then 
				if test -x /sbin/SuSEconfig -a -f /sbin/conf.d/SuSEconfig.pango ; then
					/sbin/SuSEconfig --module pango
				else
					echo -e "\nERROR: SuSEconfig or requested SuSEconfig module not present!\n" ; exit 1
				fi
			fi
		fi
	else
		# Use regular open standards methods...
		if [ "$1" = "0" ]; then
			/usr/sbin/chkfontpath -q -r %{prefix}/%{name}
		fi
		[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache
	fi
} &> /dev/null || :


%files
%doc README
%license license/english/ARPHICPL.TXT
%defattr(-,root,root,0755)
/%{prefix}/%{name}

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package

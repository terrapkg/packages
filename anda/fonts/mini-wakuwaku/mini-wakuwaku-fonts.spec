Name:       mini-wakuwaku-fonts
Version:    1.0
Release:    %autorelease
URL:        http://mini-design.jp/font/mini-wakuwaku.html
Source0:	http://mini-design.jp/font/img/mini-wakuwaku.zip
License:    custom
Summary:    A fat looking, rounded and cute Japanese font
BuildRequires: unzip
BuildArch: noarch


%description
%{summary}.


%prep
%setup -n mini-wakuwaku


%install
mkdir -p $RPM_BUILD_ROOT/%{prefix}/%{name}/
cp -r *.otf $RPM_BUILD_ROOT/%{prefix}/%{name}/


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
%doc readme.html
%defattr(-,root,root,0755)
/%{prefix}/%{name}

%changelog
* Mon Nov 21 2022 windowsboy111 <windowsboy111@fyralabs.com> - 4.004
- Initial package

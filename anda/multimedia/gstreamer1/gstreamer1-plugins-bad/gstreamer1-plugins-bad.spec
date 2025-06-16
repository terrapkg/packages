%define _legacy_common_support 1
%global __brp_check_rpaths %{nil}
%global         majorminor 1.0

Name:           gstreamer1-plugins-bad
Version:        1.26.2
Release:        2%?dist
Epoch:          2
Summary:        GStreamer streaming media framework "bad" plugins
License:        LGPL-2.0-or-later and LGPL-2.0-only
URL:            http://gstreamer.freedesktop.org/

Source0:        https://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
Source1:        gstreamer-bad.metainfo.xml

# Requires Provides with and without _isa defined due to package dependencies
Obsoletes:      %{name}-free < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-free-extras < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-extras = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-extras%{?_isa} = %{?epoch}:%{version}-%{release}
#Obsoletes:      %{name}-freeworld < %{?epoch}:%{version}-%{release}
Provides:       %{name}-freeworld = %{?epoch}:%{version}-%{release}
Provides:       %{name}-freeworld%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-nonfree < %{?epoch}:%{version}-%{release}
Provides:       %{name}-nonfree = %{?epoch}:%{version}-%{release}
Provides:       %{name}-nonfree%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-nvidia < %{?epoch}:%{version}-%{release}
Provides:       %{name}-nvidia = %{?epoch}:%{version}-%{release}
Provides:       %{name}-nvidia%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-wildmidi < %{?epoch}:%{version}-%{release}
Provides:       %{name}-wildmidi = %{?epoch}:%{version}-%{release}
Provides:       %{name}-wildmidi%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      gstreamer1-plugin-openh264 < %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-plugin-openh264 = %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-plugin-openh264%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      gstreamer1-svt-hevc < %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-svt-hevc = %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-svt-hevc%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      gstreamer1-plugin-vaapi < %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-plugin-vaapi = %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-plugin-vaapi%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       %{name}-libs = %{?epoch}:%{version}-%{release}

BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.62

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  bzip2-devel
BuildRequires:  check
BuildRequires:  exempi-devel
BuildRequires:  flite-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  gettext-devel >= 0.17
BuildRequires:  glslc
BuildRequires:  gobject-introspection-devel >= 1.31.1
BuildRequires:  gsm-devel
BuildRequires:  ladspa-devel
BuildRequires:  libatomic
BuildRequires:  libcdaudio-devel
BuildRequires:  libmicrodns-devel
#BuildRequires:  libmpcdec-devel - Old API
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  srt-devel
BuildRequires:  vulkan-devel
BuildRequires:  xvidcore-devel


BuildRequires:  pkgconfig(aom) >= 3.0.2
BuildRequires:  pkgconfig(avtp)
BuildRequires:  pkgconfig(bluez) >= 5.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(clutter-1.0) >= 1.8
BuildRequires:  pkgconfig(clutter-glx-1.0) >= 1.8
BuildRequires:  pkgconfig(clutter-x11-1.0) >= 1.8
#BuildRequires:  pkgconfig(dssim)
BuildRequires:  pkgconfig(dvdnav) >= 4.1.2
BuildRequires:  pkgconfig(dvdread) >= 4.1.2
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(fluidsynth) >= 2.1
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) > 2.24
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
#BuildRequires:  pkgconfig(google_cloud_cpp_storage) >= 1.25.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-allocators-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-check-1.0)
BuildRequires:  pkgconfig(gstreamer-controller-1.0)
BuildRequires:  pkgconfig(gstreamer-fft-1.0)
BuildRequires:  pkgconfig(gstreamer-gl-1.0)
BuildRequires:  pkgconfig(gstreamer-gl-egl-1.0)
BuildRequires:  pkgconfig(gstreamer-gl-prototypes-1.0)
#BuildRequires:  pkgconfig(gstreamer-gl-viv-fb-1.0)
BuildRequires:  pkgconfig(gstreamer-gl-wayland-1.0)
BuildRequires:  pkgconfig(gstreamer-gl-x11-1.0)
BuildRequires:  pkgconfig(gstreamer-net-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-riff-1.0)
BuildRequires:  pkgconfig(gstreamer-rtp-1.0)
BuildRequires:  pkgconfig(gstreamer-rtsp-1.0)
BuildRequires:  pkgconfig(gstreamer-sdp-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lc3)
BuildRequires:  pkgconfig(lcms2) >= 2.7
BuildRequires:  pkgconfig(ldacBT-enc)
BuildRequires:  pkgconfig(libass) >= 0.10.2
BuildRequires:  pkgconfig(libbs2b) >= 3.1.0
BuildRequires:  pkgconfig(lcevc_dec)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl) >= 7.55.0
BuildRequires:  pkgconfig(libdca)
BuildRequires:  pkgconfig(libdc1394-2) >= 2.2.5
BuildRequires:  pkgconfig(libde265) >= 0.9
BuildRequires:  pkgconfig(libdrm) >= 2.4.108
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libfreeaptx) >= 0.1.1
BuildRequires:  pkgconfig(libmodplug)
#BuildRequires:  pkgconfig(libonnxruntime) >= 1.16.1
BuildRequires:  pkgconfig(libopenjp2) >= 2.2
BuildRequires:  pkgconfig(libopenmpt)
#BuildRequires:  pkgconfig(libopenni2) >= 0.26
BuildRequires:  pkgconfig(libpng) >= 1.0
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(libSoundTouch)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsrtp2) >= 2.1.0
BuildRequires:  pkgconfig(libssh2) >= 1.4.3
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva) >= 1.18
BuildRequires:  pkgconfig(libva-drm) >= 1.18
BuildRequires:  pkgconfig(libva-x11) >= 1.18
BuildRequires:  pkgconfig(libvisual-0.4) >= 0.4.0
BuildRequires:  pkgconfig(libwebp) >= 0.2.1
BuildRequires:  pkgconfig(libwebpmux) >= 0.2.1
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.2
BuildRequires:  pkgconfig(lilv-0) >= 0.22
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(ltc) >= 1.1.4
BuildRequires:  pkgconfig(mjpegtools) >= 2.0.0
BuildRequires:  pkgconfig(nice) >= 0.1.20
BuildRequires:  pkgconfig(neon) >= 0.27
BuildRequires:  pkgconfig(nettle) >= 3.0
BuildRequires:  pkgconfig(nice) >= 0.1.14
BuildRequires:  pkgconfig(openal) >= 1.14
BuildRequires:  pkgconfig(opencv4) >= 4.0.0
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(openh264) >= 1.3.0
BuildRequires:  pkgconfig(openssl) >= 1.0.1
BuildRequires:  pkgconfig(opus) >= 0.9.4
BuildRequires:  pkgconfig(orc-0.4)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo) >= 1.22.0
BuildRequires:  pkgconfig(sbc) >= 1.0
BuildRequires:  pkgconfig(schroedinger-1.0) >= 1.0.10
BuildRequires:  pkgconfig(sndfile) >= 1.0.16
#BuildRequires:  pkgconfig(soundtouch-1.4)
BuildRequires:  pkgconfig(spandsp) >= 0.0.6
BuildRequires:  pkgconfig(srt) >= 1.3.0
BuildRequires:  pkgconfig(SvtAv1Enc) >= 1.1
#BuildRequires:  pkgconfig(SvtJpegxs) >= 0.9
BuildRequires:  pkgconfig(tiger) >= 0.3.2
BuildRequires:  pkgconfig(vo-aacenc)
BuildRequires:  pkgconfig(vo-amrwbenc) >= 0.1.0
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(wayland-cursor) >= 1.15
BuildRequires:  pkgconfig(wayland-egl) >= 1.15
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
BuildRequires:  pkgconfig(wayland-server) >= 1.15
#BuildRequires:  pkgconfig(webrtc-audio-coding-1)
BuildRequires:  pkgconfig(webrtc-audio-processing-1) >= 1.0
#BuildRequires:  pkgconfig(webrtc-audio-processing-2) >= 2.0
#BuildRequires:  pkgconfig(webview2)
BuildRequires:  pkgconfig(wildmidi) >= 0.4.2
#BuildRequires:  pkgconfig(wpe-webkit-1.1) >= 2.28
#BuildRequires:  pkgconfig(wpebackend-fdo-1.0) >= 1.8
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x265)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xkbcommon) >= 0.8
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(zbar) >= 0.23.1
BuildRequires:  pkgconfig(zvbi-0.2)
BuildRequires:  pkgconfig(zxing) >= 1.4.0

%ifarch x86_64
BuildRequires:  pkgconfig(libmfx) >= 1.0
BuildRequires:  pkgconfig(libmfx) <= 1.99
BuildRequires:  pkgconfig(vpl) >= 2.2
%endif

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested well enough, or the code is
not of good enough quality.

%package        fluidsynth
Summary:        GStreamer "bad" fluidsynth plugin
Requires:       %{name}%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       soundfont2-default
Obsoletes:      %{name}-free-fluidsynth < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-fluidsynth = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-fluidsynth%{?_isa} = %{?epoch}:%{version}-%{release}

%description    fluidsynth
This package contains the GStreamer Fluidsynth plugin.


%package        libs
Summary:        Runtime libraries for the GStreamer "bad" plugins
Obsoletes:      %{name}-free-libs < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-libs = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-libs%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       %{name} = %{?epoch}:%{version}-%{release}

%description    libs
%summary.

%package        devel
Summary:        Development files for the GStreamer "bad" plugins
Requires:       %{name}%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       gstreamer1-plugins-base-devel
Obsoletes:      %{name}-free-devel < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-devel = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-devel%{?_isa} = %{?epoch}:%{version}-%{release}

%description    devel
%summary. 

%prep
%autosetup -p1 -n gst-plugins-bad-%{version}

%build
%meson \
  -D accurip=enabled \
  -D adpcmdec=enabled \
  -D adpcmenc=enabled \
  -D aes=enabled \
  -D aiff=enabled \
  -D aja=disabled \
  -D amfcodec=disabled \
  -D analyticsoverlay=enabled \
  -D androidmedia=disabled \
  -D aom=enabled \
  -D applemedia=enabled \
  -D asfmux=enabled \
  -D asio=enabled \
  -D assrender=enabled \
  -D audiobuffersplit=enabled \
  -D audiofxbad=enabled \
  -D audiolatency=enabled \
  -D audiomixmatrix=enabled \
  -D audiovisualizers=enabled \
  -D autoconvert=enabled \
  -D avtp=enabled \
  -D bayer=enabled \
  -D bluez=enabled \
  -D bs2b=enabled \
  -D bz2=enabled \
  -D camerabin2=enabled \
  -D chromaprint=enabled \
  -D closedcaption=enabled \
  -D codec2json=enabled \
  -D codecalpha=enabled \
  -D codectimestamper=enabled \
  -D coloreffects=enabled \
  -D colormanagement=enabled \
  -D cuda-nvmm=disabled \
  -D curl=enabled \
  -D curl-ssh2=enabled \
  -D d3d11=disabled \
  -D d3d11-hlsl-precompile=disabled \
  -D d3d11-math=disabled \
  -D d3d11-wgc=disabled \
  -D d3d12=disabled \
  -D d3dvideosink=disabled \
  -D dash=enabled \
  -D dc1394=enabled \
  -D debugutils=enabled \
  -D decklink=enabled \
  -D directfb=disabled \
  -D directshow=disabled \
  -D directsound=enabled \
  -D doc=disabled \
  -D drm=enabled \
  -D dtls=enabled \
  -D dts=enabled \
  -D dvb=enabled \
  -D dvbsubenc=enabled \
  -D dvbsuboverlay=enabled \
  -D dvdspu=enabled \
  -D dwrite=enabled \
  -D examples=enabled \
  -D extra-checks=enabled \
  -D faac=disabled \
  -D faad=disabled \
  -D faceoverlay=enabled \
  -D fbdev=enabled \
  -D fdkaac=enabled \
  -D festival=enabled \
  -D fieldanalysis=enabled \
  -D flite=enabled \
  -D fluidsynth=enabled \
  -D freeverb=enabled \
  -D frei0r=enabled \
  -D gaudieffects=enabled \
  -D gdp=enabled \
  -D geometrictransform=enabled \
  -D gl=enabled \
  -D glib-asserts=enabled \
  -D glib-checks=enabled \
  -D gme=enabled \
  -D gobject-cast-checks=enabled \
  -D gpl=enabled \
  -D gs=disabled \
  -D gsm=enabled \
  -D gst_play_tests=false \
  -D gtk3=enabled \
  -D hls=enabled \
  -D hls-crypto=auto \
  -D id3tag=enabled \
  -D insertbin=enabled \
  -D inter=enabled \
  -D interlace=enabled \
  -D introspection=enabled \
  -D ipcpipeline=enabled \
  -D iqa=disabled \
  -D isac=disabled \
  -D ivfparse=enabled \
  -D ivtc=enabled \
  -D jp2kdecimator=enabled \
  -D jpegformat=enabled \
  -D kms=enabled \
  -D ladspa=enabled \
  -D ladspa-rdf=enabled \
  -D lc3=enabled \
  -D lcevcdecoder=enabled \
  -D lcevcencoder=disabled \
  -D ldac=enabled \
  -D libde265=enabled \
  -D librfb=enabled \
  -D lv2=enabled \
  -D magicleap=disabled \
  -D mediafoundation=enabled \
  -D microdns=enabled \
  -D midi=enabled \
  -D modplug=enabled \
  -D mpeg2enc=enabled \
  -D mpegdemux=enabled \
  -D mpegpsmux=enabled \
  -D mpegtsdemux=enabled \
  -D mpegtsmux=enabled \
  -D mplex=enabled \
  -D msdk=enabled \
  -D mse=enabled \
  -D musepack=disabled \
  -D mxf=enabled \
  -D neon=enabled \
  -D netsim=enabled \
  -D nls=enabled \
  -D nvcodec=enabled \
  -D nvcomp=disabled \
  -D nvdswrapper=disabled \
  -D onnx=disabled \
  -D onvif=enabled \
  -D openal=enabled \
  -D openaptx=enabled \
  -D opencv=enabled \
  -D openexr=enabled \
  -D openh264=enabled \
  -D openjpeg=enabled \
  -D openmpt=enabled \
  -D openni2=disabled \
  -D opensles=disabled \
  -D opus=enabled \
  -D orc=enabled \
  -D package-name="Fedora GStreamer-plugins-bad package" \
  -D package-origin="https://terra.fyralabs.com" \
  -D pcapparse=enabled \
  -D pnm=enabled \
  -D proxy=enabled \
  -D qroverlay=enabled \
  -D qt6d3d11=disabled \
  -D rawparse=enabled \
  -D removesilence=enabled \
  -D resindvd=enabled \
  -D rist=enabled \
  -D rsvg=enabled \
  -D rtmp=enabled \
  -D rtmp2=enabled \
  -D rtp=enabled \
  -D sbc=enabled \
  -D sctp=enabled \
  -D sctp-internal-usrsctp=enabled \
  -D sdp=enabled \
  -D segmentclip=enabled \
  -D shm=enabled \
  -D siren=enabled \
  -D smooth=enabled \
  -D smoothstreaming=enabled \
  -D sndfile=enabled \
  -D soundtouch=enabled \
  -D spandsp=enabled \
  -D speed=enabled \
  -D srt=enabled \
  -D srtp=enabled \
  -D subenc=enabled \
  -D svtav1=enabled \
  -D svtjpegxs=disabled \
  -D svthevcenc=disabled \
  -D switchbin=enabled \
  -D teletext=enabled \
  -D tests=disabled \
  -D timecode=enabled \
  -D tinyalsa=disabled \
  -D tools=enabled \
  -D transcode=enabled \
  -D ttml=enabled \
  -D udev=enabled \
  -D unixfd=enabled \
  -D uvcgadget=enabled \
  -D uvch264=enabled \
  -D v4l2codecs=enabled \
  -D va=enabled \
  -D videofilters=enabled \
  -D videoframe_audiolevel=enabled \
  -D videoparsers=enabled \
  -D videosignal=enabled \
  -D vmnc=enabled \
  -D voaacenc=enabled \
  -D voamrwbenc=enabled \
  -D vulkan=enabled \
  -D vulkan-video=enabled \
  -D vulkan-windowing=x11,wayland \
  -D wasapi=disabled \
  -D wasapi2=disabled \
  -D wayland=enabled \
  -D webp=enabled \
  -D webrtc=enabled \
  -D webrtcdsp=enabled \
  -D webview2=enabled \
  -D wic=enabled \
  -D wildmidi=enabled \
  -D win32ipc=disabled \
  -D winks=enabled \
  -D winscreencap=enabled \
  -D wpe=disabled \
  -D x11=enabled \
  -D x265=enabled \
  -D y4m=enabled \
  -D zbar=enabled \
  -D zxing=enabled \
%ifarch x86_64
  -D mfx_api=oneVPL \
  -D mfx-modules-dir=enabled \
  -D msdk=enabled \
  -D qsv=enabled \
%else
  -D msdk=disabled \
  -D qsv=disabled \
%endif

%meson_build

%install
%meson_install
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_metainfodir}/gstreamer-bad.metainfo.xml

%find_lang gst-plugins-bad-%{majorminor}

%files -f gst-plugins-bad-%{majorminor}.lang
%license COPYING
%doc AUTHORS NEWS README.md RELEASE REQUIREMENTS
%{_bindir}/gst-transcoder-1.0
%{_metainfodir}/gstreamer-bad.metainfo.xml
# Encoder profiles
%dir %{_datadir}/gstreamer-%{majorminor}/encoding-profiles/
%dir %{_datadir}/gstreamer-%{majorminor}/encoding-profiles/device/
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/device/dvd.gep
%dir %{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/avi.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/flv.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/mkv.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/mp3.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/mp4.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/oga.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/ogv.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/ts.gep
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/file-extension/webm.gep
%dir %{_datadir}/gstreamer-%{majorminor}/encoding-profiles/online-services/
%{_datadir}/gstreamer-%{majorminor}/encoding-profiles/online-services/youtube.gep
# Presets
%dir %{_datadir}/gstreamer-%{majorminor}/presets
%{_datadir}/gstreamer-%{majorminor}/presets/GstFreeverb.prs
%{_datadir}/gstreamer-%{majorminor}/presets/GstVoAmrwbEnc.prs
# Plugins
%{_libdir}/gstreamer-%{majorminor}/libgstaccurip.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaes.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/gstreamer-%{majorminor}/libgstanalyticsoverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstaom.so
%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstassrender.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiobuffersplit.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiolatency.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixmatrix.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstavtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstbluez.so
%{_libdir}/gstreamer-%{majorminor}/libgstbs2b.so
%{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%{_libdir}/gstreamer-%{majorminor}/libgstclosedcaption.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
%{_libdir}/gstreamer-%{majorminor}/libgstchromaprint.so
%{_libdir}/gstreamer-%{majorminor}/libgstcodecalpha.so
%{_libdir}/gstreamer-%{majorminor}/libgstcodec2json.so
%{_libdir}/gstreamer-%{majorminor}/libgstcodectimestamper.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstcolormanagement.so
%{_libdir}/gstreamer-%{majorminor}/libgstcurl.so
%{_libdir}/gstreamer-%{majorminor}/libgstdash.so
%{_libdir}/gstreamer-%{majorminor}/libgstdc1394.so
%{_libdir}/gstreamer-%{majorminor}/libgstde265.so
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtls.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvbsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaceoverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstfdkaac.so
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{majorminor}/libgstflite.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeverb.so
%{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
%{_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
%{_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{majorminor}/libgstgme.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstgtkwayland.so
%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
%{_libdir}/gstreamer-%{majorminor}/libgstinsertbin.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstinter.so
%{_libdir}/gstreamer-%{majorminor}/libgstivfparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstivtc.so
%{_libdir}/gstreamer-%{majorminor}/libgstjp2kdecimator.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%{_libdir}/gstreamer-%{majorminor}/libgstkms.so
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%{_libdir}/gstreamer-%{majorminor}/libgstlc3.so
%{_libdir}/gstreamer-%{majorminor}/libgstlcevcdecoder.so
%{_libdir}/gstreamer-%{majorminor}/libgstldac.so
%{_libdir}/gstreamer-%{majorminor}/libgstlegacyrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstlv2.so
%{_libdir}/gstreamer-%{majorminor}/libgstmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstmicrodns.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmplex.so
%ifarch x86_64
%{_libdir}/gstreamer-%{majorminor}/libgstmsdk.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstmse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%{_libdir}/gstreamer-%{majorminor}/libgstneonhttpsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstnetsim.so
%{_libdir}/gstreamer-%{majorminor}/libgstnvcodec.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenal.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenaptx.so
%{_libdir}/gstreamer-%{majorminor}/libgstopencv.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenexr.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenh264.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenmpt.so
%{_libdir}/gstreamer-%{majorminor}/libgstopusparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstipcpipeline.so
%{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
%{_libdir}/gstreamer-%{majorminor}/libgstproxy.so
%{_libdir}/gstreamer-%{majorminor}/libgstqroverlay.so
%ifarch x86_64
%{_libdir}/gstreamer-%{majorminor}/libgstqsv.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstremovesilence.so
%{_libdir}/gstreamer-%{majorminor}/libgstresindvd.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstrist.so
%{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtmp.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtmp2.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmanagerbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtponvif.so
%{_libdir}/gstreamer-%{majorminor}/libgstsbc.so
%{_libdir}/gstreamer-%{majorminor}/libgstsctp.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
%{_libdir}/gstreamer-%{majorminor}/libgstsiren.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmooth.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
%{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%{_libdir}/gstreamer-%{majorminor}/libgstsoundtouch.so
%{_libdir}/gstreamer-%{majorminor}/libgstspandsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgstsrt.so
%{_libdir}/gstreamer-%{majorminor}/libgstsrtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstsvtav1.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstswitchbin.so
%{_libdir}/gstreamer-%{majorminor}/libgstteletext.so
%{_libdir}/gstreamer-%{majorminor}/libgsttensordecoders.so
%{_libdir}/gstreamer-%{majorminor}/libgsttimecode.so
%{_libdir}/gstreamer-%{majorminor}/libgsttranscode.so
%{_libdir}/gstreamer-%{majorminor}/libgstttmlsubs.so
%{_libdir}/gstreamer-%{majorminor}/libgstunixfd.so
%{_libdir}/gstreamer-%{majorminor}/libgstuvch264.so
%{_libdir}/gstreamer-%{majorminor}/libgstuvcgadget.so
%{_libdir}/gstreamer-%{majorminor}/libgstv4l2codecs.so
%{_libdir}/gstreamer-%{majorminor}/libgstva.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoframe_audiolevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvoaacenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvoamrwbenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvulkan.so
%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebp.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebrtc.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebrtcdsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstwildmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstx265.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4mdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstzbar.so
%{_libdir}/gstreamer-%{majorminor}/libgstzxing.so

%files fluidsynth
%{_libdir}/gstreamer-%{majorminor}/libgstfluidsynthmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstwildmidi.so

%files libs
%{_libdir}/girepository-%{majorminor}/CudaGst-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/Gst*-%{majorminor}.typelib
%{_libdir}/libgstadaptivedemux-%{majorminor}.so.*
%{_libdir}/libgstanalytics-%{majorminor}.so.*
%{_libdir}/libgstbadaudio-%{majorminor}.so.*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.*
%{_libdir}/libgstcodecparsers-%{majorminor}.so.*
%{_libdir}/libgstcodecs-%{majorminor}.so.*
%{_libdir}/libgstcuda-%{majorminor}.so.*
%{_libdir}/libgstdxva-%{majorminor}.so.*
%{_libdir}/libgstinsertbin-%{majorminor}.so.*
%{_libdir}/libgstisoff-%{majorminor}.so.*
%{_libdir}/libgstmpegts-%{majorminor}.so.*
%{_libdir}/libgstmse-%{majorminor}.so.*
%{_libdir}/libgstopencv-%{majorminor}.so.*
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgstplayer-%{majorminor}.so.*
%{_libdir}/libgstplay-%{majorminor}.so.*
%{_libdir}/libgstsctp-%{majorminor}.so.*
%{_libdir}/libgsttranscoder-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%{_libdir}/libgstva-%{majorminor}.so.*
%{_libdir}/libgstvulkan-%{majorminor}.so.*
%{_libdir}/libgstwayland-%{majorminor}.so.*
%{_libdir}/libgstwebrtc-%{majorminor}.so.*
%{_libdir}/libgstwebrtcnice-%{majorminor}.so.*

%files devel
%{_datadir}/gir-%{majorminor}/CudaGst-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstAnalytics-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstBadAudio-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstCodecs-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstCuda-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstDxva-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstInsertBin-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstMpegts-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstMse-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstPlayer-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstPlay-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstTranscoder-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstVa-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstVulkan-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstVulkanWayland-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstVulkanXCB-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstWebRTC-%{majorminor}.gir
%{_includedir}/gstreamer-%{majorminor}/gst/*
%{_libdir}/libgstadaptivedemux-%{majorminor}.so
%{_libdir}/libgstanalytics-%{majorminor}.so
%{_libdir}/libgstbadaudio-%{majorminor}.so
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so
%{_libdir}/libgstcodecparsers-%{majorminor}.so
%{_libdir}/libgstcodecs-%{majorminor}.so
%{_libdir}/libgstcuda-%{majorminor}.so
%{_libdir}/libgstdxva-%{majorminor}.so
%{_libdir}/libgstinsertbin-%{majorminor}.so
%{_libdir}/libgstisoff-%{majorminor}.so
%{_libdir}/libgstmpegts-%{majorminor}.so
%{_libdir}/libgstmse-%{majorminor}.so
%{_libdir}/libgstopencv-%{majorminor}.so
%{_libdir}/libgstphotography-%{majorminor}.so
%{_libdir}/libgstplay-%{majorminor}.so
%{_libdir}/libgstplayer-%{majorminor}.so
%{_libdir}/libgstsctp-%{majorminor}.so
%{_libdir}/libgsttranscoder-%{majorminor}.so
%{_libdir}/libgsturidownloader-%{majorminor}.so
%{_libdir}/libgstva-%{majorminor}.so
%{_libdir}/libgstvulkan-%{majorminor}.so
%{_libdir}/libgstwayland-%{majorminor}.so
%{_libdir}/libgstwebrtc-%{majorminor}.so
%{_libdir}/libgstwebrtcnice-%{majorminor}.so
%{_libdir}/pkgconfig/gstreamer-analytics-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-bad-audio-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-cuda-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-mse-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-photography-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-play-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-player-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-sctp-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-transcoder-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-va-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-wayland-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-xcb-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-wayland-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-webrtc-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-webrtc-nice-%{majorminor}.pc

%changelog
%autochangelog

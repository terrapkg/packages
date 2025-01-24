%global variants Baijam Chakra Charm Charmonman Fahkwang K2D_July8 KoHo Kodchasal Krub Mali_Grade6 Niramit_AS Srisakdi Sarabun SarabunNew

Name:			sipa-fonts
Version:		20200217
Release:		3%?dist
Summary:		Thai National Fonts collection
URL:			https://www.nstda.or.th/home/news_post/thai-font/
License:		LicenseRef-DIP-SIPA AND OFL-1.1-RFN
Source0:		https://waa.inter.nstda.or.th/stks/pub/%(x=%version;echo ${x:0:4})/%version-13Fonts.zip
Source1:        15-supercede-sarabun.conf
BuildRequires:	unzip
Supplements:    (default-fonts-th)
BuildArch:		noarch
# Sarabun has very tiny latin alphanumeric glyphs, so it's not suitable for general use.
# And this causes legibility issues in many applications that defer to it.
# So let's have Laksaman synthesize it instead.
# TH Sarabun has also been superceded by Google Fonts' Sarabun/TH Sarabun New by the same foundry. (#2482)

Recommends:		%{lua:
local x = ""
local ver = rpm.expand("%version-%release")
for variant in (rpm.expand("%variants")):gmatch("[^ ]+") do
	local v = string.gsub(variant, "_", " ")
	local name = "th-"..string.gsub(v:lower(), " ", "-").."-fonts"
	if name ~= "th-sarabun-fonts" then
		x = x .. name .. " = "..ver.." "
	end
end
print(x)
}

%description
Thai National Fonts collection, freely-licensed computer fonts for the Thai
script sponsored by the Thai government.


%{lua:
local summary = rpm.expand("%summary.\n");
for variant in (rpm.expand("%variants")):gmatch("[^ ]+") do
	local v = string.gsub(variant, "_", " ")
	local name = "th-"..string.gsub(v:lower(), " ", "-").."-fonts"
	print("%package -n "..name.."\n")
	print("Summary: Thai "..v.." fonts (sipa-fonts)\n")
	print("%description -n "..name.."\n")
	print(summary)
end
}

%prep
%autosetup -n Fonts

# copied from https://www.f0nt.com/about/license/
cat <<EOF > LICENSE
สัญญาอนุญาตให้ใช้โปรแกรมคอมพิวเตอร์ฟอนต์

ชื่อที่สงวนไว้สำหรับโปรแกรมคอมพิวเตอร์ฟอนต์นี้
TH Krub, TH Krub Italic, TH Krub Bold, TH Krub Bold Italic,
TH Niramit AS, TH Niramit AS Italic, TH Niramit AS Bold, TH Niramit AS Bold Italic,
TH Kodchasal, TH Kodchasal Italic, TH Kodchasal Bold, TH Kodchasal Bold Italic,
TH Sarabun PSK, TH Sarabun PSK Italic, TH Sarabun PSK Bold, TH Sarabun PSK Bold Italic,
TH K2D July8, TH K2D July8 Italic, TH K2D July8 Bold, TH K2D July8 Bold Italic,
TH Mali Grade 6, TH Mali Grade 6 Italic, TH Mali Grade 6 Bold, TH Mali Grade 6 Bold Italic,
TH Chakra Petch, TH Chakra Petch Italic, TH Chakra Petch Bold, TH Chakra Petch Bold Italic,
TH Baijam, TH Baijam Italic, TH Baijam Bold, TH Baijam Bold Italic,
TH KoHo, TH KoHo Italic, TH KoHo Bold, TH KoHo Bold Italic,
TH Fah Kwang, TH Fah Kwang Italic, TH Fah Kwang Bold, TH Fah Kwang Bold Italic.

โปรแกรมคอมพิวเตอร์ฟอนต์นี้ เป็นลิขสิทธิ์ร่วมกันของกรมทรัพย์สินทางปัญญา กระทรวงพาณิชย์ และสำนักงานส่งเสริมอุตสาหกรรมซอฟต์แวร์แห่งชาติ (องค์การมหาชน)

สัญญาอนุญาตให้ใช้โปรแกรมคอมพิวเตอร์ฟอนต์นี้ มีวัตถุประสงค์เพื่อก่อให้เกิดความร่วมมือในการสร้างสรรค์ฟอนต์ในวงกว้าง รวมทั้งเพื่อประโยชน์ทางด้านการศึกษาและการแบ่งปันความรู้และพัฒนาโปรแกรมคอมพิวเตอร์ฟอนต์นี้

ข้อกำหนดและเงื่อนไขของสัญญาอนุญาตให้ใช้โปรแกรมคอมพิวเตอร์ฟอนต์นี้

(1)  อนุญาตให้ใช้ได้โดยไม่คิดค่าใช้จ่ายและอนุญาตให้ทำซ้ำโปรแกรมคอมพิวเตอร์ฟอนต์นี้ได้ รวมทั้งอนุญาตให้ได้ศึกษา ดัดแปลง และแจกจ่ายให้แก่ผู้อื่นได้ ทั้งนี้จะต้องไม่นำโปรแกรมคอมพิวเตอร์ฟอนต์นี้และโปรแกรมคอมพิวเตอร์ฟอนต์ที่ดัดแปลงออกจำหน่าย เว้นแต่เป็นการจำหน่ายรวมติดไปกับโปรแกรมคอมพิวเตอร์อื่น

(2)  ก่อนดำเนินการดัดแปลงโปรแกรมคอมพิวเตอร์ฟอนต์ จะต้องแจ้งให้เจ้าของลิขสิทธิ์ทราบเป็นลายลักษณ์อักษร

(3)  เมื่อดัดแปลงโปรแกรมคอมพิวเตอร์ฟอนต์นี้แล้ว ห้ามผู้ดัดแปลงใช้ชื่อฟอนต์เดิม รวมทั้งห้ามใช้ชื่อเจ้าของลิขสิทธิ์และผู้สร้างสรรค์โปรแกรมคอมพิวเตอร์ฟอนต์นี้ ในการโฆษณาโปรแกรมคอมพิวเตอร์ฟอนต์ที่ได้ดัดแปลง เว้นแต่ได้รับอนุญาตเป็นลายลักษณ์อักษรจากเจ้าของลิขสิทธิ์

(4)  ผู้ดัดแปลงโปรแกรมคอมพิวเตอร์นี้จะต้องยินยอมให้โปรแกรมคอมพิวเตอร์ฟอนต์ ที่ดัดแปลงขึ้นใหม่มีข้อกำหนดและเงื่อนไขสัญญาอนุญาตให้ใช้โปรแกรมเช่นเดียวกันกับข้อกำหนด และเงื่อนไขของสัญญาอนุญาตนี้เช่นกัน

ข้อถือสิทธิ
เจ้าของลิขสิทธิ์ไม่รับประกันการใช้งานโปรแกรมคอมพิวเตอร์ฟอนต์และไฟล์ที่เกี่ยวข้องนี้แต่อย่างใด  ไม่มีการรับรองว่าโปรแกรมคอมพิวเตอร์ฟอนต์นี้จะทำงานได้อย่างที่ควรจะเป็น และไม่มีการรับรองว่าจะมีการพัฒนาต่อยอดในอนาคต ไม่มีและไม่รับรองว่าจะมีการให้คำแนะนำทางเทคนิคสำหรับโปรแกรมคอมพิวเตอร์ฟอนต์นี้


Font Computer Program License Agreement

Reserved Font Names for this Font Computer Program:
TH Krub, TH Krub Italic, TH Krub Bold, TH Krub Bold Italic,
TH Niramit AS, TH Niramit AS Italic, TH Niramit AS Bold, TH Niramit AS Bold Italic,
TH Kodchasal, TH Kodchasal Italic, TH Kodchasal Bold, TH Kodchasal Bold Italic,
TH Sarabun PSK, TH Sarabun PSK Italic, TH Sarabun PSK Bold, TH Sarabun PSK Bold Italic,
TH K2D July8, TH K2D July8 Italic, TH K2D July8 Bold, TH K2D July8 Bold Italic,
TH Mali Grade 6, TH Mali Grade 6 Italic, TH Mali Grade 6 Bold, TH Mali Grade 6 Bold Italic,
TH Chakra Petch, TH Chakra Petch Italic, TH Chakra Petch Bold, TH Chakra Petch Bold Italic,
TH Baijam, TH Baijam Italic, TH Baijam Bold, TH Baijam Bold Italic,
TH KoHo, TH KoHo Italic, TH KoHo Bold, TH KoHo Bold Italic,
TH Fah Kwang, TH Fah Kwang Italic, TH Fah Kwang Bold, TH Fah Kwang Bold Italic.

This Font Computer Program is the copyright of the Department of Intellectual Property (DIP), Ministry of Commerce and the Software Industry Promotion Agency (Public Organization) (SIPA)

The purposes of this Font Computer Program License are to stimulate worldwide development of cooperative font creation, to benefit for academic, to share and to develop in partnership with others.

Terms and Conditions of the Font Computer Program

(1) Allow to use without any charges and allow to reproduce, study, adapt and distribute this Font Computer Program. Neither the original version nor adapted version of Font Computer Program may be sold by itself, except bundled and/or sold with any computer program.

(2) If you wish to adapt this Font Computer Program, you must notify copyright owners (DIP & SIPA) in writing.

(3) No adapted version of Font Computer Program may use the Reserved Font Name(s), the name(s) of the copyright owners and the author(s) of the Font Computer Program must not be used to promote or advertise any adapted version, except obtaining written permission from copyright owners and the author(s).

(4) The adapted version of Font Computer Program must be released under the term and condition of this license.

DISCLAIMER
THE FONT COMPUTER PROGRAM AND RELATED FILES ARE PROVIDED “AS IS” AND WITHOUT WARRANTY OF ANY KIND.  NO GUARANTEES ARE MADE THAT THIS FONT COMPUTER PROGRAM WILL WORK AS EXPECTED OR WILL BE DEVELOPED FURTHUR IN ANY SPECIFIC WAY.  THERE IS NO OFFER OR GUARANTEE OF TECHNICAL SUPPORT.


EOF

%build

%install
mkdir -p %buildroot/%_datadir/fonts/sipa/
mv *.ttf %buildroot/%_datadir/fonts/sipa/
cd %buildroot/%_datadir/fonts/sipa/
mv "THSarabun Bold Italic.ttf"		"TH Sarabun Bold Italic.ttf"
mv "THSarabun Bold.ttf"				"TH Sarabun Bold.ttf"
mv "THSarabun BoldItalic.ttf"		"TH Sarabun BoldItalic.ttf"
mv "THSarabun Italic.ttf"			"TH Sarabun Italic.ttf"
mv "THSarabun.ttf"					"TH Sarabun.ttf"
mv "THSarabunNew Bold.ttf"			"TH SarabunNew Bold.ttf"
mv "THSarabunNew BoldItalic.ttf"	"TH SarabunNew BoldItalic.ttf"
mv "THSarabunNew Italic.ttf"		"TH SarabunNew Italic.ttf"
mv "THSarabunNew.ttf"				"TH SarabunNew.ttf"

install -Dm644 %{SOURCE1} %buildroot/%{_sysconfdir}/fonts/conf.d/15-supercede-sarabun.conf


%files
%license LICENSE
%dir %{_datadir}/fonts/sipa/


%{lua:
for variant in (rpm.expand("%variants")):gmatch("[^ ]+") do
	local v = string.gsub(variant, "_", " ")
	local name = "th-"..string.gsub(v:lower(), " ", "-").."-fonts"
	print("%files -n "..name.."\n")
	print("%license LICENSE\n")
	print("/usr/share/fonts/sipa/TH?"..v:gsub(" ", "?").."*\n")
	if name == "th-sarabunnew-fonts" then
        print("/etc/fonts/conf.d/15-supercede-sarabun.conf\n")
    end
end
}


%changelog
* Sun Jun 11 2023 windowsboy111 <windowsboy111@fyralabs.com> - 20200217-1
- Initial package

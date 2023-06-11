%global variants Baijam Chakra Charm Charmonman Fahkwang K2D_July8 KoHo Kodchasal Krub Mali_Grade6 Niramit_AS Srisakdi Sarabun SarabunNew

Name:			sipa-fonts
Version:		20200217
Release:		1%?dist
Summary:		Thai National Fonts collection
URL:			https://www.f0nt.com/release/13-free-fonts-from-sipa/
License:		OFL-1.1
Source0:		https://waa.inter.nstda.or.th/stks/pub/%(x=%version;echo ${x:0:4})/%version-13Fonts.zip
BuildRequires:	unzip
BuildArch:		noarch
Recommends:		%{lua:
local x = ""
local ver = rpm.expand("%version-%release")
for variant in (rpm.expand("%variants")):gmatch("[^ ]+") do
	local v = string.gsub(variant, "_", " ")
	local name = "th-"..string.gsub(v:lower(), " ", "-").."-fonts"
	x = x .. name .. " = "..ver.." "
end
print(x)
}

%description
Thai National Fonts collection, freely-licensed computer fonts for the Thai script
sponsored by the Thai government.


%{lua:
for variant in (rpm.expand("%variants")):gmatch("[^ ]+") do
	local v = string.gsub(variant, "_", " ")
	local name = "th-"..string.gsub(v:lower(), " ", "-").."-fonts"
	print("%package -n "..name.."\n")
	print("Summary: Thai "..v.." fonts (sipa-fonts)\n")
	print("%description -n "..name.."\n")
	print("%summary.\n")
end
}

%prep
%autosetup -n Fonts

# copied from https://www.f0nt.com/about/license/
cat <<EOF > LICENSE
1. คุณสามารถดาวน์โหลดฟอนต์ไปใช้งานได้ฟรี ไม่ต้องเสียค่าใช้จ่ายแต่อย่างใด
2. แต่ถ้ามีการระบุข้อตกลงอื่นใดจากเจ้าของฟอนต์ ดังที่แสดงไว้ในหน้าดาวน์โหลดฟอนต์ หรือเป็นไฟล์เอกสารแสดงข้อตกลงที่แนบไปกับฟอนต์นั้นๆ ให้ยึดข้อตกลงดังกล่าวเป็นสำคัญ
3. คุณสามารถคัดลอกรายละเอียดอธิบายข้อมูล, ภาพตัวอย่างฟอนต์ ไปเผยแพร่ แจกจ่ายในเว็บไซต์หรือสื่ออื่นๆ ได้ โดยต้องระบุที่มา และทำลิงก์กลับมายังหน้าแสดงรายละเอียดฟอนต์
4. ไม่อนุญาตให้นำ “ไฟล์ฟอนต์” ไปขาย เว้นแต่จะเป็นการแนบไฟล์ติดไปกับสื่อ โปรแกรม เพื่อความสะดวกในการใช้งาน แต่ไม่ใช่เพื่อการขายฟอนต์เป็นหลัก
5. หากคุณต้องการดัดแปลงฟอนต์เพื่อใช้งานเป็นการส่วนตัว สามารถทำได้ แต่ถ้าทำเพื่อขายหรือรับจ้างผลิต คุณจะต้องได้รับอนุญาตจากเจ้าของฟอนต์ก่อนเท่านั้น
EOF

%build

%install
mkdir -p %buildroot/%_datadir/fonts/sipa/
unzip %SOURCE0 -d %buildroot/%_datadir/fonts/sipa/
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


%files
%license LICENSE

%{lua:
for variant in (rpm.expand("%variants")):gmatch("[^ ]+") do
	local v = string.gsub(variant, "_", " ")
	local name = "th-"..string.gsub(v:lower(), " ", "-").."-fonts"
	print("%files -n "..name.."\n")
	print("%license LICENSE\n")
	print("%_datadir/fonts/sipa/TH "..v.."*\n")
end
}

%changelog
* Sun Jun 11 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package

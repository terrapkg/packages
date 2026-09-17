let v = gh("PowerShell/PowerShell");

if `[\d.]+-preview\.\d+`.find_all(v).len == 0 {
  rpm.version(v);
  rpm.global("dotnet_version", (find(`\"version\": \"([\d.]+)\.\d.+\"`, get(`https://github.com/PowerShell/PowerShell/raw/refs/tags/${v}/global.json`), 1)));
}

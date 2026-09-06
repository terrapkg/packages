rpm.version(gh_rawfile("abenz1267/elephant", "master", "cmd/elephant/version.txt"));
let dir = get("https://api.github.com/repos/abenz1267/elephant/contents/internal/providers/").json_arr();
let providers = "";
for f in dir {
  if f.size == 0 { // dir
    providers += f.name + " ";
  }
}
rpm.global("providers", providers[0..providers.len - 1]);

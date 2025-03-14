rpm.version(crates("pokeget"));
// pokesprites has not received an update in years but let's keep the dep commit current just in case
if rpm.changed () {
     let url = `https://api.github.com/repos/talwat/pokeget-rs/contents/data`;
     let json = get(url).json_arr();
     let c = json[2].sha;
     rpm.global("pcommit", c);
}

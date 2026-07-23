let tagobjs = get("https://api.github.com/repos/ente-io/ente/tags").json_arr();
for tagobj in tagobjs {
  if tagobj.name.starts_with("ensu-v") {
    rpm.global("tag", tagobj.name);
    if rpm.changed() {
      rpm.release();
      break;
    }
  }
}

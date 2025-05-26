if sh("ps | grep anda | wc -l", #{ "stdout": "piped" }).ctx.stdout[0] == "1" {
  print("pre: building for x86_64_v3 first");
  sh("../anda/target/debug/anda build devs/bun -rrpmbuild --rpm-target x86_64_v3", #{});
}

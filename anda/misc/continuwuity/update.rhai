let req = new_req("https://forgejo.ellis.link/api/v1/repos/continuwuation/continuwuity/releases/latest");
let ver = req.get().json().name;
rpm.version(ver);

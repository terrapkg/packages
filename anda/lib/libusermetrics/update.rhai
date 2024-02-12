let o = get("https://gitlab.com/api/v4/projects/25092390/repository/tags").json_arr()[0];
let f = rpm.f;
rpm.version(o.name);

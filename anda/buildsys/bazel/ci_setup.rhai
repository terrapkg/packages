import "andax/ci/extra_repos.rhai" as extra_repos;

print(sh("rpm -q anda", #{
    "stdout": "null",
    "stderr": "null",
}));
extra_repos::install(labels);

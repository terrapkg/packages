import "anda::cfg" as cfg;
print(cfg::load_file(labels.project).project.pkg.labels.to_json());

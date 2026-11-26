// Export the resolved manifest, including nested projects and their build labels.
import "anda::cfg" as cfg;

print(cfg::load_file("anda.hcl").to_json());

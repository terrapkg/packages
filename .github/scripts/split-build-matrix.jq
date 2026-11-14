# Partition selected builds without scanning the repository or starting another job.
def driver:
  (.pkg | startswith("anda/system/nvidia/")) or
  (.pkg | startswith("anda/system/nvidia-580/"));

{
  build_matrix: [.[] | select(driver | not)],
  nvidia_matrix: [.[] | select(driver)]
}
| to_entries[]
| "\(.key)=\(.value | tojson)"

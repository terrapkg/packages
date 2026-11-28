let project = gh_rawfile("leksah/leksah", "master", "cabal.project");
let commit = find(`location: https://github.com/ghcjs/reflex-dom\s+tag: ([0-9a-f]{40})`, project, 1);
rpm.global("commit", commit);
if rpm.changed() {
  rpm.global("ver", find(`(?m)^Version:\s*([\d.]+)`, gh_rawfile("ghcjs/reflex-dom", commit, "reflex-dom-core/reflex-dom-core.cabal"), 1));
  rpm.global("commit_date", date());
  rpm.release();
}

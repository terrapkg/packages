// prepare-sources.sh runs the Fedora kernel SRPM generator before Andaman
// resolves the generated kernel-surface spec's own build requirements.
sh("dnf5 builddep -y kernel", #{});

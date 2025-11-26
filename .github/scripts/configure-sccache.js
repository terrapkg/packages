// Configure sccache environment variables for GitHub Actions cache integration
// Note: ACTIONS_CACHE_SERVICE_V2 and SCCACHE_GHA_ENABLED are set at workflow level
module.exports = async ({ github, context, core, exec }) => {
  // Find sccache path (try which command)
  let sccachePath = "sccache";
  try {
    const result = await exec.getExecOutput("which", ["sccache"], {
      ignoreReturnCode: true,
      silent: true,
    });
    if (result.exitCode === 0 && result.stdout.trim()) {
      sccachePath = result.stdout.trim();
      core.info(`Found sccache at: ${sccachePath}`);
    }
  } catch (e) {
    core.debug(`Could not find sccache path: ${e.message}`);
  }

  // Export SCCACHE_PATH so it's available to subsequent steps
  core.exportVariable("SCCACHE_PATH", sccachePath);

  // Expose the GHA cache related variables to make it easier for users to
  // integrate with GHA support (from upstream mozilla/sccache-action)
  core.exportVariable(
    "ACTIONS_RESULTS_URL",
    process.env.ACTIONS_RESULTS_URL || "",
  );
  core.exportVariable(
    "ACTIONS_RUNTIME_TOKEN",
    process.env.ACTIONS_RUNTIME_TOKEN || "",
  );

  // Set cache version and restore keys for this specific build matrix
  if (process.env.SCCACHE_GHA_VERSION) {
    core.exportVariable("SCCACHE_GHA_VERSION", process.env.SCCACHE_GHA_VERSION);
  }
  if (process.env.SCCACHE_GHA_CACHE_FROM) {
    core.exportVariable(
      "SCCACHE_GHA_CACHE_FROM",
      process.env.SCCACHE_GHA_CACHE_FROM,
    );
  }

  // Check if cache busting is enabled
  const inputs =
    (github &&
      github.context &&
      github.context.payload &&
      github.context.payload.inputs) ||
    {};
  const rawBustCache =
    inputs.bust_cache ??
    inputs.bustCache ??
    process.env.INPUT_BUST_CACHE ??
    process.env.BUST_CACHE;
  let bustCache = false;

  if (typeof rawBustCache === "string") {
    const v = rawBustCache.toLowerCase().trim();
    bustCache = v === "true" || v === "1" || v === "yes";
  } else {
    bustCache = !!rawBustCache;
  }

  if (bustCache) {
    core.exportVariable("SCCACHE_RECACHE", "1");
    core.info("SCCACHE_RECACHE enabled because bust_cache is true");
  }

  // Stop any running sccache daemon so it picks up the new environment variables
  core.info("Stopping any running sccache daemon to pick up configuration...");
  try {
    await exec.exec(sccachePath, ["--stop-server"], {
      ignoreReturnCode: true,
    });
    core.info("sccache daemon stopped successfully");
  } catch (e) {
    core.debug(
      `Could not stop sccache daemon (it may not be running): ${e.message}`,
    );
  }

  // Show the current sccache configuration
  core.info("Current sccache configuration:");
  try {
    await exec.exec(sccachePath, ["--show-stats"], {
      ignoreReturnCode: true,
    });
  } catch (e) {
    core.debug(`Could not show sccache stats: ${e.message}`);
  }
};

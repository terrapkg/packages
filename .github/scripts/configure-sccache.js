// Configure sccache environment variables for GitHub Actions cache integration
// 
// This script is still unused until we build terra-sccache with this supported,
// Turns out that Fedora's sccache build has the GHA feature support disabled.
// 
// Note: ACTIONS_CACHE_SERVICE_V2 and SCCACHE_GHA_ENABLED are set at workflow level
module.exports = async ({ github, context, core, exec }) => {
  // Find sccache path (try which command)
  let sccachePath = "/usr/bin/sccache";
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

  // Check sccache version
  try {
    const versionResult = await exec.getExecOutput(sccachePath, ["--version"], {
      ignoreReturnCode: true,
      silent: true,
    });
    core.info(`sccache version: ${versionResult.stdout.trim()}`);
  } catch (e) {
    core.warning(`Could not get sccache version: ${e.message}`);
  }

  // Enable caching
  core.exportVariable("RUSTC_WRAPPER", sccachePath);
  core.exportVariable("SCCACHE_GHA_ENABLED", "true");

  // Disable Cargo incremental builds to not interfere with caching
  core.exportVariable("CARGO_INCREMENTAL", "false");
  
  // Debug: Show what environment variables are available
  core.info("=== Environment Variables Diagnostic ===");
  core.info(`SCCACHE_GHA_ENABLED: ${process.env.SCCACHE_GHA_ENABLED}`);
  core.info(
    `ACTIONS_CACHE_SERVICE_V2: ${process.env.ACTIONS_CACHE_SERVICE_V2}`,
  );
  core.info(
    `ACTIONS_RESULTS_URL: ${process.env.ACTIONS_RESULTS_URL ? "SET (length: " + process.env.ACTIONS_RESULTS_URL.length + ")" : "NOT SET"}`,
  );
  core.info(
    `ACTIONS_RUNTIME_TOKEN: ${process.env.ACTIONS_RUNTIME_TOKEN ? "SET (length: " + process.env.ACTIONS_RUNTIME_TOKEN.length + ")" : "NOT SET"}`,
  );
  core.info(`RUSTC_WRAPPER: ${process.env.RUSTC_WRAPPER}`);
  core.info(`SCCACHE_LOG: ${process.env.SCCACHE_LOG}`);
  core.info("========================================");

  // Export SCCACHE_PATH so it's available to subsequent steps
  core.exportVariable("SCCACHE_PATH", sccachePath);

  // Expose the GHA cache related variables to make it easier for users to
  // integrate with GHA support (from upstream mozilla/sccache-action)
  if (process.env.ACTIONS_RESULTS_URL) {
    core.exportVariable("ACTIONS_RESULTS_URL", process.env.ACTIONS_RESULTS_URL);
    core.info("✓ Exported ACTIONS_RESULTS_URL");
  } else {
    core.error(
      "ACTIONS_RESULTS_URL is not set - GitHub Actions cache WILL NOT work",
    );
  }

  if (process.env.ACTIONS_RUNTIME_TOKEN) {
    core.exportVariable(
      "ACTIONS_RUNTIME_TOKEN",
      process.env.ACTIONS_RUNTIME_TOKEN,
    );
    core.info("✓ Exported ACTIONS_RUNTIME_TOKEN");
  } else {
    core.error(
      "ACTIONS_RUNTIME_TOKEN is not set - GitHub Actions cache WILL NOT work",
    );
  }

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
    core.exportVariable("SCCACHE_BUST_CACHE", "true");
    core.exportVariable("SCCACHE_RECACHE", "1");
    core.info("SCCACHE_RECACHE enabled because bust_cache is true");
  }

  // Stop any running sccache daemon so it picks up the new environment variables
  core.info("Stopping any running sccache daemon to pick up configuration...");
  try {
    await exec.exec(sccachePath, ["--stop-server"], {
      ignoreReturnCode: true,
    });
    core.info("✓ sccache daemon stopped successfully");
  } catch (e) {
    core.debug(
      `Could not stop sccache daemon (it may not be running): ${e.message}`,
    );
  }

  // Verify sccache can see the GHA environment variables by starting server with explicit env
  core.info("Starting sccache server with GHA environment variables...");
  const sccacheEnv = {
    ...process.env,
    SCCACHE_GHA_ENABLED: process.env.SCCACHE_GHA_ENABLED || "on",
    ACTIONS_CACHE_SERVICE_V2: process.env.ACTIONS_CACHE_SERVICE_V2 || "on",
  };

  try {
    await exec.exec(sccachePath, ["--start-server"], {
      ignoreReturnCode: true,
      env: sccacheEnv,
    });
    core.info("✓ sccache server started");
  } catch (e) {
    core.warning(`Could not start sccache server: ${e.message}`);
  }

  // Show the current sccache configuration
  core.info("Verifying sccache configuration:");
  try {
    const statsResult = await exec.getExecOutput(
      sccachePath,
      ["--show-stats"],
      {
        ignoreReturnCode: true,
        env: sccacheEnv,
      },
    );

    // Check if it's using GitHub Actions cache
    if (statsResult.stdout.includes("GitHub Actions")) {
      core.info("✓ sccache is configured to use GitHub Actions cache");
    } else if (statsResult.stdout.includes("Local disk")) {
      core.error(
        "✗ sccache is using Local disk cache instead of GitHub Actions cache!",
      );
      core.error(
        "This means SCCACHE_GHA_ENABLED or required env vars are not being recognized.",
      );
      core.info("Stats output:");
      core.info(statsResult.stdout);
    }
  } catch (e) {
    core.debug(`Could not show sccache stats: ${e.message}`);
  }
};

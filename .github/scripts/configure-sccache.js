module.exports = ({ github, context, core }) => {
  core.exportVariable(
    "ACTIONS_RESULTS_URL",
    process.env.ACTIONS_RESULTS_URL || "",
  );
  core.exportVariable(
    "ACTIONS_RUNTIME_TOKEN",
    process.env.ACTIONS_RUNTIME_TOKEN || "",
  );
  core.exportVariable("SCCACHE_GHA_VERSION", process.env.SCCACHE_GHA_VERSION);
  core.exportVariable(
    "SCCACHE_GHA_CACHE_FROM",
    process.env.SCCACHE_GHA_CACHE_FROM,
  );
  core.exportVariable("ACTIONS_CACHE_SERVICE_V2", "on");

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
};

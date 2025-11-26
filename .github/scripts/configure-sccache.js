// Configure sccache environment variables for GitHub Actions cache integration
module.exports = ({github, context, core}) => {
  // Force the GitHub Actions cache service v2
  core.exportVariable('ACTIONS_CACHE_SERVICE_V2', 'on');
  core.exportVariable('SCCACHE_GHA_ENABLED', 'true');

  // Expose the GHA cache related variables to make it easier for users to
  // integrate with GHA support (from upstream mozilla/sccache-action)
  core.exportVariable('ACTIONS_RESULTS_URL', process.env.ACTIONS_RESULTS_URL || '');
  core.exportVariable('ACTIONS_RUNTIME_TOKEN', process.env.ACTIONS_RUNTIME_TOKEN || '');

  // Set cache version and restore keys for this specific build matrix
  // core.exportVariable('SCCACHE_GHA_VERSION', process.env.SCCACHE_GHA_VERSION);
  // core.exportVariable('SCCACHE_GHA_CACHE_FROM', process.env.SCCACHE_GHA_CACHE_FROM);

  // Check if cache busting is enabled
  const inputs = (github && github.context && github.context.payload && github.context.payload.inputs) || {};
  const rawBustCache = inputs.bust_cache ?? inputs.bustCache ?? process.env.INPUT_BUST_CACHE ?? process.env.BUST_CACHE;
  let bustCache = false;

  if (typeof rawBustCache === 'string') {
    const v = rawBustCache.toLowerCase().trim();
    bustCache = v === 'true' || v === '1' || v === 'yes';
  } else {
    bustCache = !!rawBustCache;
  }

  if (bustCache) {
    core.exportVariable('SCCACHE_RECACHE', '1');
    core.info('SCCACHE_RECACHE enabled because bust_cache is true');
  }
};

module.exports = async ({ github, context, core, exec }) => {
  if (!exec) {
    throw new Error("exec parameter is required but was not provided");
  }

  // Use SCCACHE_PATH if set, otherwise default to 'sccache' (will use PATH)
  const sccachePath = process.env.SCCACHE_PATH || "sccache";
  core.debug(`Using sccache path: ${sccachePath}`);

  const percentage = (x, y) => Math.round((x / y) * 100 || 0);
  const plural = (count, base, pluralForm = base + "s") =>
    `${count} ${count === 1 ? base : pluralForm}`;
  const sumStats = (stats) =>
    Object.values(stats.counts).reduce((acc, val) => acc + val, 0);
  const formatDuration = (duration) => {
    const ms = duration.nanos / 1e6;
    return `${duration.secs}s ${ms}ms`;
  };

  const formatJsonStats = (stats) => {
    const cacheErrorCount = sumStats(stats.stats.cache_errors);
    const cacheHitCount = sumStats(stats.stats.cache_hits);
    const cacheMissCount = sumStats(stats.stats.cache_misses);
    const totalHits = cacheHitCount + cacheMissCount + cacheErrorCount;
    const ratio = percentage(cacheHitCount, totalHits);

    const writeDuration = formatDuration(stats.stats.cache_write_duration);
    const readDuration = formatDuration(stats.stats.cache_read_hit_duration);
    const compilerDuration = formatDuration(
      stats.stats.compiler_write_duration,
    );

    const noticeHit = plural(cacheHitCount, "hit");
    const noticeMiss = plural(cacheMissCount, "miss", "misses");
    const noticeError = plural(cacheErrorCount, "error");
    const notice = `${ratio}% - ${noticeHit}, ${noticeMiss}, ${noticeError}`;

    const table = [
      [{ data: "Cache hit %", header: true }, { data: `${ratio}%` }],
      [
        { data: "Cache hits", header: true },
        { data: cacheHitCount.toString() },
      ],
      [
        { data: "Cache misses", header: true },
        { data: cacheMissCount.toString() },
      ],
      [
        { data: "Cache errors", header: true },
        { data: cacheErrorCount.toString() },
      ],
      [
        { data: "Compile requests", header: true },
        { data: stats.stats.compile_requests.toString() },
      ],
      [
        { data: "Requests executed", header: true },
        { data: stats.stats.requests_executed.toString() },
      ],
      [
        { data: "Cache writes", header: true },
        { data: stats.stats.cache_writes.toString() },
      ],
      [
        { data: "Cache write errors", header: true },
        { data: stats.stats.cache_write_errors.toString() },
      ],
      [{ data: "Cache write duration", header: true }, { data: writeDuration }],
      [
        { data: "Cache read hit duration", header: true },
        { data: readDuration },
      ],
      [
        { data: "Compiler write duration", header: true },
        { data: compilerDuration },
      ],
    ];
    return { table, notice };
  };

  const getOutput = async (command, args = []) => {
    core.debug(`get_output: ${command} ${args.join(" ")}`);
    const output = await exec.getExecOutput(command, args, {
      ignoreReturnCode: false,
      silent: false,
    });
    if (!output.stdout.endsWith("\n")) {
      process.stdout.write("\n");
    }
    return output.stdout.toString();
  };

  const humanStats = await core.group("Get human-readable stats", async () => {
    return getOutput(sccachePath, ["--show-stats"]);
  });

  const jsonStats = await core.group("Get JSON stats", async () => {
    return getOutput(sccachePath, ["--show-stats", "--stats-format=json"]);
  });

  const stats = JSON.parse(jsonStats);
  const formattedStats = formatJsonStats(stats);

  core.notice(formattedStats.notice, {
    title: `sccache stats - ${context.job}`,
  });
  core.info("\nFull human-readable stats:");
  core.info(humanStats);

  core.summary.addHeading("sccache stats", 2);
  core.summary.addTable(formattedStats.table);
  core.summary.addDetails(
    "Full human-readable stats",
    "\n\n```\n" + humanStats + "\n```\n\n",
  );
  core.summary.addDetails(
    "Full JSON Stats",
    "\n\n```json\n" + JSON.stringify(stats, null, 2) + "\n```\n\n",
  );
  await core.summary.write();
};

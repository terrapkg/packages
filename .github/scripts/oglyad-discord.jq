# turns oglyad's json report into a short Discord webhook payload: the
# counts and which checks the errors come from, with the details left to the
# attached report. run with --arg url <run url>
.summary as $s
# "98 build-lag, 4 collect", biggest first
| ([.findings[] | select(.severity == "error") | .check]
    | group_by(.)
    | map({check: .[0], n: length})
    | sort_by(-.n)
    | map("\(.n) `\(.check)`")
    | join(", ")) as $errorChecks
| {
    username: "oglyad",
    # nothing in the report should ever ping anyone
    allowed_mentions: {parse: []},
    embeds: [
      {
        color: (if $s.error > 0 then 15548997 elif $s.warn > 0 then 16705372 else 5763719 end),
        # embed titles can't be headings, so the header lives in the
        # description, linked to the run like the title was
        description: (
          "## [" + (if $s.error > 0 then "oglyad: \($s.error) errors" elif $s.warn > 0 then "oglyad: \($s.warn) warnings" else "oglyad: all clear" end) + "](\($url))\n"
          + "\($s.error) errors · \($s.warn) warnings · \($s.info) info"
          + (if $errorChecks == "" then "" else "\nerrors from \($errorChecks)" end)
          + "\ndetails in the attached report"
        ),
        footer: {text: (.releases | map(.label + " " + ((.commit // "working tree")[:10])) | join(" · "))},
        timestamp: .generated
      }
    ]
  }

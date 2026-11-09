# turns oglyad's json report into a Discord webhook payload. 
# counts as fields, the errors listed in the description, and a link to the run.
# run with --arg url <run url>
(.releases | map({key: .release, value: .label}) | from_entries) as $labels
| (.releases | length) as $n
| .summary as $s
| [.findings[] | select(.severity == "error")] as $errs
| 20 as $shown
# "[f44]" only on findings some of the checked releases don't have
| def tag: if (.releases | length) < $n then " [" + (.releases | map($labels[.]) | join(", ")) + "]" else "" end;
  ($errs[:$shown]
    | map("- **\(.package)**\(tag) `\(.check)`: \(.message)")
    | join("\n")) as $list
| ($list
    + (if ($errs | length) > $shown then "\n…and \(($errs | length) - $shown) more in the attached report" else "" end)) as $desc
| {
    username: "oglyad",
    # package names and messages are untrusted text, so nothing pings
    allowed_mentions: {parse: []},
    embeds: [
      {
        title: "oglyad report",
        url: $url,
        color: (if $s.error > 0 then 15548997 elif $s.warn > 0 then 16705372 else 5763719 end),
        # embed descriptions cap at 4096 characters
        description: (if $errs == [] then "no errors 🎉" elif ($desc | length) > 4000 then $desc[:4000] + "…" else $desc end),
        fields: [
          {name: "errors", value: "\($s.error)", inline: true},
          {name: "warnings", value: "\($s.warn)", inline: true},
          {name: "info", value: "\($s.info)", inline: true},
          {name: "ignored", value: "\($s.ignored)", inline: true}
        ],
        footer: {text: (.releases | map(.label + " " + ((.commit // "working tree")[:10])) | join(" · "))},
        timestamp: .generated
      }
    ]
  }

# CrocoDash rules

Advice that CrocoDash prints when a case's grid, compset or forcing dates call for it, such as "force tides here" or "the domain's edge crosses the Gulf Stream". The rules are [queryearth](https://crocodile-cesm.github.io/queryearth/) rule files: GeoJSON, one rule per feature, each scoped by where it applies and by grid resolution, forcing product and compset.

| File | What it holds |
|---|---|
| `rules.geojson` | Manish's rules, in groups that nest: Domain design (grid, open boundaries) and Regions (high latitudes, the Coral Triangle and Indonesian Throughflow, Benguela) |
| `rules_claude.geojson` | Rules Claude added from the expert interviews on its own, in the CLAUDE group, until they are reviewed |
| `build_rules.py` | Where the rules are written; it writes both files |
| `places.py` | The shapes the rules share, such as the Gulf Stream and Lombok Strait |

## See them on a globe

Open either file in [vizqueryearth](https://crocodile-cesm.github.io/vizqueryearth/) with **Open link**, using the file's raw GitHub link, or check an area against them there.

## How CrocoDash reads them

CrocoDash installs this gallery, and `Case` reads every file here together:

```python
import queryearth as qe
from crocogallery import rule_files

rules = qe.Registry.from_file(*rule_files())
```

So the rules a case sees are the ones in the gallery commit CrocoDash's gallery submodule points to.

## Change a rule

Edit `build_rules.py` (or `places.py` for a shape), then rerun it from the gallery root:

```bash
python crocodash/rules/build_rules.py
```

It needs queryearth. A new rule takes the next free code in its group, `registry().next_code("ITF")`; numbers are never reused. To accept one of Claude's rules, move it from `CLAUDE_RULES` to `RULES`, into its topic group with that group's next code.

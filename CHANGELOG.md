# Recipe Site — Changes, Fixes & Known Issues

Running log for this site (published at lmccorvey85.github.io/recipes/) and its relationship to the recipe-development Claude.ai Project.

## Reference

- Published at: https://lmccorvey85.github.io/recipes/
- Recipes are developed/refined in a separate Claude.ai Project (rules.md, recipe-index.md, recipes/ folder, ai-handoff.md, starter-prompt.md) — that Project's files aren't live-accessible from the streaming server; content gets pasted/uploaded in when turning a recipe into a page.
- Reorganized 2026-08-15 (commit `4b664b7`) from a flat pile of ~30 HTML files into category folders: `breakfast/`, `smoothies/`, `lunch/`, `snacks/`, `dinner/`, `drinks/`, `plans/` (archived meal plans/shopping lists), plus a real `index.html` homepage with category cards.
- There is no persistent local clone on the streaming server — the working copy used to build/edit pages lives in a session scratchpad that doesn't survive between conversations. Always `git clone`/pull this repo fresh before editing. This changelog living inside the repo (rather than as a standalone file elsewhere) means it now travels with every fresh clone.
- Cooking preferences and the 28-part full-recipe format used when developing new recipes: Southern/Cajun-leaning, mild-medium spice, dinner categorized as Quick Weeknight / Standard Dinner / Full Flavor, velveting technique for chicken, no apple cider vinegar, Kroger (Riley Fuzzel Rd / Spring, TX) shopping lists.

## Site structure / publishing changes

- **2026-08-15 — Site reorganization.** Flat ~30-file layout replaced with category folders (`breakfast/`, `smoothies/`, `lunch/`, `snacks/`, `dinner/`, `drinks/`, `plans/`) and a new `index.html` homepage with category cards. Commit `4b664b7`.
- **2026-08-26 — Changelog moved into this repo.** Previously tracked as a standalone file (`~/recipe-site-changelog.md`) on the streaming server, outside version control. Moved here as `CHANGELOG.md` so it's versioned, diffable, and persists across sessions via git instead of a loose local file.

## Recipe corrections

- **Stir fry oversalting fix** — baked into `dinner/velveted_chicken_stir_fry.html`: switched to low-sodium soy sauce, reduced oyster sauce.

## Reference docs mirrored

- **2026-09-07 — `rules.md` and `ai-handoff.md` added.** Mirrored the recipe-development Claude.ai Project's actual rulebook and handoff doc into this repo (previously only a summary existed, held in a separate session's memory — now the authoritative source is versioned here too).

## New recipes

- **2026-08-28 — Cajun Shrimp & Sausage Skillet with Buttered Garlic Green Beans.** Added `dinner/cajun_shrimp_sausage_skillet.html`, linked from `index.html`. Developed in the recipe Project, then scaled from the original 4-serving version to a 6-serving meal-prep batch with the sauce doubled again (on top of the recipe's usual "double sauce" rule) after the first cook ran too thin to coat the rice.

## Known / pending issues

- **Cajun Ranch Baked Chicken Thighs** needs a smoother/more spreadable seasoning paste (flagged in the Claude.ai Project's own memory as of 2026-08-15) — the recipe file content itself hasn't been brought into a session yet, only the fact that the fix is pending.

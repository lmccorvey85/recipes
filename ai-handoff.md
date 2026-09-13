# AI Handoff — How This Project Works

**Purpose:** Recipe collection assistant — dinner planning (with full detailed recipes + Kroger shopping lists), plus desserts and drinks. One chat per recipe/session; each chat starts fresh using the starter prompt.

Mirrored here (in the GitHub recipes site repo) alongside `rules.md` so both are durable and versioned — the source Claude.ai Project isn't git-tracked itself.

## File map (in the Claude.ai Project)

- `custom-instructions.md` — pasted into the Project's Instructions field in Claude.ai settings. This is the "always on" behavior layer.
- `rules.md` — the full detailed rulebook (formats, required fields, Kroger cart table, rice rules, shortcut system, etc.). Referenced, not duplicated, by the instructions. Mirrored in this repo.
- `recipe-index.md` — one-line-per-recipe master list, grouped by category. Check this first when asked for ideas in a theme, or "what recipes do I have."
- `recipes/*.md` — one file per saved recipe, full detail, using the Saved Recipe Entry Format from `rules.md`.
- `starter-prompt.md` — what gets pasted at the top of a new chat.

## Workflow each session (in the Claude.ai Project)

1. A new chat is opened in the Project and the starter prompt is pasted in, filled in.
2. The assistant checks `recipe-index.md` (and relevant `recipes/*.md` files) for saved-favorite fits before generating ideas.
3. The assistant develops/finalizes one recipe per chat, following the Full Recipe Format in `rules.md`.
4. When told "save it" or "save with changes," the assistant outputs a clean Saved Recipe Entry (format in `rules.md`) to paste into a new file under `recipes/`, plus a one-line addition for `recipe-index.md`. The assistant does NOT edit Project files directly — files are updated manually via Claude.ai's UI.
5. Chat ends; the next recipe gets its own new chat.

## What NOT to do

- Don't dump the entire recipe ledger back into the Instructions field — keep instructions short and point to files instead.
- Don't apply dinner-only rules (vegetable side requirement, Success Rice rule, cooking-mode timing targets) to desserts or drinks.
- Don't use live Kroger pricing unless asked — default is estimates, no web search needed.
- Don't try to update the GitHub HTML recipe site from the recipe-development Project — that's this repo's job, handled in a separate session.

## Relationship to this GitHub site

The recipe-development Claude.ai Project is where recipes get drafted/refined, following `rules.md`'s Full Recipe Format. Once a recipe is finalized there (or developed directly in a session working on this repo), it gets turned into an HTML page here under the matching category folder in `dinner/`, `breakfast/`, etc., linked from `index.html`, and logged in `CHANGELOG.md`.

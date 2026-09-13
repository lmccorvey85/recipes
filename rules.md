# Rules.md — Detailed Rulebook

This file holds the detailed rules referenced by the recipe-development Claude.ai Project's custom instructions. It is mirrored here (in the GitHub recipes site repo) so it's durable and versioned, since the Project itself isn't git-tracked. Read this whenever generating dinner ideas, full recipes, or shopping lists — whether in the Project or when turning a recipe into a site page here.

## Dinner Idea Format (3 options by default)

Each option includes: meal name; new vs. saved favorite; main dish; two side dishes (at least one vegetable); prep time; cook time; total time; active work time; servings/yield; difficulty; estimated Kroger price range; estimated price per serving; spice level (mild / mild-medium / medium); simple nutrition per serving (calories, protein, carbs, fat, sodium if reasonable); why I might like it; major equipment needed; useful shortcut ingredients; best mode (Quick Weeknight / Standard Dinner / Full Flavor).

After the 3 options: give a final best-pick recommendation with reasoning (flavor, convenience, budget, timing, leftovers, saved-recipe fit, my preferences).

## My Cooking Preferences

Default serving size: 4. Meal prep: scale to 6–8 unless told otherwise. Budget target: under $50, flexible if scaling up or worth it.

Favorites: baked chicken, stir fry, cabbage dishes, spaghetti (baked & stovetop), Southern-style meals — but still want variety outside these.

Prefer Southern-style seasoning when it fits; open to other cuisines. Mild to medium spice unless I ask for more. Juicy/tender meat methods required — during cooking, serving, storage, and reheating.

Stir fry: prefer frozen stir fry vegetable bags over hand-cutting.

Shortcuts welcome (boxed/packet mixes, jarred sauces, frozen veg, canned sides, pre-cut veg, store-bought components, Success Rice) — always doctor them up for better flavor.

## Required Side Dish Rules (dinner only)

Every complete dinner needs at least one vegetable side. Rice does not count as one of the two sides. Don't overuse toast, garlic bread, or salad.

Preferred vegetable sides: doctored canned green beans, frozen/canned sweet corn, doctored Glory greens, cabbage, mashed potatoes, roasted cubed potatoes, broccoli, asparagus, Brussels sprouts, honey-butter carrots, or other fitting vegetables.

## Pantry / Staple Items (assume I may have)

Tony Chachere's, Slap Ya Mama, sea salt, black pepper, onion powder, garlic powder, chicken bouillon powder. Don't force these into everything — use when they fit. Recommend other seasonings/herbs/sauces/aromatics as needed.

## Kitchen Equipment I Have

Oven, stovetop, air fryer, slow cooker/Crock-Pot, Instant Pot, cast iron skillet, 14" carbon steel Yosukata wok, meat thermometer, baking rack, sheet pans, standard pots/pans, mixing bowls, cutting board, knives, measuring cups/spoons.

Stir fry recipes must account for wok preheating, oiling, batch size, and avoiding overcrowding. Every full recipe lists equipment needed.

## Rice and Success Rice Rule (dinner only, when rice is included)

Prefer Success boil-in-bag rice. For any rice-included recipe, use this block:

**Rice needed:**
- Cooked rice needed:
- Regular Success Rice bags:
- Family-size Success Rice bags:
- Rice prep note: (fresh / chilled / day-old / buttered / seasoned / plain)

Always remind to check the box yield since package sizes vary. Rice never counts as one of the two required sides.

## Full Recipe Format (28 parts)

1. Recipe title
2. Mode used
3. Servings
4. Meal-prep scaling option (6–8 servings) when useful
5. Prep time
6. Cook time
7. Total time
8. Active work time
9. Estimated Kroger cost
10. Estimated cost per serving
11. Spice level
12. Simple estimated nutrition per serving
13. Full ingredient list with exact measurements
14. Equipment list
15. Ingredient prep instructions
16. Detailed cooking instructions
17. Detailed timeline so main + sides finish together
18. Keeping food warm instructions
19. Flavor and tenderness tips
20. Juiciness tips for meat
21. Easier shortcut alternatives
22. Individual/from-scratch version vs. shortcut/packet/boxed version when useful
23. Storage instructions
24. Reheating instructions
25. Things to check before shopping
26. Grocery list by Kroger section
27. Kroger cart-building version (when requested)
28. Save-for-later prompt

## Detailed Cooking Directions Rule

Never give only broad timeline steps. Include: what to wash/drain/pat dry/trim/chop/slice/dice/mince/peel/measure and cutting size/shape when it matters; when to start each side so everything finishes together; stove heat level per step (low/medium-low/medium/medium-high/high); oven temp, rack position, pan size, lined/greased or not; covered vs. uncovered; when to stir/flip/rotate/baste/toss/uncover/check; approximate timing per step; visual doneness signs; safe internal temp for meat; resting time; keeping-warm instructions; storage/reheating that protects juiciness and texture.

Sheet-pan/oven meals: note pan rotation/rack switching. Stovetop meals: note when to lower heat to prevent burning/drying/over-thickening. Wok/stir fry: note preheating, oiling, batch cooking, when to pull ingredients out and return them, and how to avoid overcrowding/steaming.

## Double Sauce / Gravy Rule

Any gravy, sauce, marinade, glaze, pan sauce, cream sauce, stir fry sauce, spaghetti sauce, or dipping sauce gets scaled to a generous double amount unless it would ruin the dish — label it **"Double sauce amount."** If the full double might make the dish too wet, add ~75% first and adjust to taste.

## Shortcut System

For any labor-heavy or from-scratch component, give: (1) best flavor method, (2) shortcut method, (3) how to doctor it up, (4) tradeoff explanation.

Useful shortcuts: upgraded boxed cornbread mix; doctored store-bought gravy packets; doctored jarred pasta sauce; frozen vegetables; bagged cabbage/coleslaw mix; rotisserie chicken; steam-in-bag vegetables; Success Rice; doctored boxed/packet seasoning blends.

## Recipe Review and Improvement Mode

When an existing recipe is provided: identify what's good; identify what's bland/dry/inefficient/unclear/under-seasoned/over-complicated/failure-prone; improve while keeping the original idea intact unless told otherwise; upgrade flavor/tenderness/juiciness/texture/timing/instructions/side pairing; add missing measurements, temps, internal temps, equipment, prep/cutting steps, sauce amounts (apply double-sauce rule), storage, reheating, Kroger list, estimated cost, nutrition, shortcut alternatives, individual-vs-shortcut method; explain the most important changes and why.

## Kroger Shopping Context

Shop near Riley Fuzzel Rd / 2323 Silver Plume Ln, Spring, TX. Use estimated prices by default. Organize grocery lists by section: Produce, Meat/Seafood, Dairy, Frozen, Pantry/Dry Goods, Canned/Jarred Goods, Bakery, Rice/Pasta/Grains, Spices/Seasonings, Condiments/Sauces, Refrigerated, Optional upgrades.

Before the final list, include a "Check before buying" list of pantry staples already on hand.

## Kroger Cart-Building Version

Table format:

| Kroger section | Search phrase | Amount needed | Suggested package size | Estimated price | Notes |
|---|---|---:|---|---:|---|

Also include: pantry check first; must-buy items; optional upgrades; shortcut swaps; budget estimate; estimated cost per serving; notes on which pantry staples reduce checkout cost. Keep concise enough to quickly search Kroger and add to cart.

## Saved Recipe Entry Format

Used in the recipe-development Project whenever a recipe is saved — pasted into a new file under that Project's `recipes/` folder and added as a line to `recipe-index.md`:

```
#### Recipe Name
- Category:
- Main dish:
- Side dishes:
- Vegetable side:
- Key ingredients:
- Sauce/gravy/marinade/seasoning notes:
- Success Rice guidance, if included:
- Shortcut options:
- User feedback:
- Future changes:
- Save date:
```

## Standalone Recipe Prompt

After finalizing any recipe, generate a clean standalone prompt (for pasting into a plain chat) including: recipe name, servings, mode, main dish, side dishes, vegetable side, rice instructions + Success Rice bag guidance if applicable, double-sauce requirement, equipment, detailed timeline, storage, reheating, nutrition, estimated cost, shortcut alternatives, individual seasoning/sauce option, shortcut packet/boxed option, and flavor/tenderness/juiciness priorities.

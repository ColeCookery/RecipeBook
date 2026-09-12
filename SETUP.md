# Cole Cookery — new setup

## What changed

- The site is now a **Jekyll** site instead of hand-written HTML pages. GitHub Pages
  and Netlify both build Jekyll natively — you don't run anything locally unless you
  want a live preview while editing.
- Every recipe is one small file in `_recipes/` (front matter: title, category, image,
  ingredients, instructions, status). The recipe page, category pages, homepage, and
  search page are all generated automatically from these files — you never hand-edit
  HTML for a new recipe again.
- Adding a recipe = filling out a form at **`/admin`** (once set up below). That form
  writes the file to `_recipes/` and commits it to GitHub for you.
- Draft recipes: set **Status: Draft** in the form. Draft recipes are excluded from the
  homepage, category pages, and search — but the page still exists at its own URL if
  you want to check it while you work on it. (Note: this makes it *unlisted*, not
  password-protected — don't put anything sensitive in a draft.) Flip to
  **Published** whenever it's ready.

## Why Netlify instead of GitHub Pages

The no-code admin form (Decap CMS) needs somewhere to handle GitHub login securely.
GitHub Pages alone can't do that without a custom server. Netlify has this built in
for free (Identity + Git Gateway), so we're using Netlify to host the *live* site,
while your GitHub repo stays the actual source of truth — every edit still shows up
as a normal commit in `ColeCookery/RecipeBook`. You can point a custom domain at
Netlify later if you want; the `.github.io` link would just stop being the live one.

## One-time setup

1. **Replace the repo contents.** In your `RecipeBook` repo, delete the old files
   (or start fresh in a new branch) and copy in everything from this folder.
   Commit and push to `main`.

2. **Create a free Netlify account** at netlify.com and choose
   "Add new site → Import an existing project → GitHub", then pick `RecipeBook`.
   Netlify will read `netlify.toml` automatically (build command and publish folder
   are already configured).

3. **Turn on Identity + Git Gateway** (in Netlify: Site configuration → Identity →
   Enable Identity, then Services → Git Gateway → Enable). Under Identity settings,
   invite yourself by email — you'll get a link to set a password.

4. **Update `admin/config.yml`** — replace the `site_url` and `display_url` with your
   actual Netlify URL once you have it (e.g. `https://cole-cookery.netlify.app`).

5. Visit **`yoursite.netlify.app/admin`**, log in, and you're editing with a form —
   no more copying HTML files.

## About your existing content

I migrated your 12 real recipes into the new format exactly as written (ingredients
and instructions preserved verbatim). A few things I found while migrating that are
worth knowing about — these are exactly the kind of thing that happens when
everything's tracked by hand:

- **"Barbacoa"** was listed in `recipes.json` under Mexican, but its link actually
  pointed at the Lasagna file — there's no real Barbacoa recipe content anywhere in
  the repo. I didn't fabricate one; add it fresh via `/admin` whenever you write it up.
- **"Chocolate Cake"** in `recipes.json` pointed to a file that doesn't exist
  (`recipes/chocolate-cake.html`); the actual `2chocolate-cake.html` in the repo looks
  like an early placeholder/test file rather than your real recipe, so I left it out.
- **`2Chili.html`** wasn't linked from any category page or `recipes.json` at all —
  a fully orphaned recipe — and its content was placeholder text, not a real recipe.
- **`2spaghetti-bolognese.html`** was an old test file using a different, earlier
  template — not a real listed recipe.

None of these are in the new site. If any of them are actually recipes you care
about, just add them through `/admin` — that's now a two-minute job instead of a
multi-file edit.

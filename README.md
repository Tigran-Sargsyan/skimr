# skimr

A personal reading list site. The pipeline checks YouTube channels daily, fetches
captions for new videos, runs three OpenAI calls to summarize, classify, and score
each one against your profile, and rebuilds an Astro site that's deployed to
GitHub Pages.

No login. No app. No notifications. Just a URL you check on your phone.

## What's in here

- `pipeline/` — Python 3.11+ pipeline. Single synchronous script.
- `site/` — Astro 4 static site.
- `data/` — `profile.yaml`, `sources.yaml`, and the SQLite DB. All committed.
- `.github/workflows/digest.yml` — daily cron + manual trigger + Pages deploy.

## First-time setup

1. **Create a GitHub repo** (public or private).
2. **Clone it locally** and copy these files in.
3. **Fill in `data/profile.yaml`** — start from `data/profile.yaml.example`. The
   five theme keys (`tech`, `thinking`, `culture`, `business`, `science`) are
   fixed; don't add others.
4. **Fill in `data/sources.yaml`** — start from `data/sources.yaml.example`.
   Channel handles begin with `@`.
5. **Set the OpenAI API key as a GitHub secret**:
   Settings → Secrets and variables → Actions → New repository secret →
   name `OPENAI_API_KEY`.
6. **Enable GitHub Pages**:
   Settings → Pages → Source → "GitHub Actions".
7. **Update `site/astro.config.mjs`** — replace `username` with your GitHub
   username. Drop the `base: '/skimr'` line if you serve from a custom domain
   or the root of `<username>.github.io`.
8. **Initialize the database**:
   ```bash
   uv sync
   uv run python scripts/init_db.py
   ```
9. **Commit the initial state and push.**
10. **Trigger the first run**: GitHub → Actions → Skimr Daily Digest → Run workflow.
    This will backfill the past `SKIMR_BACKFILL_DAYS` (default 7) days from each
    source.
11. **Visit your site** at `https://<username>.github.io/skimr/`.

After that, the workflow runs every day at 04:00 UTC.

## Local development

Local development needs `uv` (https://github.com/astral-sh/uv) and Node 20+.

```bash
cp .env.example .env
# edit .env to set OPENAI_API_KEY

# Run the pipeline once
uv sync
uv run python -m pipeline.main

# Boot the site dev server
cd site
npm ci
npm run dev
```

The pipeline writes markdown to `site/src/content/items/`. Re-running the
pipeline only does work for items that haven't progressed past their stage,
so it's safe to run repeatedly.

## Configuration

| Env var                    | Default          | Notes                                     |
|----------------------------|------------------|-------------------------------------------|
| `OPENAI_API_KEY`           | (required)       | OpenAI API key                            |
| `SKIMR_MODEL_SUMMARIZE`    | `gpt-5.4-mini`   | Model for the summary call                |
| `SKIMR_MODEL_CLASSIFY`     | `gpt-5.4-mini`   | Model for the classification call         |
| `SKIMR_MODEL_SCORE`        | `gpt-5.4-mini`   | Model for the scoring call                |
| `SKIMR_REASONING_SUMMARIZE`| `low`            | reasoning_effort for summarize            |
| `SKIMR_REASONING_CLASSIFY` | `minimal`        | reasoning_effort for classify             |
| `SKIMR_REASONING_SCORE`    | `medium`         | reasoning_effort for score                |
| `SKIMR_HOMEPAGE_LIMIT`     | `10`             | How many items to show on the home page   |
| `SKIMR_BACKFILL_DAYS`      | `7`              | First-run backfill window per source      |
| `SKIMR_DB_PATH`            | `data/digest.db` | SQLite DB path                            |
| `SKIMR_SITE_CONTENT_DIR`   | `site/src/content/items` | Where rendered markdown goes      |

## How it works

```
discover (yt-dlp)  →  fetch transcript  →  summarize  →  classify  →  score  →  render md
```

Each step writes back to SQLite. Failures on individual items don't abort the
run — they get marked `failed` (or `no_transcript`) and the rest of the batch
continues.

## What it isn't (v1)

No auth. No multi-user. No email digest. No Telegram. No RSS. No audio
transcription (captions only). No favorites. No feedback. See the spec for
the v2 roadmap.

## Cost

Three OpenAI calls per item with mini-class models. At ~10 new items/day this
runs well under $5/month.

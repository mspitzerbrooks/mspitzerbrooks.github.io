# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Personal academic website for Matthew Spitzer Brooks (Ph.D. Candidate, UC Davis), built on the [Academic Pages](https://academicpages.github.io/) Jekyll template — a fork of the Minimal Mistakes theme.

## Running locally

```bash
bundle install          # install Ruby dependencies
jekyll serve -l -H localhost  # serve at localhost:4000 with live reload
```

Or with Docker:
```bash
docker build -t jekyll-site .
docker run -p 4000:4000 --rm -v $(pwd):/usr/src/app jekyll-site
```

**Note:** Changes to `_config.yml` require restarting the server — live reload does not pick them up.

## Content architecture

Site content lives in a few key places:

- **`_pages/`** — Standalone pages (about, research, teaching, students, CV, etc.). The homepage is `_pages/about.md` (permalink: `/`). The research and teaching pages are hand-maintained markdown files — they are NOT auto-generated from collections.
- **`_publications/`, `_talks/`, `_teaching/`, `_portfolio/`** — Jekyll collections that generate individual pages. Each file uses YAML frontmatter and is rendered via layouts in `_layouts/`.
- **`files/`** — PDFs and downloadable files, served at `https://mspitzerbrooks.github.io/files/<filename>`.
- **`images/`** — Site images (author avatar, etc.).
- **`_data/`** — Navigation and other structured data (YAML).
- **`_config.yml`** — Site-wide settings: author info, social links, publication categories, collection config, and plugin settings.

## Key pages to know

The pages most likely to be updated are:

- `_pages/about.md` — Homepage bio, news items, and research summaries
- `_pages/research.md` — Full publication list with abstracts (hand-maintained, uses `<details>`/`<summary>` HTML for collapsible abstracts)
- `_pages/teaching.md` — Teaching history, student eval excerpts, and mentoring info
- `_pages/cv.md` — CV page (links to `files/BrooksCV.pdf`)

## Content patterns

**Collapsible abstracts** on the research and about pages use raw HTML:
```html
<details>
  <summary><small><strong>Show Abstract</strong></small></summary>
  <p>Abstract text here.</p>
</details>
```

**Inline metadata** (conference presentations, funding, pre-analysis plans) uses `<small>` and `<br>` tags for visual grouping under a paper entry.

**Publication categories** in `_config.yml` (`books`, `manuscripts`, `conferences`) control headings when using the publications collection — but the research page currently uses a hand-written list rather than the collection.

## Markdown generator

`markdown_generator/` contains Jupyter notebooks and Python scripts to generate markdown files for talks and publications from TSV files. Use these when adding multiple entries at once rather than writing individual markdown files by hand.

## Deployment

Pushing to `master` triggers GitHub Pages to build and deploy the site automatically. The live site is at `https://mspitzerbrooks.github.io`.

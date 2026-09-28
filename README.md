# Siya Chhibber — Portfolio

A complete, responsive static website with seven project pages. All finished HTML is included. GitHub Pages requires no build, install, API key, or backend.

## Preview it

Unzip the package and open `index.html` in a browser. Project pages, images, the video, and the journalism PDF use relative links.

For a local web-server preview, use either:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`. Or, with Node.js installed, run `npm run dev` and open `http://localhost:4173`. There is no `npm install` step.

## Put it on GitHub Pages

1. Create a GitHub repository. Use `siya-portfolio` for a project URL, or `YOUR-USERNAME.github.io` for an account homepage. A public repository works with GitHub Free.
2. Upload the **contents** of this folder to the repository. `index.html` must be at the repository root, next to `assets`, `projects`, and `downloads`. Do not upload only the ZIP or put the whole website inside an extra outer folder.
3. Open the repository’s **Settings → Pages**.
4. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
5. Choose **main** and **/(root)**, then save.
6. When the deployment completes, use the website URL shown on the Pages settings screen.

For a project repository, the URL format is `https://YOUR-USERNAME.github.io/siya-portfolio/`. The included relative paths also work under a custom domain or account homepage. No custom domain is configured in this package.

The `.nojekyll` file is included for direct static hosting. If your upload interface hides this file, you can create an empty `.nojekyll` file in the repository. No custom GitHub Actions workflow is required for branch deployment.

Official instructions, checked September 26, 2026:

- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Edit the content

The simplest approach is to change the visible text directly in `index.html` or in a page under `projects/`. Changes are ready to publish immediately.

For consistent edits across the site, edit `content.json`, then run:

```bash
python3 tools/build.py
```

The generator uses only Python’s standard library. It rewrites `index.html` and all seven project pages. Keep edits in `content.json` and `tools/build.py` if you use this route; direct HTML changes would otherwise be overwritten. Commit the regenerated HTML as well as the source content. GitHub does not run this optional generator automatically.

`assets/styles.css` controls colors, typography, spacing, and responsive layouts. The two Google Fonts are optional; the stylesheet includes local fallback fonts. They can be removed by deleting the first `@import` line for fully offline typography.

## Add or replace media

- Put web-ready photos in `assets/` and update the matching filename and alt text in `content.json`.
- Kina’s visuals are extracted from Siya’s supplied project slides. The crochet collection image and poster are frames from her supplied video; the wearable photo is her supplied photo.
- The crochet video is a compressed copy of the provided 62.7-second edit. The original is not modified. Native video controls are enabled and playback is never automatic.
- `downloads/journalism-portfolio.pdf` is the supplied journalism portfolio, with a simplified filename.
- Pill Sleeve has an explanatory LED-state diagram. DropLedger has a clearly labeled interface concept with invented sample data. These are not presented as photographs or released-product screenshots.
- Add authentic book-cover images, Pill Sleeve photographs, or actual DropLedger screens when available. The current pages are complete without empty image slots or broken links.

## Content notes

The page copy is an editable first-person draft based on the portfolio materials provided. Both Pill Adherence Sleeve and DropLedger are attributed to Siya, following the ownership correction in this conversation.

Current status labels preserve what is documented: Kina is a working prototype without blind-user testing; the pill sleeve is under testing; DropLedger is described through its product and architecture design because implementation status has not been provided. Update these labels as the projects progress.

The published 2025 NASA poster links to its confirmed NTRS record. The portfolio describes the second summer’s Ground Scenarios work from Siya’s project summary; its separate NTRS link is omitted because the record could not be opened during preparation.

No personal email address, phone number, street address, private rental information, or account credentials are included. Add a public-facing contact address only if desired.

No analytics, cookies, contact-form service, or AI API is used by this portfolio website. DropLedger’s technology stack appears as project content only.

## Files

- `index.html` — homepage with all selected work and about section
- `projects/` — seven standalone project stories
- `assets/` — stylesheet, project images, and compressed video
- `downloads/` — journalism PDF
- `content.json` — centralized, editable page content
- `tools/build.py` — optional standard-library HTML generator
- `tools/dev-server.mjs` — optional dependency-free local server
- `package.json` — convenience preview/build commands; no dependencies

Website text and original creative work belong to Siya Chhibber. Existing third-party crochet pattern attribution is preserved in the supplied video; no claim is made that every featured character pattern is original.

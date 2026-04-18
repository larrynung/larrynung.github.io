# AGENTS.md

## Build & Run

- **Local dev server**: `hugo server -D`
- **Production build**: `hugo --minify`
- **Output**: `public/` directory

## CI/CD

- Deploys automatically on push to `hugo` branch via `.github/workflows/hugo.yml`
- Requires manual trigger if not on `hugo` branch

## Structure

- `config/_default/hugo.toml` - Hugo config
- `content/posts/` - Blog posts (Markdown)
- `themes/PaperMod/` - Theme (submodule)
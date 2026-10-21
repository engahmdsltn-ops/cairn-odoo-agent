"""Fill the site template from publish.config.yaml and write site/index.html."""
import argparse
import html
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "site" / "index.template.html"
OUTPUT = ROOT / "site" / "index.html"


class BuildError(Exception):
    pass


def repo_url(config):
    repo = config.get("repo") or {}
    if repo.get("url"):
        return repo["url"]
    owner, name = repo.get("owner"), repo.get("name")
    if not owner or not name:
        raise BuildError("repo.owner and repo.name (or repo.url) are required")
    return f"https://github.com/{owner}/{name}"


def render(template, config):
    author = config.get("author") or {}
    name = (author.get("name") or "").strip()
    if not name:
        raise BuildError("author name is empty")
    urls = {
        "{{REPO_URL}}": repo_url(config).strip(),
        "{{PORTFOLIO_URL}}": (author.get("portfolio_url") or "").strip(),
    }
    for url in urls.values():
        if not url.startswith("https://"):
            raise BuildError(f"URL is not https: {url!r}")
    out = template
    for key, url in urls.items():
        out = out.replace(key, html.escape(url, quote=True))
    out = out.replace("{{AUTHOR_NAME}}", html.escape(name, quote=True))
    if "{{" in out:
        raise BuildError("unfilled placeholder remains in output")
    return out


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=ROOT.parent / "publish.config.yaml")
    args = parser.parse_args(argv)
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    try:
        OUTPUT.write_text(render(TEMPLATE.read_text(encoding="utf-8"), config), encoding="utf-8")
    except BuildError as exc:
        print(f"build failed: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

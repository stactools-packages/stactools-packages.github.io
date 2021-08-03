from pathlib import Path
import requests
from datetime import datetime
from jinja2 import Template


def get_repos() -> list:
    """Get a list of repositories from Github

    Returns:
        list: List of dictionaries containing repos.
    """
    with requests.get("https://api.github.com/users/stactools-packages/repos") as site:
        data = site.json()

    return data


def main() -> str:
    """Create a readme markdown document and populate the Repo table
    from the stactools-package Github Organizations.

    Returns:
        str: Markdown document
    """
    data = get_repos()
    now = datetime.utcnow().strftime("%b %d %H:%M %Z %Y")
    template = Template(Path("./README_TEMPLATE.md.jinja").read_text())

    with Path("./README.md") as f:
        f.write_text(template.render(packages=data, updated_time=now))

    return True


if __name__ == "__main__":
    main()

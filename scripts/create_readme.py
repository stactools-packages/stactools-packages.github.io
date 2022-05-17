from os import error
from pathlib import Path
import requests
from datetime import datetime
from jinja2 import Template
import logging

logger = logging.getLogger(__name__)


def get_repos() -> list:
    """Get a list of repositories from Github

    Returns:
        list: List of dictionaries containing repos.
    """
    try:
        with requests.get(
                "https://api.github.com/users/stactools-packages/repos?per_page=1000"
        ) as site:
            data = site.json()
    except error as e:
        logger.error(f"Requests could not complete. {e}")

    return data


def main() -> bool:
    """Create a readme markdown document and populate the Repo table
    from the stactools-package Github Organizations.

    Returns:
        bool: True if it worked
    """
    data = get_repos()
    now = datetime.utcnow().strftime("%b %d %H:%M %Z %Y")
    template = Template(Path("./README_TEMPLATE.md.jinja").read_text())

    with Path("./README.md") as f:
        f.write_text(template.render(packages=data, updated_time=now))

    return True


if __name__ == "__main__":
    main()

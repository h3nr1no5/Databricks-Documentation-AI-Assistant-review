import json
from pathlib import Path

import requests
import trafilatura
from tqdm import tqdm

from src.config import DOCS_DIR

URLS = json.load(open(DOCS_DIR / "urls.json"))

OUTPUT = DOCS_DIR
OUTPUT.mkdir(parents=True, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0"
}

for i, url in enumerate(tqdm(URLS)):

    try:

        html = requests.get(
            url,
            headers=headers,
            timeout=30,
        ).text

        markdown = trafilatura.extract(
            html,
            output_format="markdown",
            include_links=True,
        )

        if markdown is None:
            continue

        document = {
            "id": i,
            "url": url,
            "markdown": markdown,
        }

        with open(
            OUTPUT / f"{i}.json",
            "w",
            encoding="utf8",
        ) as f:

            json.dump(
                document,
                f,
                ensure_ascii=False,
                indent=2,
            )

    except Exception as e:

        print(url)
        print(e)
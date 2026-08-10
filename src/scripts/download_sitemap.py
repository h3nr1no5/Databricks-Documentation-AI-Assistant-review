import requests
import xml.etree.ElementTree as ET
from pathlib import Path
import json
import sys

SITEMAP_URL = "https://docs.databricks.com/sitemap.xml"

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.config import DOCS_DIR

OUTPUT = DOCS_DIR
OUTPUT.mkdir(exist_ok=True)

print("Downloading sitemap...")

response = requests.get(SITEMAP_URL, timeout=60)
response.raise_for_status()

root = ET.fromstring(response.content)

namespace = {
    "ns": "http://www.sitemaps.org/schemas/sitemap/0.9"
}

urls = []

for url in root.findall("ns:url", namespace):

    loc = url.find("ns:loc", namespace)

    if loc is not None:
        urls.append(loc.text)

print(f"Found {len(urls)} URLs")

with open(OUTPUT / "urls.json", "w") as f:
    json.dump(urls, f, indent=2)

print("Saved urls.json")
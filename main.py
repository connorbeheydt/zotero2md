import json
import sqlite3
from markdownify import markdownify as md
from database_utils import get_bibdata, get_annotations, get_tabledata_from_parent_id, get_tabledata_from_id, get_tabledata_from_key
import jinja2
from jinja2 import Environment, FileSystemLoader
from typing import Dict

def main():
    print("PROGRAM START")

    zotero_dir = "./"
    output_dir = "./references/"
    target_citeref = "angioniDesignImplementationSubstation2017"

    # Load data from database and save as json
    cur_z = sqlite3.connect(f"file:./zotero.sqlite?mode=ro", uri=True).cursor()
    cur_b = sqlite3.connect(f"file:./better-bibtex.sqlite?mode=ro", uri=True).cursor()
    wanted_tables = ["itemAnnotations",  "itemNotes"]
    bibdata = get_bibdata(cur_b)
    ref_id = bibdata[target_citeref]["itemID"]
    ref_key = bibdata[target_citeref]["itemKey"]
    print(f"id: {ref_id}, key: {ref_key}")
    print(get_tabledata_from_parent_id(cur_z, "itemAnnotations", ref_id))
    context = {}
    for tablename in wanted_tables:
        context[tablename] = get_tabledata_from_parent_id(cur_z, tablename, ref_id)
    with open(f"{target_citeref}_info.json", "w") as f:
        f.write(json.dumps(context, indent=2))

    # Load from json and fill in template
    environment = Environment(loader=FileSystemLoader("templates/"))
    reference_template = environment.get_template("reference_template.md")
    
    with open(f"{output_dir}{target_citeref}.md", "w") as f:
        f.write(md(reference_template.render(context)))
    print("PROGRAM END")

if __name__ == "__main__":
    main()

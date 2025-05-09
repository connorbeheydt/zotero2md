## Overview
The idea of this project is to mimic the functionaltiy of the Obsidian plugin Zotero Connection. From a BetterBibTex citation key I want a nice looking markdown file laid out according to a template I specify.

SQLite -> json -> md

## TODO
- [ ] Match citation key to item
    - [ ] Match citation keys to relevant metadata, annotations, and notes
import json
    - [X] Get citationKeys
- [ ] Extract relevant data to json
- [ ] Fill in template with json information

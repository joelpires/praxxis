import os
import sys

from src.mtool.cli import mtool
from src.mtool.util.log import Log
from src.mtool.notebook import notebook

m = None
log = None
counter = 0
items = []
search_term = None

def search_notebook(args):
    global m
    global search_term
    global log

    log = Log()
    
    m = mtool.Mtool(args)
    search_term = args.term
    log.section("Search notebook names for", search_term)
    m.write_list(items)


def filter(filename):
    global counter
    global items
    global search_term

    nb = notebook.Notebook(filename)

    if (nb.name.lower().find(search_term)) > -1:
        counter += 1
        log.info(f"\t{str(counter)}.\t{nb.name} ({nb.library_name})")
        items.append([counter, nb.name, nb.library_name])

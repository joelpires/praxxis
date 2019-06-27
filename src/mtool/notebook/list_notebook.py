"""
This file lists all of the notebooks loaded into the library db file
"""
        
def list_notebook(scene_root, library_root, library_db, current_scene_db, start, stop):
    """ gets the notebooks from the sqlite db and displays them through its display function"""
    from src.mtool.util import sqlite_util
    from src.mtool.display import display_notebook

    notebooks = sqlite_util.list_notebooks(library_db, start, stop)
    sqlite_util.write_list(current_scene_db, notebooks)
    display_notebook.display_list_notebook(notebooks)
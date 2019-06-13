"""
This file calls a function to change the current scene.

Dependencies within mtool: mtool/mtool.py
"""

import os

def change_scene(args, root, history_db):
    """Calls mtool method to change the current scene"""
    from src.mtool.util import sqlite_util

    if hasattr(args, "name"):
        name = args.name
    else:
        name = args

    sqlite_util.update_current_scene(history_db, name)

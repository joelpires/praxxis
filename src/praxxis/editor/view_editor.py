"""
This file finds the current default editor
"""

def view_editor(_user_info_db):
    from src.praxxis.display import display_editor
    from src.praxxis.sqlite import sqlite_user

    editor = sqlite_user.get_user_info(_user_info_db)[6][1]
    display_editor.display_current_editor(editor)
    return editor

"""
This file lists all of the editors available to choose
"""

def list_editor(available_editors):
    from src.praxxis.display import display_editor

    display_editor.display_list_editors(available_editors)
    return available_editors

def change_editor(editor,_user_info_db):
    from src.praxxis.display import display_editor
    from src.praxxis.sqlite import sqlite_user

    sqlite_user.set_user_info(_user_info_db, "custom_editor", editor)

    display_editor.display_change_editor(editor)
    return editor

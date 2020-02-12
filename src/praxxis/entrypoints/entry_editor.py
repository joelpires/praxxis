"""
This file handles the editor functions of the CLI
"""

from src.praxxis.util.roots import _user_info_db

def change_editor(editor,_user_info_db=_user_info_db):
    from src.praxxis.editor import change_editor
    from src.praxxis.util import roots
    from src.praxxis.util import error

    available_editors = ["jupyter", "vim", "html", "ads"]

    change_editor.list_editor(available_editors)

    editor = input("")

    if editor.isdigit():
        if int(editor) <= len(available_editors):
            editor = available_editors[int(editor) - 1]
            change_editor.change_editor(editor,_user_info_db=_user_info_db)
        else:
            raise error.EditorNotFoundError(editor)
    elif editor not in available_editors:
        raise error.EditorNotFoundError(editor)
    else:
        change_editor.change_editor(editor,_user_info_db=_user_info_db)

def view_editor(user_info_db=_user_info_db):
    from src.praxxis.editor import view_editor
    from src.praxxis.util import roots

    view_editor.view_editor(_user_info_db)

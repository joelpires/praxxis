"""
This file contains the sqlite functions for the user management
"""

def get_user_info(_user_info_db):
    """retrieves user's the custom editor"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(_user_info_db)
    cur = conn.cursor()

    get_custom_editor = 'SELECT * FROM "UserInfo"'
    cur.execute(get_custom_editor)

    conn.commit()
    row = cur.fetchall()
    conn.close()

    if row == []:
        raise error.UserNotFoundError()

    return row


def set_user_info(_user_info_db, key, value):
    """it sets the custom editor of the user"""
    from src.praxxis.sqlite import connection

    conn = connection.create_connection(_user_info_db)
    cur = conn.cursor()

    set_custom_editor = 'UPDATE "UserInfo" SET Value = ? WHERE Key = ?'
    cur.execute(set_custom_editor, (value, key))

    conn.commit()
    conn.close()

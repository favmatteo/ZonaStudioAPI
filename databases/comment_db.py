from lib.app import database
from databases.school_address_db import get_id_by_school_address


def create_comment_on_freepost(
    text: str,
    id_free_post: int,
    id_student: str = None,
    id_helper: str = None,
) -> bool:
    id_writer = ""
    if id_student:
        id_writer = id_student
    else:
        id_writer = id_helper
    query = """INSERT INTO Comment (text, id_freePost, id_user) VALUES (%s, %s, %s)"""
    database.cursor.execute(query, (text, id_free_post, id_writer))
    database.conn.commit()


def get_comment_on_freepost(id: int):
    query = """SELECT * FROM Comment WHERE id_freePost = (%s)"""
    database.cursor.execute(query, (id,))
    result = database.cursor.fetchall()
    return result

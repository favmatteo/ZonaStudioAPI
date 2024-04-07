from lib.app import database
from databases.school_address_db import get_id_by_school_address


def create_free_post(
    title: str,
    description: str,
    id_student: str,
    tags=None,
) -> bool:
    query = f"""
    INSERT INTO FreePost (title, description, tags, id_student)
    VALUES (%s, %s, %s, %s)
    """
    database.cursor.execute(query, (title, description, tags, id_student))
    database.conn.commit()


def get_all_post_of_a_user(uid: str):
    query = """
    SELECT *
    FROM FreePost
    WHERE id_student = %s
    """
    database.cursor.execute(query, (uid,))
    posts = database.cursor.fetchall()
    return posts


def get_free_post(id: int):
    query = f"SELECT * FROM FreePost WHERE id_post = {id}"
    database.execute(query)
    free_post = database.fetch_one()

    return free_post

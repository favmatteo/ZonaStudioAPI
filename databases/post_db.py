from lib.app import database
import databases.tag_db


def create_free_post(
    title: str,
    description: str,
    id_student: str,
    tags=None,
) -> str:
    query = """
    INSERT INTO FreePost (title, description, id_student)
    VALUES (%s, %s, %s)
    """
    database.cursor.execute(query, (title, description, id_student))
    database.conn.commit()

    # Get the ID of the last inserted post
    database.cursor.execute("SELECT LAST_INSERT_ID()")
    id_post = database.cursor.fetchone()[0]

    id_tags = []
    if tags:
        for tag in tags:
            id_tags.append(databases.tag_db.create_tag(tag))

    for id_tag in id_tags:
        query = """INSERT INTO PostHasTag (id_freePost, id_tag) VALUES (%s, %s)"""
        database.cursor.execute(query, (id_post, id_tag))

    database.conn.commit()

    return id_post


def get_all_post_of_a_user(uid: str):
    query = """
    SELECT FreePost.*, Tag.tag
    FROM FreePost
    LEFT JOIN PostHasTag ON FreePost.id_post = PostHasTag.id_freePost
    LEFT JOIN Tag ON PostHasTag.id_tag = Tag.id_tag
    WHERE FreePost.id_student = %s
    """
    database.cursor.execute(query, (uid,))
    posts_with_tags = database.cursor.fetchall()
    return posts_with_tags


def get_free_post(id: int):
    query = f"SELECT * FROM FreePost WHERE id_post = {id}"
    database.execute(query)
    free_post = database.fetch_one()

    return free_post

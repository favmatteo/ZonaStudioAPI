from lib.app import database
from databases.school_address_db import get_id_by_school_address


def create_tag(tag: str):
    tag = tag.lower()
    query = """
    INSERT INTO Tag (tag)
    SELECT %s
    WHERE NOT EXISTS (
        SELECT 1 FROM Tag WHERE tag = %s
    );
    """
    database.cursor.execute(query, (tag, tag))
    database.conn.commit()

    # Ottieni l'ID del tag appena inserito o già esistente
    query_get_id = """
    SELECT id_tag FROM Tag WHERE tag = %s
    """
    database.cursor.execute(query_get_id, (tag,))
    tag_id = database.cursor.fetchone()  # Assume che ci sia solo un risultato

    return tag_id[0] if tag_id else None


def get_tags_for_post(post_id: str) -> list:
    query = """
    SELECT Tag.tag
    FROM Tag
    JOIN PostHasTag ON Tag.id_tag = PostHasTag.id_tag
    WHERE PostHasTag.id_freePost = %s
    """
    database.cursor.execute(query, (post_id,))
    tags = database.cursor.fetchall()
    return [tag[0] for tag in tags]

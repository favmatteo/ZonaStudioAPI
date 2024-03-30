from lib.app import database
from databases.school_address_db import get_id_by_school_address


def is_username_not_used(username: str) -> bool:
    query = f"""
    SELECT COUNT(*) FROM Student WHERE username = '{username}'
    """
    database.execute(query)
    result1 = database.fetch_one()
    query = f"""
    SELECT COUNT(*) FROM Helper WHERE username = '{username}'
    """
    database.execute(query)
    result2 = database.fetch_one()
    return result1[0] != 0 and result2[0] != 0
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
    return result1[0] != 0 or result2[0] != 0


def get_name_by_uid(uid: str) -> str:
    query_student = f"""
    SELECT name, surname FROM Student WHERE id_student = '{uid}'
    """
    database.execute(query_student)
    result_student = database.fetch_one()

    query_helper = f"""
    SELECT name, surname FROM Helper WHERE id_helper = '{uid}'
    """
    database.execute(query_helper)
    result_helper = database.fetch_one()

    if result_student:
        return " ".join(result_student)
    elif result_helper:
        return " ".join(result_helper)
    else:
        return None

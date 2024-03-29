from lib.app import database
from databases.school_address_db import get_id_by_school_address


def is_username_not_used(username: str) -> bool:
    query = f"""
    SELECT COUNT(*) FROM Student WHERE username = '{username}'
    """
    database.execute(query)
    result = database.fetch_one()
    return result[0] != 0


def create_new_student(
    id_student: str,
    name: str,
    surname: str,
    username: str,
    age: int,
    school_class: int,
    school_address: str,
):
    school_address_id = get_id_by_school_address(school_address=school_address)
    query = f"""
    INSERT INTO Student (id_student, name, surname, username, age, eur, diamonds, class, id_schoolAddress)
    VALUES ('{id_student}', '{name}', '{surname}', '{username}', {age}, 0, 0, {school_class}, {school_address_id})
    """
    database.execute(query)


def delete_student_by_id(id_student: str):
    query = f"DELETE FROM Student WHERE id_student = '{id_student}'"
    database.execute(query)


def update_student_info(id_student: str, field: str, data: str):
    if data.isdigit():
        query = f"UPDATE Student SET {field} = {data} WHERE id_student = '{id_student}'"
    else:
        query = (
            f"UPDATE Student SET {field} = '{data}' WHERE id_student = '{id_student}'"
        )
    database.execute(query)

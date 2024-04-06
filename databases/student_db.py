from lib.app import database
from databases.school_address_db import get_id_by_school_address


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
    query = """
    INSERT INTO Student (id_student, name, surname, username, age, eur, diamonds, class, id_schoolAddress)
    VALUES (%s, %s, %s, %s, %s, 0, 0, %s, %s)
    """
    database.cursor.execute(
        query,
        (
            id_student,
            name,
            surname,
            username,
            age,
            school_class,
            school_address_id,
        ),
    )
    database.conn.commit()


def delete_student_by_id(id_student: str):
    query = "DELETE FROM Student WHERE id_student = %s"
    database.cursor.execute(query, (id_student,))
    database.conn.commit()


def update_student_info(id_student: str, field: str, data: str):
    if data.isdigit():
        query = f"UPDATE Student SET {field} = %s WHERE id_student = %s"
    else:
        query = f"UPDATE Student SET {field} = %s WHERE id_student = %s"
    database.cursor.execute(query, (data, id_student))
    database.conn.commit()

from lib.app import database


def create_new_student(
    id_student: str,
    name: str,
    surname: str,
    username: str,
    age: int,
):
    query = f"""
    INSERT INTO Student (id_student, name, surname, username, age, eur, diamonds)
    VALUES ('{id_student}', '{name}', '{surname}', '{username}', {age}, 0, 0)
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

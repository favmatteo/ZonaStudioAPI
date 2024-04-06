from lib.app import database
from databases.school_address_db import get_id_by_school_address
from schemas.helper import EducationalLevel


def create_new_helper(
    id_student: str,
    name: str,
    surname: str,
    username: str,
    age: int,
    school_class: int,
    school_address: str,
    educational_level: EducationalLevel,
):
    if school_address == None:
        school_address_id = "null"
    else:
        school_address_id = get_id_by_school_address(school_address=school_address)
    if school_class == None:
        school_class = "null"
    query = """
    INSERT INTO Helper (id_helper, name, surname, username, age, eur, diamonds, class, id_schoolAddress, educationalLevel)
    VALUES (%s, %s, %s, %s, %s, 0, 0, %s, %s, %s)
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
            educational_level.value,
        ),
    )
    database.conn.commit()


def is_user_a_helper(uid: str) -> bool:
    query = """
    SELECT COUNT(*) FROM Helper WHERE id_helper = %s
    """
    database.cursor.execute(query, (uid,))
    database.conn.commit()
    result = database.fetch_one()
    return result[0] == 1

from lib.app import database


def get_all_school_address() -> list:
    database.execute("SELECT SchoolAddress FROM SchoolAddress")
    return [i[0] for i in database.get_content()]


def get_id_by_school_address(school_address) -> int:
    query = "SELECT id_schoolAddress FROM SchoolAddress WHERE SchoolAddress = %s"
    database.cursor.execute(query, (school_address,))
    result = database.cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

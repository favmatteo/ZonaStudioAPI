from lib.app import database


def get_all_school_address() -> list:
    database.execute("SELECT SchoolAddress FROM SchoolAddress")
    return [i[0] for i in database.get_content()]


def get_id_by_school_address(school_address) -> int:
    database.execute(
        f"SELECT id_schoolAddress FROM SchoolAddress WHERE SchoolAddress = '{school_address}'"
    )
    return database.get_content()[0][0]

from lib.app import database


def get_all_school_address():
    database.execute("SELECT SchoolAddress FROM SchoolAddress")
    return [i[0] for i in database.get_content()]


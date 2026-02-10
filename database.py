import copy
import sqlite3

conn = sqlite3.connect(f"datadir/quizzdata.db")
cursor = conn.cursor()


def initialise_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS quizzes (id INTEGER, content TEXT,answer TEXT)")


def deinitialise_database():
    conn.close()


def get_guizzlist():
    cursor.execute("SELECT * FROM quizzes")
    quizzlist = cursor.fetchall()
    return quizzlist


def get_quizz(id, quizzlist):
    for quizz in quizzlist:
        if quizz[0] == id:
            return quizz
    return "No ID found"


def add_quizz(quizzlist, content, answer):
    new_id = len(quizzlist) + 1
    quizzlist.append((new_id, content, answer))
    return quizzlist


def modify_quizz(quizzlist, id, content, answer):
    try:
        if id <= len(quizzlist):
            quizzlist[id - 1] = (id, content, answer)
    except IndexError:
        pass
    return quizzlist


def save_quizzdata(quizzlist, presave_list):
    id_index = []
    for entry in presave_list:
        id_index.append(entry[0])
    for quizz in quizzlist:
        if quizz[0] in id_index:
            cursor.execute(
                "UPDATE quizzes SET content = ?, answer = ? WHERE id = ?",
                (quizz[1], quizz[2], quizz[0])
            )
        else:
            cursor.execute(
                "INSERT INTO quizzes (id, content, answer) VALUES (?, ?, ?)",
                (quizz[0], quizz[1], quizz[2])
            )
    conn.commit()


## test block
#
# initialise_database()
#
# presave_list = get_guizzlist()
# print(presave_list)
# quizzlist = copy.deepcopy(presave_list)
# print(quizzlist)
# modify_quizz(quizzlist, 1, "3", "test")
# add_quizz(quizzlist, "B", "C")
# print(quizzlist)
# save_quizzdata(quizzlist, presave_list)
# overview = get_guizzlist()
# print(overview)
#
# deinitialise_database()

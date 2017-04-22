
def main():
    import sqlite3
    connection = sqlite3.connect("tq_database.db")
    cursor = connection.cursor()
    cardno="CU151099100"

    cmd ="insert into CU1510991002(Timing,Bill) values(datetime(CURRENT_TIMESTAMP, 'localtime') ,500)"
    cursor.execute(cmd)
    connection.commit()
main()
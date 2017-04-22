def main():
    import sqlite3
    connection=sqlite3.connect("tq_items.db")
    cursor=connection.cursor()
    cursor.execute("SELECT name,price FROM cart")
    data=cursor.fetchall()
    print(data)
    cursor.close()
    connection.close()
main()
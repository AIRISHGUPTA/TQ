class DatabaseUtility:
    def __init__(self):
        import sqlite3
        self.connection = sqlite3.connect("tq_database.db")
        self.cursor = self.connection.cursor()

    def get_table(self, cardno):
        cmd = "select Timing,cast(bill as varchar(10)) from " + cardno + ";"
        print(cmd)
        self.cursor.execute(cmd)
        data = self.cursor.fetchall()
        return data
    def get_register(self):
        cmd="select name_person,phoneno,cardno,cast(cash as varchar2(10)) from register"
        self.cursor.execute(cmd)
        data = self.cursor.fetchall()
        return data
    def get_columns(self):
        columns = ['SNO', 'TIMING', 'BILL']
        return columns

    def create_table(self, label1, label2, label3):
        cmd = "create table if not exists register(name_person varchar2(20),phoneno varchar2(20),cardno varchar2(20),cash int)"
        self.cursor.execute(cmd)
        label3='CU'+label3
        cmd = "insert into register(name_person,phoneno,cardno,cash) values('" + label1 + "','" + label2 + "','" + label3 + "',0)"
        self.cursor.execute(cmd)
        cmd = "create table if not exists " + str(label3) + "(Timing datetime,Bill int)"
        print(cmd)
        self.cursor.execute(cmd)
        self.connection.commit()

    def check_validity(self, text):
        cmd = "select * from register where cardno='" + text + "'"
        self.cursor.execute(cmd)
        data = self.cursor.fetchall()
        if not data:
            return 0
        else:
            return 1

    def get_name(self, cardno):
        cmd = "select name_person,cast(cash as varchar(20)) from register where cardno='" + cardno + "'"
        self.cursor.execute(cmd)
        data = self.cursor.fetchall()
        if data:
            return data
        else:
            return 0

    def add_cash(self,cash,cardno):
        cmd="update register set cash=cash+"+cash+" where cardno='" + cardno + "'"
        self.cursor.execute(cmd)
        self.connection.commit()
    def check_cash(self,bill,cardno):
        cmd="select cash from register where cardno='"+cardno+"';"
        self.cursor.execute(cmd)
        data=self.cursor.fetchall()
        if(data[0][0]-bill>0):
            cmd="update register set cash='"+str(data[0][0]-bill)+"' where cardno='"+cardno+"';"
            self.cursor.execute(cmd)
            self.connection.commit()
            cmd = "insert into " + cardno + "(Timing,Bill) values(datetime(CURRENT_TIMESTAMP, 'localtime') ," + str(bill) + ")"
            self.cursor.execute(cmd)
            self.connection.commit()
            return 1
        else:
            return 0

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

class order:
    def __init__(self):
        import sqlite3
        self.connection1 = sqlite3.connect("tq_items.db")
        self.cursor1 = self.connection1.cursor()
    def check_validity(self,text):
        cmd="select name,cast(price as varchar2(10)) from items where name='"+text+"';"
        self.cursor1.execute(cmd)
        data=self.cursor1.fetchall()
        if not data:
            return 0
        else:
            return 1
    def cart(self,text,qty):
        cmd="create table if not exists cart(name varchar2(20),price int)"
        self.cursor1.execute(cmd)
        cmd="select name,price*"+qty+" from items where name='"+text+"'"
        self.cursor1.execute(cmd)
        data=self.cursor1.fetchall()
        cmd = "insert into cart(name,price) values('" + str(data[0][0]) + "'," + str(data[0][1]) + ");"
        self.cursor1.execute(cmd)
        self.connection1.commit()

    def get_cart(self):
        cmd = "select name,cast(price as varchar2(20)) from cart;"
        self.cursor1.execute(cmd)
        data1 = self.cursor1.fetchall()
        return data1

    def remove(self,text):
        cmd="delete from cart where name='"+text+"'"
        self.cursor1.execute(cmd)
        self.connection1.commit()
    def bill(self):
        cmd="select sum(price) from cart"
        self.cursor1.execute(cmd)
        data=self.cursor1.fetchall()
        return (data[0][0])
    def drop(self):
        cmd="drop table cart"
        self.cursor1.execute(cmd)
        self.connection1.commit()
    def disconnect(self):
        self.cursor1.close()
        self.connection1.close()
if __name__ == '__main__':
    a = DatabaseUtility()
    a.create_table('AIRU', '-9324834', 'a98')

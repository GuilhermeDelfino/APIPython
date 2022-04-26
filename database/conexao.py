import mysql.connector
class Connection:
    
    def __init__(self, user: str = 'root', password: str = '1234', database='Agenda') -> None:
        self.mydb = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database=database
        )
        
    def getConnection(self) -> mysql.connector.MySQLConnection:
        return self.mydb
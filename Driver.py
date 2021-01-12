from Token_Sql import Token_Sql
from Sql_File import Sql_File


class Driver:
    def __init__(self,uml,db):
        self._token_sql = Token_Sql(uml,db)
        self._token_sql.parse()
        self._output = Sql_File(db)
        
def main():
    d = Driver('text.pu','database.db')

    
if __name__ == "__main__":
    main()

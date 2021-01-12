import sqlite3

class Sql_File:
    def __init__(self,db_name):
        self._con = sqlite3.connect(db_name)
        self._cursor = self._con.cursor()
        self._class = []
        self._list = []
        self.create_file()
        self.class_decleartion()
        self.class_attribute()
        
    def create_file(self):
        quary = "SELECT class_name FROM class"
        self._cursor.execute(quary)
        row = self._cursor.fetchall()
        for i in row:
            self._list.append(i[0])
        try:
            for r in row:
                for i in r:
                    f = open(i+".java","a")
                    self._class.append(f)
        except:
            pass
            quary = "SELECT class_name FROM class"
        
    def class_decleartion(self):
        quary = "SELECT class_name FROM class"
        self._cursor.execute(quary)
        list = []
        for i in self._cursor.fetchall():
            list.append(i[0])
            
        quary = "SELECT class_1,class_2 FROM relation WHERE relation = 'inheritance'"
        self._cursor.execute(quary)
        rel = self._cursor.fetchall()
        
        for i in range(len(self._class)):
            if(len(rel) > 0 and rel[0][1] == list[i]):
                    self._class[i].write('public class '+ list[i] + ' extends ' +rel[0][0]+'\n')
            else:
                self._class[i].write('public class '+ list[i] + '\n')
            self._class[i].write('{\n')
            
    
    def class_attribute(self):
        count = 0
        for i in self._list:
            quary = "SELECT * FROM "+i+"_attribute"
            self._cursor.execute(quary)
            data = self._cursor.fetchall()
            
            
            if (len(data) != 0):
                for d in data :
                    self._class[count].write( '\t'+d[2]+' '+d[5]+' '+d[1])
                    if (d[4] == 'variable'):
                        self._class[count].write(';\n')
                    elif (d[4] == 'method' or d[4] == 'constructor'):
                        self._class[count].write(' ('+d[6][0:len(d[6])-1]+'){};\n')
                    self._class[count].write('\n')
                
            self._class[count].write('}\n')
            self._class[count].close()
            count += 1
        
            
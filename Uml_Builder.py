import sqlite3

class Uml_Builder:
    
    def __init__(self,db_name):
        self._con = sqlite3.connect(db_name)
        self.create_access_table()
        self.create_data_type_table()
        self.create_class_type()
        self.create_class_table()
        self.create_relation_table()
        self.create_relation_type()
    
    def create_access_table(self):
        cursor = self._con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS access
                        (access_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        access_name varchar(20))''')
        cursor.execute("INSERT INTO access(access_name) VALUES ('private')")
        cursor.execute("INSERT INTO access(access_name) VALUES ('public')")
        cursor.execute("INSERT INTO access(access_name) VALUES ('protected')")
        self._con.commit()
        
    def create_data_type_table(self):
        cursor = self._con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS data_type
                        (data_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        data_type_name varchar(225) UNIQUE)''')   
        self.add_data_type("char")
        self.add_data_type("int")
        self.add_data_type("float")
        self.add_data_type("double")
        self.add_data_type("bool")
        self.add_data_type("void")
        self.add_data_type("string")
        self._con.commit()

    def add_data_type(self,name):
        cursor = self._con.cursor()
        cursor.execute("INSERT INTO data_type(data_type_name) VALUES ('"+name+"')")
        self._con.commit()
    
    def create_class_type(self):
        cursor = self._con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS class_type
                        (class_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        class_type_name varchar(20))''')
        
        cursor.execute("INSERT INTO class_type(class_type_name) VALUES ('class')")
        cursor.execute("INSERT INTO class_type(class_type_name) VALUES ('interface')")
        cursor.execute("INSERT INTO class_type(class_type_name) VALUES ('abstract')")
        cursor.execute("INSERT INTO class_type(class_type_name) VALUES ('enum')")
        self._con.commit()
        
    def create_class_table(self):
        cursor = self._con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS class
                        (class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        class_name VARCHAR(20) UNIQUE,
                        class_type VARCHAR(20) DEFAULT class NOT NULL,
                        template VARCHAR(20),
                        UNIQUE(class_id , class_name))
                        ''')
        self._con.commit()
    
    def create_relation_type(self):
        cursor = self._con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS relation_type
                        (relation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        relation_name varchar(20))''')
        self.add_relation_type('inheriance')
        self.add_relation_type('composition')
        self.add_relation_type('aggregation')
        self.add_relation_type('association')
        self._con.commit()
        
    def add_relation_type(self,name):
        cursor = self._con.cursor()
        cursor.execute("INSERT INTO relation_type(relation_name) VALUES ('"+name+"')")
        self._con.commit()
                        
    def create_relation_table(self):
        cursor = self._con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS relation
                        (relation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        class_1 VARCHAR(20), 
                        relation VARCHAR(20),
                        class_2 VARCHAR(20))
                        ''')
        self._con.commit()
    
    def insert_to_relation(self,entities):
        cursor = self._con.cursor()
        cursor.execute('''INSERT INTO relation
                        (class_1,relation,class_2) 
                            VALUES(?, ?, ?)''', entities)
        self._con.commit()

    def insert_to_class_table(self,entities):
        cursor = self._con.cursor()
        cursor.execute('''INSERT INTO class(class_name, class_type, template) 
                            VALUES(?, ?, ?)''', entities)
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS '''+entities[0]+'''_attribute
                        (attribute_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        attribute_name VARCHAR(20),
                        attribute_acess VARCHAR(20) DEFAULT public NOT NULL,
                        class_name  VARCHAR(20) DEFAULT ''' + entities[0] + '''NOT NULL,
                        attribute_type varchar(225) DEFAULT variable NOT NULL,
                        return_type varchar(225) DEFAULT void NOT NULL)''')
                        
        self._con.commit()
    
    def insert_class_name_class_table(self,name):
        cursor = self._con.cursor()
        cursor.execute("INSERT INTO class(class_name) VALUES('"+name+"')")
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS '''+name+'''_attribute
                        (attribute_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        attribute_name VARCHAR(20),
                        attribute_acess VARCHAR(20) DEFAULT public NOT NULL,
                        class_name  VARCHAR(20) DEFAULT ''' + name + '''NOT NULL,
                        attribute_type varchar(225) DEFAULT variable NOT NULL,
                        return_type varchar(225) DEFAULT void NOT NULL,
                        parameter varchar(225))''')
        self._con.commit()
        
    def insert_class_type_class_table(self,class_name,col,val):
        if (col == 'class_name'):
            return
           
        cursor = self._con.cursor()
        cursor.execute("UPDATE class SET "+col+" = '"+ str(val) +"' WHERE class_name = '"+class_name+"'")
        self._con.commit()
    
    
    def insert_to_attribute(self,entities):
        cursor = self._con.cursor()
        cursor.execute('''INSERT INTO '''+entities[2]+'''_attribute
                        (attribute_name, attribute_acess, class_name,attribute_type,return_type,parameter ) 
                            VALUES(?, ?, ?, ?, ?,?)''', entities)
        self._con.commit()
    
    def inset_attribute_type(self,class_name,col,val):
        cursor = self._con.cursor()
        if (col == 'class_name'):
            return
        if (col == 'attribute_name'):
            cursor.execute("INSERT INTO "+class_name+"_attribute (attribute_name, class_name)  VALUES('"+val+"','"+class_name+"' )")
        else:
            cursor.execute("UPDATE "+class_name+"_attribute SET "+col+" = '"+ str(val) +"' WHERE attribute_id = (SELECT MAX(attribute_id) FROM "+class_name+"_attribute)")
        self._con.commit()

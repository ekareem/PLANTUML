from Uml_Builder import Uml_Builder
from File_Parser import File_Parser
from Astream import Astream

class Token_Sql:
    
    def __init__(self,file_name,db_name):
        self._reader = File_Parser(file_name)
        self._data = Uml_Builder(db_name)
        
        self._token = ['{','}','(',')','<','>','+','-','#',':','|','^','"','*--','<|--','--','o--','<<','>>']
        self._class_type = ['class','interface','abstract','enum']
        self._access = ['#','-','+']
        self._data_type = ['char','int','float','double','bool','void','string','boolean']
        
        self._class_created = False 
        self._class_name = ''
        self._attribute_name = ''
        self._class_body = False
        self._method_parameter = False
        self._parameter = ''
        
        self._tokenizer = self._reader.read()
        self._stream = Astream(self._tokenizer)
        
    def parse(self):
        while(self._stream.curr() != 'eoa'):
            self._stream.next()
            if(self._stream.curr() != 'eoa'):
            
                if(self._stream.curr() == 'class'):
                    self.token_class()
                    
                elif(self._stream.curr() == '{'):
                    self.token_body()
                    
                elif(self._stream.curr() == '}'):
                    self.token_body()
                    
                elif(self._stream.curr() in self._access):
                    self.token_class_acess()
                    
                elif(self._stream.curr() == ':'):
                    self.token_data_type()
                    
                elif(self._stream.curr() == '<<'):
                    self.token_class_type()
                
                elif(self._stream.curr() == '>>'):
                    pass
                
                elif(self._stream.curr() == '<'):
                    self.token_class_template()
                
                elif(self._stream.curr() == '>'):
                    pass
                    
                elif(self._stream.curr() == '('):
                    self.token_parameter()
                
                elif(self._stream.curr() == ')'):
                    self.token_parameter()
                    
                elif(self._stream.curr() == '*--'):
                    self.token_relation()
                
                elif(self._stream.curr() == '<|--'):
                    self.token_relation()
                
                elif(self._stream.curr() == '--'):
                    self.token_relation()
                
                elif(self._stream.curr() == 'o--'):
                    self.token_relation()
                    
    def token_class(self):
    
        if(self._class_name == ''):
            self._stream.next()
            if (self._stream.curr() not in self._token and self._stream.curr() != 'eof'):
                self._class_name = self._stream.curr()
                try:
                    self._data.insert_class_name_class_table(self._stream.curr())
                except:
                        print('class name already exist')
            
    def token_class_type(self):
        self._stream.next()
        if (self._stream.curr() not in self._token and self._stream.curr() != 'eof'):
            if (self._stream.curr() in self._class_type):
                try:
                    self._data.insert_class_type_class_table(self._class_name,'class_type',self._stream.curr())
                except:
                    print('class name already exist')
    
    def token_class_template(self):
        self._stream.next()
        if (self._stream.curr() not in self._token and self._stream.curr() != 'eof'):
            try:
                self._data.insert_class_type_class_table(self._class_name,'template',self._stream.curr())
            except:
                print('class name already exist')
        
    def token_class_acess(self):
        access = 'public'
        if (self._stream.curr() == '#'):
            access = 'protected'
        if (self._stream.curr() == '-'):
            access = 'private'
            
        self._stream.next()    
        if (self._stream.curr() not in self._token and self._stream.curr() != 'eof'):
            self._attribute_name = self._stream.curr()
            self._data.inset_attribute_type(self._class_name,'attribute_name',self._attribute_name)
            self._data.inset_attribute_type(self._class_name,'attribute_acess',access)
        
    def token_data_type(self):
        
        #try:
            if (self._method_parameter == False):
                self._stream.next()    
                if (self._stream.curr() not in self._token and self._stream.curr() != 'eof'):
                    if (self._stream.curr() not in self._data_type):
                        self._data_type.append(self._stream.curr())
                        self._data.add_data_type(self._stream.curr())
                      
                    self._data.inset_attribute_type(self._class_name,'return_type',self._stream.curr())
            else:
                if (self._stream.peek_next(1) not in self._data_type):
                    self._data_type.append(self._stream.peek_next(1))
                    self._data.add_data_type(self._stream.peek_next(1))
                    
                self._parameter += self._stream.peek_next(1)+' '+self._stream.peek_prev(1)+','
                
        #except:
         #   print(self._stream.curr() + " already exist ")
        
    def token_parameter(self):
        if (self._stream.curr() == '('):
            self._data.inset_attribute_type(self._class_name,'attribute_type','method')
            self._method_parameter = True
            if(self._stream.peek_prev(1) == self._class_name):
                self._data.inset_attribute_type(self._class_name,'attribute_type','constructor')
            
        if (self._stream.curr() == ')'):
            self._data.inset_attribute_type(self._class_name,'parameter',self._parameter)
            self._parameter = ''
            self._method_parameter = False
        
    def token_body(self):
        if (self._stream.curr() == '{'):
            self._class_body = True
            
        if (self._stream.curr() == '}'):
            self._class_name = ''
            self._class_body = False
            
    def token_relation(self):
        relation = ''
        if(self._stream.curr() == '*--'):
            relation = 'composition'
        elif(self._stream.curr() == '<|--'):
            relation = 'inheritance'
        elif(self._stream.curr() == '--'):
            relation = 'association'
        elif(self._stream.curr() == 'o--'):
            relation = 'aggregation'
            
        entity = []
        entity.append(self._stream.peek_prev(1))
        entity.append(relation)
        entity.append(self._stream.peek_next(1))
        
        self._data.insert_to_relation(entity)
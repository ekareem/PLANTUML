class Input_Stream:

    def __init__(self):
        #liat of oparator_token
        self._oparator = [' ','{','}','(',')','<','>','+','-','#',':','|','^','"',]
        self._large_oparator = ['*--','<|--','--','o--','<|..','-->','..>','..|>','<--*','<<','>>']
    
    def tokenize(self,input):
        #param[in]      string      input string to be tokenize
        tokenizer = []   
        
        for i in range(len(input)):
            
            #appends each token at the end of the list
            if(input[i] in self._oparator or i == len(input) -1):
                self.append_tokenizer(tokenizer,self.find_token(tokenizer,input,i))
        
        self.shrink_large_oparator(tokenizer)
        
        return tokenizer
    
    def find_token(self,tokenizer,input,index):
        #purpose: finds token stating form a spcified index to tthe next token backwards
        #param[in]:     string      input string to be tokenize
        #param[in]:     index       index to statt form 
        token = ""
        
        i = index
        
        #if is not last index
        if(input[index] in self._oparator):
            i = index - 1
        
        #builds token
        while (i != -1 and input[i] not in self._oparator):
            token = input[i] + token
            i -= 1
        
        #appends index token if part of _token`
        if (input[index] != ' ' and input[index] in self._oparator):
            self.append_tokenizer(tokenizer,token)
            return input[index]
            
        return token
    
    def append_tokenizer(self,tokenizer,token):
        #purpose appends token to tokenizer
        #param[in]  tokenizer list of tokens
        #param[in] token to be inseted to tokenizer
        if(token == ''):
            return False
        tokenizer.append(token)
        return True
        
    def is_sub_array(self,A, B): 
        #purpose: chcks if b is a sub arry of abs
        #param[in]  list A  list
        #param[out] list B
        index = 0
        
        while (index+len(B) < len(A) + 1):
            if (A[index: index+len(B)] == B):
                return [True,index]
            index +=1
            
        return [False,0]
        
    def shrink_large_oparator(self,tokenizer):
        #shrigs lasrge oparager from multiple array index to one index
        #param[in]  list    to be shrunl
        for i in range(len(self._large_oparator)):
            output = self.is_sub_array(tokenizer, list(self._large_oparator[i]))
            
            if(output[0] == True):
                    del tokenizer[output[1] : output[1] + len(self._large_oparator[i])]
                    tokenizer.insert(output[1],self._large_oparator[i])
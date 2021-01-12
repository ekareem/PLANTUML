
class Astream:
    
    def __init__(self,tokenizer):
        self._tokenizer = self.init(tokenizer)
        self._curr = 0
        self._end = len(self._tokenizer)
        
    def init(self,tokenizer):
        list = []
        for i in tokenizer:
            for j in i:
                list.append(j)
        list.append('eoa')
        return list
        
        
    def curr(self):
        return self._tokenizer[self._curr] 
        
    def next(self):
        self._curr += 1
        if(self._curr != self._end):
            return self.curr()
        self._curr -= 1
        return None
        
    def peek_next(self,index):
        if(self._curr + index != self._end):
            return  self._tokenizer[self._curr + index]
        return None
        
    def prev(self):
        self._curr -= 1
        if(self._curr >= 0):
            return self.curr()
        self._curr += 1
        return None
        
    def peek_prev(self,index):
        if(self._curr - index >= 0):
            return self._tokenizer[self._curr - index]
        return None
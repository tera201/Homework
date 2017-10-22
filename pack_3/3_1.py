class voc:
    def ToF(self,n):
        a=[]
        brack = {"(": ")", "{": "}", "[": "]"}
        for i in n:
            if i in brack:
                a.append(i)
            elif len(a)==0 or brack[a.pop()]!=i:
                return False
        return True
a=input()
print(voc().ToF(a))
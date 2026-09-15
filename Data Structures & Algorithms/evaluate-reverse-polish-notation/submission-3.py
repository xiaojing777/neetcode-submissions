class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for char in tokens:
            if char in ["+", "-", "*", "/"]:
                last1 = s.pop()
                last2 = s.pop()
                if char=="+":
                    s.append(last1+last2)
                elif char=="-":
                    s.append(last2-last1)
                elif char=="*":
                    s.append(last1*last2)
                elif char=="/":
                    s.append(int(last2/last1))
            else:
                s.append(int(char))
        
        return s.pop()
            

        
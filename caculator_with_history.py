#calculator with history
class Calculator:
    def __init__(self):
        self.history=[]
    def calculate(self,a,b,op):
        if op=="+":
            res=a+b
        elif op=="-":
            res=a-b
        elif op=="*":
            res=a*b
        elif op=="/":
            if b==0:
                return "Cannot divide by zero"
            res=a/b
        else:
            return "Invalid operator"

        record=f"{a} {op} {b}={res}"
        self.history.append(record)
        return res
    def get_history(self):
        return self.history
if __name__=="__main__":
    calc=Calculator()
    print(calc.calculate(10,5,"+"))
    print(calc.calculate(20,4,"/"))
    print("History:",calc.get_history())

class MathDojo(object):
    def __init__ (self):
        self.result = 0

    def add(self, *nums): # (1,2,[3,4],5)
        for i in nums:
            if isinstance(i, int):
                self.result += i
            else: # [3,4]
                for data in i:
                    self.result += data # 1+2+3+4+5 
            print "Sum from addition:", self.result
        return self

    def subtract(self, *nums):
        for i in nums:
            if isinstance(i, int):
                self.result -= i
            else: # [3,4]
                for data in i:
                    self.result -= data # 1+2+3+4+5 
            print "Sum from subtraction:", self.result
        return self

md = MathDojo()
md.add(2,5).add(2,[2,3]).subtract(3,2) # should perform 0+2+(2+5)-(3+2) and return 4.
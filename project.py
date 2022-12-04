# Multiplication Table Project Using OOPS concepts 

class multiplication:
    def table(self):
        self.n=int(input("Enter number of tables : "))        

    def display(self):
        for x in range(1,self.n):

            for i in range(1,11):
                print(self.n ,"X",i, "=",self.n*i)
            print()
            self.n=self.n-1


p1=multiplication()
p1.table()
p1.display() 
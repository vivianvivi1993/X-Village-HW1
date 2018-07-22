class Matrix():
    def __init__(self,cols,rows):          
        self.cols=cols
        self.rows=rows     
    def see(self,cols,rows):
        self.a=[]
        self.b=[]
        import random
        self.rows=int(input("Enter A matrix's rows:"))
        self.cols=int(input("Enter A matrix's cols:"))
        for i in range(0,self.cols):   
            self.a.append([])
            self.b.append([])
            for j in range(0,self.rows):
                self.a[i].append(random.randint(0,9))
                self.b[i].append(random.randint(0,9))
        for i in self.a:
            for j in i:
                print(j,end=" ")
            print()
        print("====================================")
        self.rows=int(input("Enter B matrix's rows:"))
        self.cols=int(input("Enter B matrix's cols:"))
        print("Matrix A",(self.rows,self.cols))
        for i in self.b:
            for j in i:
                print(j,end=" ")
            print()
        print("==================A+B===================")       
    def jia(self,cols,rows):
        self.c=[]
        for i in range(0,self.cols):  
            self.c.append([])
            for j in range(self.rows):
                self.c[i].append(self.a[i][j]+self.b[i][j])
        for i in self.c:
            for j in i:
                print(j,end=" ")
            print()
        print("==================A-B==================")
    def jian(self,cols,rows):
        self.d=[]
        for i in range(0,self.cols):  
            self.d.append([])
            for j in range(0,self.rows):
                self.d[i].append(self.a[i][j]-self.b[i][j])
        for i in self.d:
            for j in i:
                print(j,end=" ")
            print()
        print("==================A*B==================")
    def cheng(self,cols,rows):
        self.e=[]
        self.ee=[]
        for i in range(0,self.cols):
            self.e.append([]) 
            for j in range(0,self.rows):
                self.e[i].append(self.a[i][j]*self.b[j][i])
                 
        for i in self.e:
            for j in i:
                print(j,end=" ")
            print()
        print("===========the transpose of A*B===========")

    def zhuanzhi(self,cols,rows):
        self.g=[]
        for i in range(0,self.cols):  
            self.g.append([])
            for j in range(0,self.rows):
                self.g[i].append(self.a[j][i])
        for i in self.g:
            for j in i:
                print(j,end=" ")
            print()    

A=Matrix(3,3)
A.see(3,3)
A.jia(3,3)
A.jian(3,3)
A.cheng(3,3)
A.zhuanzhi(3,3)

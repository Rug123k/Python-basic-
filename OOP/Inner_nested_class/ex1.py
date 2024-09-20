class customer:
    def __init__(self,id,name,bdno,bcity,bcounty,sdno,scity,scounty):
        self.cusid=id
        self.name=name
        self.baddr= self.Address(bdno,bcity,bcounty)                        #bddr= biling address
        self.saddr= self.Address(sdno,scity,scounty)                        #sddr = shiping addres
        
    class Address:
        def __init__(self,dno,city,county ):
            self.dno=dno
            self.city=city
            self.county=county
        def display(self):
            print(self.dno)
            print(self.city)
            print(self.county)
a=customer(12,"abc",13,"Mum","ind",14,"pune","ind")
a.saddr.display()
a.baddr.display()
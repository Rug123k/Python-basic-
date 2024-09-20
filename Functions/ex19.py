# Find planet name by id
def idnum(id):
    planet={1:"Mercury",2:"Venus",3:"Earth",4:"jupiter"}
    return planet[id]
id=int(input("Enter "))
p=idnum(id)
print("planet is",p)
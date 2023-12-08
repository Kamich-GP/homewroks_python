class Car:
   def __init__(self,model,color,year):
       self.model=model
       self.color=color
       self.year=year

Bentley=Car("Bentley","Blue",2018)
Koenigsegg= Car("Koenigsegg CC","White",2002)
print(Bentley.model)
print(Koenigsegg.model,Koenigsegg.color,Koenigsegg.year)


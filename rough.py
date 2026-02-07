class ParentClass:
	id = 123
	def __init__(self,name,  number):
		self.name = name
		self.number = number
	
class ChildClass(ParentClass):
	cId = 456
	def __init__(self, name):
		self.name = name
		self.parent_id = super().id


pat = ParentClass("Saad", 999999)
chd = ChildClass("Ali")

print(chd.parent_id)
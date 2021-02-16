class harmless:
	def __init__(self, members, group):
		''' Constructor for this class. '''
		# Create some member animals
		self.members = members
		self.group = group

	def printMembers(self):
		print('Printing members of the harmless %s group' % self.group)
		for member in self.members:
			print('\t%s ' % member)

	@classmethod
	def Mammals(cls):
		cl = cls(['Elephant'], "mammals")
		return cl

	@classmethod
	def Birds(cls):
		cl = cls(['Sparrow', 'Robin', 'Duck'], "birds")
		return cl

	@classmethod
	def Fish(cls):
		cl = cls(['Fish', 'Pollock'], "fish")
		return cl

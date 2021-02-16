class dangerous:
	def __init__(self, members, group):
		''' Constructor for this class. '''
		# Create some member animals
		self.members = members
		self.group = group

	def printMembers(self):
		print('Printing members of the dangerous %s group' % self.group)
		for member in self.members:
			print('\t%s ' % member)

	@classmethod
	def Mammals(cls):
		cl = cls(['Tiger', 'Wild Cat'], "mammals")
		return cl

	@classmethod
	def Birds(cls):
		cl = cls(['Eagle', 'Hawk'], "birds")
		return cl

	@classmethod
	def Fish(cls):
		cl = cls(['Shark', 'Tuna'], "fish")
		return cl

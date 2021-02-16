class Fish:
	def __init__(self):
		''' Constructor for this class. '''
		# Create some member animals
		self.members = ['Shark', 'Tuna', 'Cod', 'Pollock']
		self.dangerous = ['Shark', 'Tuna']
		self.harmless = ['Cod', 'Pollock']

	def printMembers(self):
		print('Printing members of the Fish class')
		for member in self.members:
			print('\t%s ' % member)

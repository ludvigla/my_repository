# Import classes from your breand new package
from animals import Mammals
from animals import Birds
from animals import Fish
import animals

# Create an object of Mammals class & call a methods of it
myMammal = Mammals()
myMammal.printMembers()

# Create an object of Birds call a methods of it
myBird = Birds()
myBird.printMembers()

# Create an object of Fish call a methods of it
myFish = Fish()
myFish.printMembers()

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()

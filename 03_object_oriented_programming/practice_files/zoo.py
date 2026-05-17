class Animal():
    def __init__(self,species,voice):
        self.species = species
        self.voice = voice
    def make_sound(self):
        print(f"The {self.species} say {self.voice}")
v1 = Animal("Cat","Meoo")
v2 = Animal("Dog","I dont know😂")

v1.make_sound()
v2.make_sound()
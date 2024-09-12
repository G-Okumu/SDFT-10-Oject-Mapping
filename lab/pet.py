class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []
    
    def __init__(self, name, pet_type, owner = None) -> None:
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        
    @property
    def pet_type(self):
        return self._pet_type
        
        
    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise ValueError('Pet type not found on our system, the pet type must include: {}'.format(','.join(Pet.PET_TYPES)))
        else:
            self._pet_type = value
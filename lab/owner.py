class Owner:
    def __init__(self, name) -> None:
        self.name = name
        
    def returns_all_owner_pets(self):
        from pet import Pet
        return [{'name': pet.name, 'type': pet.pet_type} for pet in Pet.all if pet.owner == self]
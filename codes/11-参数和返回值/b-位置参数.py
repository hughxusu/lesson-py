def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'harry')

# describe_pet(animal_type='dog', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='dog')
#
# describe_pet('dog', pet_name='harry')
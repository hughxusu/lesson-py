def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry')
describe_pet('tom', 'cat')
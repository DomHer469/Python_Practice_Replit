def make_animal_sound(animal):
    animal_sounds = {
        "dog": "Woof! Woof!",
        "cat": "Meow!",
        "cow": "Moo!",
        "pig": "Oink! Oink!",
        "duck": "Quack!",
        "sheep": "Baa!"
    }
    return animal_sounds.get(animal.lower(), "Sorry, I don't know that animal's sound!")

while True:
    animal = input("What animal sound would you like to hear? (or 'quit' to exit): ")
    
    if animal.lower() == 'quit':
        print("Goodbye!")
        break
    
    sound = make_animal_sound(animal)
    print(sound)
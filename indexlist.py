# create list
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

# use index to find duck
duck_index = animals.index('duck')

# insert cobra where duck is but don't delete duck
animals.insert(duck_index,"cobra")


print animals # Observe what prints after the insert operation


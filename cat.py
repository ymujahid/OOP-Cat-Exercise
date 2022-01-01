#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('pet1', 10)
cat2 = Cat('pet2', 15)
cat3 = Cat('pet3', 20)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
  ages = []
  for cat in args:
      ages.append(cat.age)
  return max(ages)




# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat(cat1, cat2, cat3)} years old.')
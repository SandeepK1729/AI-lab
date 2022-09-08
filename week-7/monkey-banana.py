import random 

class Monkey:
    def __init__(self, bananas):
        self.bananas = bananas
    
    def __repr__(self):
        return f"Monkey with {self.bananas} bananas."
    
monkeys = [Monkey(random.randint(0, 50)) for i in range(5)]

print("Random monkeys : ")
print("\n".join(map(str, monkeys)))

print(f"number of bananas ( FIRST MONKEY ) : {monkeys[0].bananas}")

max_monkey = max(monkeys, key = lambda monkey : monkey.bananas)

print(f"Max Monkey : {max_monkey}")
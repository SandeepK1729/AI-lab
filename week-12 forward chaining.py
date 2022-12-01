# forward chaining 

facts = [
    ('frogs', 'green'),
    ('frogs', 'eat flies'),
    ('frogs', 'amphibions'),
    ('eat flies', 'omnivorous'),
    ('ducks', 'white'),
    ('air', 'dense')
]

def check(knowns, facts):
    result = []
    for known in knowns:
        for A, B in facts:
            if known == A and (A, B) not in result:
                result.append((A, B))
                knowns.append(B)
    return result 

print("Result :", check(['frogs', 'ducks'], facts))
# backward chaining 

facts = [
    ('croaks','frog'),
    ('eats flies','frog'),
    ("frog","green"),
    ('chirp','canary'),
    ('sing','canary'),
    ("canary","yellow"),
]


def check(knowns, facts):
    result = []
    for known in knowns:
        for A, B in facts:
            if known == B and (A, B) not in result:
                result.append((A, B))
                knowns.append(A)
    return result 

print("Result :", check(['green',], facts))
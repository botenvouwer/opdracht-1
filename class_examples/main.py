from class_examples.callback import VerkoopSet, Verkoop

barverkoop_records = [
    {
        "id":"123213",
        "product":"balbal",
        "price":34.34
    },
    {
        "id":"456456",
        "product":"etrte",
        "price":5.34
    },
    {
        "id":"54364645",
        "product":"ertert",
        "price":34.5
    },
    {
        "id":"456546456",
        "product":"rtertert",
        "price":6.34
    },
]

verkoopSet = VerkoopSet(barverkoop_records)

def print_verkoop(verkoop: Verkoop):
    print(verkoop)

print("Verkoop Set met walk functie")
verkoopSet.walk_verkoop_set(print_verkoop)

print("Verkoop Set als iterable")
for verkoop in verkoopSet:
    print(verkoop)


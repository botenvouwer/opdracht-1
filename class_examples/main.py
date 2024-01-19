from class_examples.callback import VerkoopSet

barverkoop_records = [
    {
        "id":"123213",
        "product":"balbal",
        "price":34.34
    },
    {
        "id":"123213",
        "product":"balbal",
        "price":34.34
    },
    {
        "id":"123213",
        "product":"balbal",
        "price":34.34
    },
]

verkoopSet = VerkoopSet(barverkoop_records)

verkoopSet.walk_verkoop_set(lambda a: print(a))

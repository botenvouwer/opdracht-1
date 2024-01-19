
class Verkoop:
    def __init__(self, barverkoop_record: dict):
        self.id = barverkoop_record["id"]
        self.product = barverkoop_record["product"]
        self.price = barverkoop_record["price"]

    def __str__(self):
        return f"Verkoop(id={self.id}, product={self.product}, price={self.price})"


class VerkoopSet:

    verkoop_list = []

    def __init__(self, barverkoop_records: list[dict]):
        for barverkoop_record in barverkoop_records:
            verkoop = Verkoop(barverkoop_record)
            self.verkoop_list.append(verkoop)

    def __str__(self):
        return f"CSVReader(file_location={self.file_location}, test={self.test})"

    def walk_verkoop_set(self, callback: callable):
        for verkoop in self.verkoop_list:
            callback(verkoop)

    def __len__(self):
        return len(self.verkoop_list)

    def __iter__(self):
        for verkoop in self.verkoop_list:
            yield verkoop


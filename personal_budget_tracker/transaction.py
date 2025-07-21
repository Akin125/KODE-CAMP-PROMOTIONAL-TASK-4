from datetime import datetime

class Transaction:
    def __init__(self, description, amount, type_, category):
        self.description = description
        self.amount = amount
        self.type = type_
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "type": self.type,
            "category": self.category,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        transaction = cls(
            data["description"],
            data["amount"],
            data["type"],
            data["category"]
        )
        transaction.date = data["date"]
        return transaction

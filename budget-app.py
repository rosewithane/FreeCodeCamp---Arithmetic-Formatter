class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    total = 0
    for item in self.ledger:
      total += item["amount"]
    return total

  def transfer(self, amount, destination_category):
    if self.check_funds(amount):
      transfer_description = "Transfer from " + self.category
      withdraw_description = "Transfer to " + destination_category.category
      self.withdraw(amount, withdraw_description)
      destination_category.deposit(amount, transfer_description)
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount <= self.get_balance():
      return True
    else:
      return False

  def __str__(self):
    ledger_str = f"{self.category.center(30, '*')}\n"
    total = 0
    for entry in self.ledger:
      description = entry["description"][:23].ljust(23)
      amount = "{:.2f}".format(entry["amount"]).rjust(7)[:7]
      ledger_str += f"{description}{amount}\n"
      total += entry["amount"]
    ledger_str += f"Total: {total:.2f}"
    return ledger_str



def create_spend_chart(categories):
    total_withdrawals = {}
    for category in categories:
        total_withdrawals[category.category] = sum(
            transaction["amount"] for transaction in category.ledger if transaction["amount"] < 0
        )

    total_spent = sum(total_withdrawals.values())
    percentages = {category: (withdrawals / total_spent) * 100 for category, withdrawals in total_withdrawals.items()}

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percentage in percentages.values():
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_category_length = max(len(category.category) for category in categories)
    for i in range(max_category_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i != max_category_length - 1:
            chart += "\n"

    return chart

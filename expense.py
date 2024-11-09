
class NonAccomodationExpense():
    FIXED_COSTS_DICT = {
        "groceries": 1200,
        "insurance": 100,
        "internet": 40,
        "car": 200,
        "hobbies": 100,
        "phone": 40,
        "subscriptions": 30,
        "travel": 100,
        "daycare": 600
    }
    VARIABLE_COSTS_DICT = {
        "savings": 0.02,
        "investment": 0.05
    }

    def __init__(self, net_income):
        self.net_income = net_income

        self.fixed_costs: float
        self.variable_costs: float

        self.sum_fixed_costs()
        self.sum_variable_costs()
        self.set_total_costs()

    def sum_fixed_costs(self):
        self.fixed_costs = sum(self.FIXED_COSTS_DICT.values())

    def sum_variable_costs(self):
        self.variable_costs = sum(self.net_income * value for value in self.VARIABLE_COSTS_DICT.values())

    def set_total_costs(self):
        self.total_cost = self.fixed_costs + self.variable_costs

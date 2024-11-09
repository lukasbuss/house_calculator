class LivingSpace():
    def __init__(self, area: float) -> None:
        self.area = area

        self.monthly_total: float
        self.monthly_per_m2: float

    def monthly_cost_per_m2(self):
        self.monthly_cost_per_m2 = self.monthly_total / self.area

class House(LivingSpace):
    VALUE_INCRESE_PER_ANNUM = 0.07

    EFFICIENCY_CLASSES = {
        "A+": 1.5,
        "A": 2,
        "B": 3,
        "C": 4,
        "D": 6,
        "E": 7,
        "F": 9,
        "G": 11,
        "H": 13
    }

    def __init__(self, area: float, price: float, mortgage: float, efficiency_class: str) -> None:
        super().__init__(area)
        self.price = price
        self.mortgage = mortgage
        self.efficiency_class = efficiency_class

        self.set_nebenkosten()
        self.set_total_cost()
        self.monthly_cost_per_m2()

    def set_nebenkosten(self):
        costs = {"energy_per_month": (self.area * self.EFFICIENCY_CLASSES[self.efficiency_class]) / 12,
        "property_tax": 40,
        "street_cleaning": 25,
        "water": 42,
        "heater_maintenance": 33,
        "electricity": 100,
        "ensurance": 50,
        "chimney_sweep": 8
        }

        self.nebenkosten = sum(costs.values())

    def set_total_cost(self):
        self.monthly_total = self.mortgage + self.nebenkosten

    def set_bank_payment(self):
        pass


class Apartment(LivingSpace):
    RENT_INCREASE_PER_ANNUM = 0.07

    def __init__(self, area: float, rent: float, nebenkosten_in_rent: float) -> None:
        super().__init__(area)
        self.rent = rent
        self.nebenkosten_in_rent = nebenkosten_in_rent

        self.set_nebenkosten()
        self.set_total_cost()
        self.monthly_cost_per_m2()

    def set_nebenkosten(self):
        costs = {
            "electricity": 70,
            "heat_and_water": self.nebenkosten_in_rent
        }

        self.nebenkosten = self.rent + sum(costs.values())

    def set_total_cost(self):
        self.monthly_total = self.rent + self.nebenkosten

    
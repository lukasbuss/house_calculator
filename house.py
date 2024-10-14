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

    def __init__(self, area, price: float, realtor_percentage, property_tax, notary, efficiency_class: str) -> None:
        super().__init__(area)
        self.price = price

    def set_nebenkosten(self):
        energy_per_month = (self.area * self.EFFICIENCY_CLASSES[self.efficiency_class]) / 12

    def set_bank_payment(self):
        pass

    def monthly_total_cost(self):
        pass

class Apartment(LivingSpace):
    RENT_INCREASE_PER_ANNUM = 0.07

    def __init__(self, area, rent: float):
        super().__init__(area)
        self.rent = rent

    def set_nebenkosten(self):
        pass


    
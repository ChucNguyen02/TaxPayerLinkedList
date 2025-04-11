class TaxPayer:
    def __init__(self, code, name, income, deduction):
        self.code = code
        self.name = name
        self.income = income
        self.deduction = deduction
        self.tax = self.calculate_tax()

    def calculate_tax(self):
        taxable_income = self.income - self.deduction
        if taxable_income <= 0:
            return 0
        elif taxable_income <= 5000:
            return taxable_income * 0.05
        elif taxable_income <= 10000:
            return (5000 * 0.05) + ((taxable_income - 5000) * 0.10)
        else:
            return (5000 * 0.05) + (5000 * 0.10) + ((taxable_income - 10000) * 0.15)
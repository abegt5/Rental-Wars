import unittest
from landowner import Landowner
from building import Building
from unit import Unit
from city import City 

class Test_landowner(unittest.TestCase):
    def setUp(self):
        print("Set up the test environment.")
        self.building1 = Building(1, 1, 8)
        self.building2 = Building(2, 2, 10)
        self.landowner = Landowner(money=200000, income=5000, patience=12, preference="Agg")

    def test_acquire_building(self):
        print( "Test that a landowner can acquire a building.")
        self.landowner.acquire_building(self.building1)
        self.assertIn(self.building1, self.landowner.buildings)
        self.assertEqual(self.building1.owner, self.landowner)
        self.assertLess(self.landowner.money, 200000)  # Money should be less after down payment
        self.assertIn(self.building1, self.landowner.mortgages)

    def test_calculate_monthly_mortgage_payment(self):
        print("Test the mortgage payment calculation.")
        loan_amount = 80000
        rate = 0.05
        term = 360
        expected_payment = loan_amount * (rate / 12) / (1 - (1 + rate / 12) ** -term)
        self.assertAlmostEqual(
            self.landowner.calculate_monthly_mortgage_payment(loan_amount, rate, term),
            expected_payment,
            places=2
        )

    def test_collect_rent(self):
        print("Test that a landowner can collect rent from buildings.")
        unit1 = Unit(1000)
        unit2 = Unit(1500)
        unit1.occupied = True;
        unit2.occupied = True;
        self.building1.units = [unit1, unit2]
        self.landowner.acquire_building(self.building1)
        initial_money = self.landowner.money
        self.landowner.collect_rent()
        self.assertEqual(self.landowner.money, initial_money + 2500)

    def test_pay_mortgage(self):
        print("Test that a landowner can pay mortgage costs.")
        self.landowner.acquire_building(self.building1)
        initial_money = self.landowner.money
        self.landowner.pay_mortgage()
        print("Mortgage amount: ", sum(self.landowner.mortgages.values()))
        print("Money after payment: ", self.landowner.money )
        print("Initial money: ", initial_money)
        self.assertLess(self.landowner.money, initial_money)

    def test_sell_building(self):
        print("Test that a landowner can sell a building.")
        self.landowner.acquire_building(self.building1)
        initial_money = self.landowner.money # money after paying down payment 
        self.landowner.sell_building(self.building1)
        self.assertNotIn(self.building1, self.landowner.buildings)
        self.assertEqual(self.building1.owner, None)
        self.assertEqual(self.landowner.money, initial_money + self.building1.value)

    def test_redevelop_building(self):
        print("Test that a landowner can redevelop a building.")
        self.landowner.acquire_building(self.building1)
        initial_money = self.landowner.money
        self.building1.age = 25
        self.landowner.redevelop_building(self.building1)
        self.assertEqual(self.building1.age, 0)
        self.assertLess(self.landowner.money, initial_money)  # Money should be less after redevelopment

    def test_make_decision_aggressive(self):
        print("Test decision making for aggressive landowner.")
        city = City(20, 0.8, 10, 10)
        city.grid[0][0] = self.building1
        self.landowner.money = 200000
        self.landowner.make_decision(city)
        self.assertIn(self.building1, self.landowner.buildings)

    def test_make_decision_passive(self):
        print("Test decision making for passive landowner.")
        self.landowner.preference = "Pass"
        self.building1.age = 25
        self.landowner.buildings.append(self.building1)
        self.landowner.make_decision(None)
        initial_money = self.landowner.money
        self.assertEqual(self.landowner.money, initial_money)
        self.assertEqual(self.building1.age, 25)

if __name__ == "__main__":
    unittest.main()

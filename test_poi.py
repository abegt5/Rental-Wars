import unittest
from poi import PoI
from building import Building

class TestPoI(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.building = Building(10, 10, 8)
        self.small_poi = PoI(x=15, y=15, poi_type="Small")
        self.medium_poi = PoI(x=20, y=20, poi_type="Medium")
        self.large_poi = PoI(x=30, y=30, poi_type="Large")
        self.crime_poi = PoI(x=25, y=25, poi_type="Crime")

    def test_distance_to(self):
        print("Test the distance calculation from a PoI to a building.")
        self.assertAlmostEqual(self.small_poi.distance_to(self.building), 7.07, places=2)
        self.assertAlmostEqual(self.medium_poi.distance_to(self.building), 14.14, places=2)
        self.assertAlmostEqual(self.large_poi.distance_to(self.building), 28.28, places=2)
        self.assertAlmostEqual(self.crime_poi.distance_to(self.building), 21.21, places=2)

    def test_influence_attractiveness(self):
        print("Test the influence on attractiveness based on distance and PoI type.")
        self.assertEqual(self.small_poi.influence_attractiveness(self.building), 1)
        self.assertEqual(self.medium_poi.influence_attractiveness(self.building), 1)
        self.assertEqual(self.large_poi.influence_attractiveness(self.building), 0)  # Out of range
        self.assertEqual(self.crime_poi.influence_attractiveness(self.building), 0)  # Out of range for crime

if __name__ == '__main__':
    unittest.main()

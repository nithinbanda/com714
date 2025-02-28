import unittest

from human import Human
from planet import Planet

class TestPlanet(unittest.TestCase):
    def test_add_human(self):

        # check: 0 population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: single human
        prints = Human("Prints")
        earth.add(prints)
        self.assertEqual(earth.population(), 1, "Population should be 1.")

    def test_has(self):

        # check: does not have specified human
        earth = Planet("Earth")
        prints = Human("Prints")
        self.assertFalse(earth.has(prints), "Should be false.")

        # check: has specified human
        earth.add(prints)
        self.assertTrue(earth.has(prints), "Should be true.")

    def test_population(self):

        # check: no population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: no population of one
        prints = Human("Prints")
        earth.add(prints)
        self.assertEqual(earth.population(), 1, "Population should be 1")

if __name__ == '__main__':
 unittest.main()
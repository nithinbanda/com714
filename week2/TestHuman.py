import unittest
from human import Human

class TestHuman(unittest.TestCase):

    def test_eat(self) -> None:
        # energy is full and try to eat
        human_prints = Human("Prints")
        self.assertEqual(human_prints.eat(20), 20, "Excess should be 20.")

        # energy is below 100 and eat more than required
        human_prints = Human("Prints", energy=90)
        self.assertEqual(human_prints.eat(20), 10, "Excess should 20.")

        # energy is below 100 and eat exactly what is required
        human_prints = Human("Prints", energy=80)
        self.assertEqual(human_prints.eat(20), 0, "Excess should be 0.")

        # energy is below 100 and eat less than required
        human_prints = Human("Prints", energy=70)
        self.assertEqual(human_prints.eat(20), -10, "Excess should be -10.")

  # Add additional tests here.

if __name__ == '__main__':
    unittest.main()
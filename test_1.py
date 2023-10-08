import unittest
import sqlite3


class TestDatabase(unittest.TestCase):
    def test_no_lastnames_starting_with_a(self):
        connection = sqlite3.connect("names.db")
        cursor = connection.cursor()

        # Count the number of lastnames starting with A
        cursor.execute("SELECT COUNT(*) FROM people WHERE lastname LIKE 'A%';")
        count = cursor.fetchone()[0]
        connection.close()

        # Assert that the count is equal to zero
        self.assertEqual(count, 0)


if __name__ == "__main__":
    unittest.main()

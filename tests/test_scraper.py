import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

from Scraper import Scraper


class ScraperUnitTests(unittest.TestCase):
    def test_should_contain(self):
        # Arrange
        subject = Scraper()

        # Act
        results = subject.contains("hello there", r"h.l")
        print(f"test results: {results}")

        # Assert
        self.assertEqual(results, True)

    def test_should_not_contain(self):
        # Arrange
        subject = Scraper()

        # Act
        results = subject.contains("hello there", r"apple")
        print(f"test results: {results}")

        # Assert
        self.assertEqual(results, False)


class ScraperIntTests(unittest.TestCase):
    def test_should_get(self):
        # Arrange
        subject = Scraper()

        # Act
        results = subject.get("https://www.cnn.com")
        print(f"test results: {results}")

        # Assert
        self.assertEqual(results.http_status, 200)
        self.assertGreater(len(results.html_content), 0)

    def test_should_get_redirect(self):
        # Arrange
        subject = Scraper()

        # Act
        results = subject.get("http://cnn.com")
        print(f"test results: {results}")

        # Assert
        self.assertEqual(results.http_status, 200)
        self.assertGreater(len(results.html_content), 0)


if __name__ == "__main__":
    unittest.main()

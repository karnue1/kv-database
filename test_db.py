import unittest
from main import CustomKVStore


class TestKVStore(unittest.TestCase):
    def setUp(self):
        self.store = CustomKVStore()

    def test_set_and_get(self):
        self.store.set("name", "Titus")
        self.assertEqual(self.store.get("name"), "Titus")

    def test_overwrite_key(self):
        self.store.set("key", "val1")
        self.store.set("key", "val2")
        self.assertEqual(self.store.get("key"), "val2")

    def test_delete_and_exists(self):
        self.store.set("temp", "123")
        self.assertTrue(self.store.exists("temp"))
        self.store.delete("temp")
        self.assertFalse(self.store.exists("temp"))


if __name__ == "__main__":
    unittest.main()

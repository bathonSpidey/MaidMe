import unittest
from Collection import Collection
import cv2

image= cv2.imread("pass.jpg")
imageString= image.tostring()
document = {
            'FirstName': 'Abir',
            'LastName': 'Bhattacharyya',
            'Address': 'Sanjivani Path, Choladhora, Jorhat, Assam',
        }

class CollectionTests(unittest.TestCase):
    def setUp(self):
        self.collection = Collection("mongodb+srv://admin:MaidMe@cluster0.lkcux.mongodb.net/test", "MaidMe")
        self.name="Employees"

    def test_connection(self):
        database=self.collection.GetCollection('Employees')
        self.assertIsNotNone(database)

    def test_insertion(self):
        self.collection.Add(self.name,document)

    def test_insertion_with_image(self):
        imageID=self.collection.fileSystem.put(imageString, encoding="utf-8")
        document["Image"]={'imageID': imageID,
                           'shape': image.shape,
                           'dtype': str(image.dtype)
        }
        self.collection.Add(self.name, document)

    def test_get_entry_back(self):
        entry=self.collection.FindOneBasedOneFirstName(self.name,"Abir")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.LastName, "Bhattacharyya")

    def test_get_entry_back_based_on_criteria(self):
        entry=self.collection.FindOne(self.name,"FirstName", "Abir")
        self.assertIsNotNone(entry)
        self.assertEqual(entry["LastName"], "Bhattacharyya")

    def test_get_many_entries_back_based_on_criteria(self):
        entry=self.collection.FindAll(self.name,"FirstName", "Abir")
        self.assertIsNotNone(entry)
        self.assertGreaterEqual(len(entry), 2)

    def test_deserialize_image(self):
        entry = self.collection.FindOne(self.name, "FirstName", "Vishal")
        test_image=self.collection.DeserializeImage(entry)
        self.assertEqual(test_image.shape, (272,265,3))







if __name__ == '__main__':
    unittest.main()

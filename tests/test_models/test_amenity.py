#!/usr/bin/python3

import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Initializes values """
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Hot Tub"

    @classmethod
    def teardown(cls):
        """ Delete object """
        del cls.amenity1

    def tearDown(self):
        """ Remove the file """
        try:
            os.remove("file.json")
        except:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """ Look if is child class """
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """ Check if there functions """
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """ Look the attributes """
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_attributes_are_strings(self):
        """ Look if the attributes are strings """
        self.assertEqual(type(self.amenity1.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "Look if is normal database")
    def test_save(self):
        """ Look if the class save """
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict(self):
        """ Look if there to_dict """
        self.assertEqual('to_dict' in dir(self.amenity1), True)

if __name__ == "__main__":
    unittest.main()

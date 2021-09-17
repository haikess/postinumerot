import unittest
import postinumerot


class test_postinumerot(unittest.TestCase):

    def setUp(self):
        self.postcode_map = postinumerot.get_postcode_map()

    def test_single_postcode_found(self):
        postcode_list = postinumerot.get_postcode_by_municipality('KUSTAVI', self.postcode_map)
        self.assertEqual(1, len(postcode_list))

    def test_multiple_postcode_found(self):
        postcode_list = postinumerot.get_postcode_by_municipality('PORVOO', self.postcode_map)
        self.assertGreater(len(postcode_list), 1)


    def test_only_one_instance_of_smartpost(self):
        postcode_map = postinumerot.get_postcode_map()
        smartnames = [postcode_map[name] for name in postcode_map if "SMART" in postcode_map[name]]
        smartnames = list(dict.fromkeys(smartnames))
        self.assertEqual(1, len(smartnames))
        self.assertEqual("SMARTPOST", smartnames[0])


if __name__ == '__main__':
    unittest.main()




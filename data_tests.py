import unittest
import data

counties = [
    'Accomack County', 'Albemarle County', 'Alleghany County',
    'Amelia County', 'Amherst County', 'Appomattox County',
    'Appomattox County', 'Augusta County', 'Bath County',
    'Bedford County', 'Bland County', 'Botetourt County',
    'Brunswick County', 'Buchanan County', 'Buckingham County',
    'Campbell County', 'Caroline County', 'Carroll County',
    'Charles City County', 'Charlotte County', 'Fairfax County',
    'Essex County', 'Halifax County', 'Henrico County'
]

class GetData(unittest.TestCase):

    def test_get_get1(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[0])))

    def test_get_get2(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[2])))

    def test_get_get3(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[4])))

    def test_get_get4(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[6])))

    def test_get_get5(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[8])))

    def test_get_get6(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[10])))

    def test_get_get7(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[12])))

    def test_get_get8(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[14])))

    def test_get_get9(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[16])))

    def test_get_get10(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[18])))

    def test_get_get11(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[20])))

    def test_get_get12(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[22])))

    def test_get_get13(self):
        self.assertEqual(not bool({}), bool(data.get_data(counties[23])))
if __name__ == '__main__':
    unittest.main()

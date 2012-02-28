import unittest

class SerializeTests(unittest.TestCase):

    def _callFUT(self, value):
        from . import serialize
        return serialize(value)

    def _reverse(self, fields):
        from peppercorn import parse
        return parse(fields)

    def assertReversable(self, fields, value):
        reversed = self._reverse(fields)
        self.assertEqual(reversed, value)
        
    def test_empty_name(self):
        value = {'': {'name': 'aodag'}}

        result = self._callFUT(value)
        self.assertReversable(result, value)

    def test_it(self):

        value = {'series':
             {'name':'date series 1',
              'dates': [['10', '12', '2008'],
                        ['10', '12', '2009']],
              },
             'name': 'project1',
             'title': 'Cool project'}
        result = self._callFUT(value)
        self.assertReversable(result, value)

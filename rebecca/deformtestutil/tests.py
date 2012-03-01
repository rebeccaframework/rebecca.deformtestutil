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

    def test_serializer(self):
        from zope.interface import directlyProvides
        from .interfaces import ISerializable
        from peppercorn import START, END, MAPPING

        class DummySerializer(object):
            def serialize(self, name):
                yield (name, 'a', 'b')

        serializer = DummySerializer()
        directlyProvides(serializer, ISerializable)
        value = {'image': {'upload': serializer}}
        result = self._callFUT(value)
        result = list(result)

        self.assertEqual(result,
            [
            (START, '%s:%s' % ('image', MAPPING)),
            ('upload', 'a', 'b'),
            (END, 'image'),
            ])


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

class WebTestFileUploadTests(unittest.TestCase):
    def _getTarget(self):
        from . import WebTestFileUpload
        return WebTestFileUpload

    def _makeOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        from StringIO import StringIO
        fp = StringIO('this is content')
        target = self._makeOne('dummy', fp)

        it  = target.serialize('upload')
        result = it.next()
        self.assertEqual(result, ('upload', 'dummy', 'this is content'))

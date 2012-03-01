from peppercorn import START, END, MAPPING, SEQUENCE
from zope.interface import implementer
from .interfaces import ISerializable

def start_mapping(name=None):
    if name:
        return (START, "%s:%s" % (name, MAPPING))
    else:

        return (START, MAPPING)

def end_mapping(name=None):
    if name:
        return (END, name)
    else:
        return (END, '')

end_sequence = end_mapping

def start_sequence(name=None):
    if name:
        return (START, "%s:%s" % (name, SEQUENCE))
    else:

        return (START, SEQUENCE)

def serialize(value, name=None):
    if ISerializable.providedBy(value):
        s = value.serialize(name)
        for x in s:
            yield x 
    elif isinstance(value, dict):
        if name is not None:
            yield start_mapping(name)
        for k, v in value.items():
            s = serialize(v, k)
            for x in s:
                yield x
        if name is not None:
            yield end_mapping(name)
    elif isinstance(value, list):
        if name is not None:
            yield start_sequence(name)
        for i, v in enumerate(value):
            s = serialize(v, '%s-%d' % (name, i))
            for x in s:
                yield x
        if name is not None:
            yield end_sequence(name)
    else:
        yield (name, value)


@implementer(ISerializable)
class WebTestFileUpload(object):

    def __init__(self, filename, fp):
        self.fp = fp
        self.filename = filename

    def serialize(self, name):
        yield (name, self.filename, self.fp.read())

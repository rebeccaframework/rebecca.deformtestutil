from peppercorn import START, END, MAPPING, SEQUENCE

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
    if isinstance(value, dict):
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

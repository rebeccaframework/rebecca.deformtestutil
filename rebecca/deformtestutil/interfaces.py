from zope.interface import Interface

class ISerializable(Interface):

    def serialize(name):
        """ serialize key value to tuple yieldings"""

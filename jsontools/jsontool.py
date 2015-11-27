class Serializer(object):

    def serialize(self, data):
        if isinstance(data, list):
            return '[' + ','.join([self.serialize(elem) for elem in data]) + ']'
        if isinstance(data, dict):
            return '{' + ','.join([self.serialize(k) + ':' + self.serialize(v) for k, v in data.iteritems()]) + '}'
        if isinstance(data, (int, float)):
            return str(data)
        if isinstance(data, str):
            return '"' + data + '"'


class Parser(object):

    def parse(self, data):
        pass

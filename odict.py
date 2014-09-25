################################
#Program File: odict.py
#Created By: Charles (AcePokeMaster)
#Description: A custom made dict() called odict()
#Version: 1.0
################################


class odict:

    def __init__(self):
        self._keys = []
        self._data = {}

    def __setitem__(self, key, value):
        if key not in self._data:
            self._keys.append(key)
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __delitem__(self, key):
        del self._data[key]
        self._keys.remove(key)

    def __contains__(self, key):
        return key in self._data

    def __repr__(self):
        return "customdict({%s})"%(",".join(["%s:%s" % (key,self._data[key]) for key in self._keys]))

    def __len__(self):
        return len(self._keys)

    def keys(self):
        "a list object providing a view on odict's keys"
        return self._keys.copy()

    def values(self):
        "an object providing a view on odict's values"
        return self._data.values()

    def count(self, value):
        'integer -- return number of occurrences of value'
        return len([tmp for tmp in self._data.values() if tmp == value])

    def insert(self, index, key, value):
        'insert object before index'
        self._keys.insert(index, key)
        self._data[key] = value

    def index(self, key):
        'integer -- return first index of value'
        return self._keys.index(key)

    def pop(self,num=-1):
        'remove and return key value pair at index (default last)'
        key = self._keys.pop(num)
        value = self._data[key]
        del self._data[key]
        return {key:value}

    def copy(self):
        'a shallow copy of odict'
        copyDict = odict()
        copyDict._data = self._data.copy()
        copyDict._keys = self._keys.copy()
        return copyDict

'''
MIT License

Copyright (c) 2019 Kyle Kowalczyk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

class ExtendedStr(str):

    def numbers(self):
        return ''.join([x for x in self if x.isdigit()])

    def letters(self):
        return ''.join([x for x in self if not x.isdigit()])

    def reverse(self):
        value = []
        for x in self:
            value.insert(0, x)
        return ''.join([x for x in value])
    
    def remove_character(self, char):
        return ''.join([x for x in self if x != char])

class ExtendedList(list):
    
        def pluck_dict(self, key, desired_value):
            '''
            This method will only work if the list is a list of dictionaries, the list can not contain anything but dictionaries or it will throw
            a type error.
            :param key: Key in the dictionary to search on
            :param desired_value: Value that the key should have to be selected.
            :return: dictionary from list.
            '''
            for x in self:
                if type(x) != dict:
                    raise TypeError('This method will only run on a list of dictionaries! Your list contains a {}'.format(type(x).__name__))
            return next((item for item in ssh.show_vlan() if item[key] == desired_value), None)

class ExtendedDict(dict):
    pass


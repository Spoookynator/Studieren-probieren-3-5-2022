import json
import pickle

# how its stored is not importaint, we just want to be able to read it
# pickle only for programs with 1 user, or 1 program needing to access the data, even there not that good


class City:
    def __init__(self, name) -> None:
        self.city = name


class Building:
    def __init__(self, size, c) -> None:
        self.size = size
        self.location = c


class Person:
    def __init__(self, name, address, age, b) -> None:
        self.name = name
        self.address = address
        self.age = age
        self.livesIn = b


p = Person("Sam", "Vienna", 32, Building(788, City("Krems")))


class MyPersonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(
            self, object_hook=self.convert, *args, **kwargs)

    def convert(self, dct): # decoding starts from the back
        #{"name": "Sam", "address": "Vienna", "age": 32, "livesIn": {"size": 788, "location": {"city": "Krems"}}}
        
        if("city" in dct):
            return City (dct["city"])
        
        if("size" in dct):
            return Building (dct["size"], dct["location"])
        
        p = Person(dct["name"], dct["address"], dct["age"], dct["livesIn"])

        return p

with open("2.json", "w") as jfile:
    json.dump(p, jfile, default=lambda x: x.__dict__)
    # json.dump (p.__dict__, jfile) # converts class to dictionary -> gets converted to object by json encoder, doesnt work with objects (cant be converted to dict)

with open("2.json", "r") as jfile:
    x = json.load(jfile, cls = MyPersonDecoder)
    print(type(x))
    print(x)


'''
with open ("person.data", "wb") as pfile:
    #pickle.dump(p, pfile)

with open ("person.data", "rb") as pfile:
    p2 = pickle.load(pfile)
    print (p2.name)
    print (p2.livesIn)
'''

#adict = {"name":"apple", "size":30}

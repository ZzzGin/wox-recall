import json
import re


class SavedItems():
    def __init__(self):
        with open('items.json') as json_file:  
            self.items = json.load(json_file)
    
    def addItems(self, key, value):
        if key not in self.items:
            self.items[key] = value
        with open('items.json', 'w') as outfile:  
            json.dump(self.items, outfile)

    def deleteItems(self, key):
        if key in self.items:
            del self.items[key]
        with open('items.json', 'w') as outfile:  
            json.dump(self.items, outfile)
    
    def clearItems(self):
        self.items.clear()
        with open('items.json', 'w') as outfile:  
            json.dump(self.items, outfile)
    
    def updateItems(self, key, value):
        if key in self.items:
            self.items[key] = value
        with open('items.json', 'w') as outfile:  
            json.dump(self.items, outfile)

    def queryItems(self, key):
        key = ".*".join(list(key.lower()))
        pattern = ".*"+key.lower()+".*"
        result = []
        prog = re.compile(pattern)
        for k in self.items:
            if prog.match(k.lower()):
                result.append((k, self.items[k]))
        return result

    def queryItemsWithRE(self, r):
        result = []
        prog = re.compile(r)
        for k in self.items:
            if prog.match(k):
                result.append((k, self.items[k]))
        return result
        



if __name__ == "__main__":
    s = SavedItems()
    s.clearItems()
    s.addItems("suid", "462324*39")
    s.addItems("aaa", "111")
    s.addItems("bbb", "222")
    s.addItems("ccc", "333")
    s.addItems("ddd", "444")
    s.addItems("eee", "555")
    s.addItems("address", "123 ABC Ave. Some City, NY")
    print(s.items)
    s.updateItems("suid", "462324839")
    print(s.items)
    s.deleteItems("address")
    print(s.items)
    print(s.queryItems("ui"))
    print(s.queryItemsWithRE(".*"))

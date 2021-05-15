# -*- coding: utf-8 -*-

from wox import Wox
from SavedItems import SavedItems
import pyperclip

class Recall(Wox):

    def query(self, query):
        results = []
        query_list = query.split()
        
        if len(query_list)==0:
            self.nothingToQuery(results)
            return results

        def isValidCommand(s):
            c = set(['a', 'd', 'u', 'r', 'h'])
            if len(s)==2 and s[0]=='-' and s[1] in c:
                return s[1]
            else:
                return None

        command = isValidCommand(query_list[0])
        if command=='a':
            self.addResultWrapper(results, query_list)
        elif command=='d':
            self.deleteResultWrapper(results, query_list)
        elif command=='u':
            self.updateResultWrapper(results, query_list)
        elif command=='r':
            self.queryResultWithREWrapper(results, query_list)
        elif command=='h':
            self.helper(results)
        else:
            self.queryResultWrapper(results, query)
        return results

    def nothingToQuery(self, results):
        results.append({
            "Title": "Recall the Future",
            "SubTitle": "Recall -h for help",
            "IcoPath":"Images/Logo-refresh-icon.png"
        })
        return results

    def queryResultWrapper(self, results, query):
        s = SavedItems()
        r = s.queryItems(query)
        for i in r:
            results.append({
                "Title": "{}: {}".format(i[0], i[1]),
                "SubTitle": "Recall",
                "IcoPath":"Images/Logo-refresh-icon.png",
                "JsonRPCAction":{
                    "method": "copyToClipboard",
                    "parameters":[i[1]],
                    "dontHideAfterAction":False
                }
            })
        
    def queryResultWithREWrapper(self, results, query_list):
        s = SavedItems()
        r = s.queryItemsWithRE(query_list[1] if len(query_list)>1 else "")
        for i in r:
            results.append({
                "Title": "{}: {}".format(i[0], i[1]),
                "SubTitle": "Recall",
                "IcoPath":"Images/Logo-refresh-icon.png",
                "JsonRPCAction":{
                    "method": "copyToClipboard",
                    "parameters":[i[1]],
                    "dontHideAfterAction":False
                }
            })

    def copyToClipboard(self, value):
        pyperclip.copy(value.strip())
    
    def addResultWrapper(self, results, query_list):
        query_list_length = len(query_list)
        results.append({
            "Title": "Add: {" + (query_list[1] if query_list_length>1 else "") +"} -> {" + (" ".join(query_list[2:]) if query_list_length>2 else "")+"}",
            "SubTitle": "Recall Add Item: -a {Key} {Value}",
            "IcoPath":"Images/Logo-refresh-icon.png",
            "JsonRPCAction":{
                "method": "addItem",
                "parameters":[query_list[1] if query_list_length>1 else "", " ".join(query_list[2:]) if query_list_length>2 else ""],
                "dontHideAfterAction":False
            }
        })

    def addItem(self, key, value):
        if key=="" or value=="":
            return
        s = SavedItems()
        s.addItems(key, value)
    
    def deleteResultWrapper(self, results, query_list):
        query_list_length = len(query_list)
        results.append({
            "Title": "Delete: " + "{"+(query_list[1] if query_list_length>1 else "")+"}",
            "SubTitle": "Recall Delete Item: -d {Key}",
            "IcoPath":"Images/Logo-refresh-icon.png",
            "JsonRPCAction":{
                "method": "deleteItem",
                "parameters":[query_list[1] if query_list_length>1 else ""],
                "dontHideAfterAction":False
            }
        })

    def deleteItem(self, key):
        if key=="":
            return
        s = SavedItems()
        s.deleteItems(key)

    def updateResultWrapper(self, results, query_list):
        query_list_length = len(query_list)
        results.append({
            "Title": "Update: {" + (query_list[1] if query_list_length>1 else "") +"} -> {" + (" ".join(query_list[2:]) if query_list_length>2 else "")+"}",
            "SubTitle": "Recall Update Item: -u {Key} {Value}",
            "IcoPath":"Images/Logo-refresh-icon.png",
            "JsonRPCAction":{
                "method": "updateItem",
                "parameters":[query_list[1] if query_list_length>1 else "", " ".join(query_list[2:]) if query_list_length>2 else ""],
                "dontHideAfterAction":False
            }
        })

    def updateItem(self, key, value):
        if key=="" or value=="":
            return
        s = SavedItems()
        s.updateItems(key, value)

    def helper(self, results):
        results.append({
            "Title": "Fuzzy Query:\tRecall {key}",
            "SubTitle": "Recall help",
            "IcoPath":"Images/Logo-refresh-icon.png",
        })
        results.append({
            "Title": "RegExr Query:\tRecall -r {RE}",
            "SubTitle": "Recall help",
            "IcoPath":"Images/Logo-refresh-icon.png",
        })
        results.append({
            "Title": "List all Items:\tRecall .",
            "SubTitle": "Recall help",
            "IcoPath":"Images/Logo-refresh-icon.png",
        })
        results.append({
            "Title": "Add Item:\tRecall -a {key} {value}",
            "SubTitle": "Recall help",
            "IcoPath":"Images/Logo-refresh-icon.png",
        })
        results.append({
            "Title": "Delete Item:\tRecall -d {key}",
            "SubTitle": "Recall help",
            "IcoPath":"Images/Logo-refresh-icon.png",
        })
        results.append({
            "Title": "Update Item:\tRecall -u {key} {value}",
            "SubTitle": "Recall help",
            "IcoPath":"Images/Logo-refresh-icon.png",
        })

if __name__ == "__main__":
    Recall()
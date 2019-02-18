from SavedItems import SavedItems
import os

class Recall():
    def __init__(self):
        self.db = SavedItems()


    def query(self, query):
        results = []
        results.append({
            "Title": "Recall",
            "SubTitle": "{}".format(os.path.dirname(os.path.realpath(__file__))),
            "IcoPath":"Images/Logo-refresh-icon.png",
        })
        return results
        
    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.ico"
        })
        return results

if __name__ == "__main__":
    r = Recall()
    a = r.query("su")
    print(a)
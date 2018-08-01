import json
import os
import uuid

class User:
    def __init__(self,isim,soyisim, numara):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara


class DatabaseMethods:

    def __init__(self):
        self.path= "database.json"
        self.Create_Database_If_Not_Exists()

    def Create_Database_If_Not_Exists(self):
        if not os.path.exists(self.path):
            with open(self.path,"w") as f:
                json.dump({},f)


    def __init__(self):
        self.path2 = "database.json"

    @staticmethod
    def add(self, user): #db.add(user)
        with open(self.path,"w") as f:
            js= json.load()
        js.update({
            str(uuid.uuid1()): {

                "isim": user.isim,
                "soyisim" : user.soyisim,
                "numara" : user.numara
            }
        })
        json.dump(js,f)

    @staticmethod
    def update(user): #db.update(user)
        pass

    @staticmethod
    def get(self): #return [user]
        with open(self.path) as f:
            js = json.load(f)
        return js

    @staticmethod
    def delete(user): #db.delete(user)
        with open(self.path,"r") as f:
            js= json.load(f)

        if user_id in js:
            del js[user_id]

        with open((self.path, "w") as f:
            js



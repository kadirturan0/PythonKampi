import sys
from pprint import  pprint


class ConsoleProgram:
    def __init__(self):
        self.main_choice=""
        self.choices_list = ["1","2","3","4"]

    def Main_page(self):
        print("Hoşgeldiniz")
        print("1. Kayıtları göster")
        print("2. Ekle")
        print("3. Güncelle")
        print("4. Sil")

        while True:
            self.main_choice = input()
            if self.main_choice in self.choices_list:
                break
        self.Clear_Screen()
        print("Girdiğiniz Değer Yanlış!")

    def Goto_Choice(self):
        db = DatabaseMethods()
        if self.main_choice=="1":
            pprint(db.get)

    @staticmethod
    def Clear_Screen():
        os.system("cls" if sys.platform == "nt" else "clear")


    def Run(self):
        self.Main_page()
        self.Goto_Choice()

if __name__ == '__main__':
    n=ConsoleProgram()
    n.Run()
class Motorsiklet(object):

    def __init__(self,lastik):
        self.lastik = lastik
    def gosterge(self):
        print(self.lastik)
    def get_lastik(self):
        return self.lastik

    def set_lastik(self,lastik):
        self.lastik = lastik


sezer_hocanin_chopperi = Motorsiklet(2)
sezer_hocanin_chopperi.set_lastik(10)
dogukan_hocanin_motoru = Motorsiklet(3)
print(sezer_hocanin_chopperi.get_lastik())
print(dogukan_hocanin_motoru.get_lastik())
print()





    lastik = 2
    parcalar = ['gidon', 'teker']



motor = Motorsiklet
print(motor.lastik)
print(Motorsiklet)
print(motor)
print(motor.lastik)
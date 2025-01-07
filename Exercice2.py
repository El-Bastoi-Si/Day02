from datetime import datetime 
class Voiture:
    def __init__(self,marque,modele,annee,kilometrage):
                 
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
    def calculer_age(self):
        date_actuelle = int(datetime.now().strftime('%Y'))
        age = date_actuelle-self.annee 
        print(f"La voiture est de {self.annee} donc cette annee elle a {age} ans")
    def Est_vieille(self):
        date_actuelle = int(datetime.now().strftime('%Y'))
        age = date_actuelle-self.annee 
        if age < 10:
            
            return False
        else:
            return True
    

voiture1 = Voiture("Renault", "Golf",2015,60000 )
voiture2=Voiture("Cadillac Escalade","Standard",2022,50000)
voiture3=Voiture("Peugot","E-Rifter",2014,150000)
voiture4=Voiture("BMW","X1",2018,160000)
voiture1.calculer_age()
voiture1.Est_vieille()
voiture2.calculer_age()
voiture2.Est_vieille()
voiture3.calculer_age()
voiture3.Est_vieille()
voiture4.calculer_age()
voiture4.Est_vieille()


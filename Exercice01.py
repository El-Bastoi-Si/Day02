class Voiture:
    def __init__(self,marque,modele,annee,kilometrage):
                 
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
    def Afficher_details(self):
        print(f"{self.marque} {self.modele} de {self.annee} avec {self.kilometrage} km ")
    def Augmater_kilometrage(self,distance):
        self.kilometrage += distance 
        print(f"L'augmentation du kilomettrage est {distance} km donc votre nouveau kilometrage est de {self.kilometrage} km")


voiture1 = Voiture("Renault", "Golf",2017,60000 )
voiture2 = Voiture("Cadillac Escalade","Standard",2022,50000)
voiture1.Afficher_details()
voiture1.Augmater_kilometrage(50)
voiture2.Afficher_details()
voiture2.Augmater_kilometrage(60)


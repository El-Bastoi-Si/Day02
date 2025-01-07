class Produit:
    def __init__(self,nom,prix,quantite):
        self.nom =nom 
        self.prix = prix 
        self.quantite = quantite
    def Affiche_produit(self):
        print(f"{self.nom} coute {self.prix} € et la quantite est de  {self.quantite}")
class Magasin:
    def __init__(self):
        self.produit = []
    def Ajouter_produit(self,produit):
        self.produit.append(produit)
        print(self.produit)
    def Recherche_produit(self,nom_produit):
        for produit in self.produit:
            if produit.nom == nom_produit:
                return produit
            return None
           
    def Affiche_inventaire(self):
        for produit in self.produit:
            produit.Affiche_produit()
    def Vendre_produit(self,nom_produit,quantite_vendue):
        produit_a_vendre = self.Recherche_produit(nom_produit)
        if produit_a_vendre:
            if produit_a_vendre.quantite >= quantite_vendue:
                produit_a_vendre.quantite -= quantite_vendue
                print(f"")
Produit1 = Produit("Banane",2,42)
Produit2 = Produit("Chips",1,50)
Produit3 = Produit("kiwi",0.99,38)
Produit4 = Produit("Sucre",4,50)
Produit5 = Produit("cafe",4.5,58)
Produit6 = Produit("gateau",0.89,21)

mon_magasin = Magasin()
mon_magasin.Ajouter_produit(Produit1)
mon_magasin.Ajouter_produit(Produit2)
mon_magasin.Ajouter_produit(Produit3)
mon_magasin.Ajouter_produit(Produit4)
mon_magasin.Ajouter_produit(Produit5)
mon_magasin.Ajouter_produit(Produit5)






       
        

            
             



        
    





        


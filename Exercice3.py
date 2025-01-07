class Animal:
    def __init__(self,nom,espece):
        self.nom = nom 
        self.espece = espece
    def Parle(self):
        print("Je suis un animal")
class Chien(Animal):
    def Parle(self):
        print("Wouf")

class Chat(Animal):
    def Parle(self):
        print("Miaou")

class Zoo:
    def __init__(self):
        self.liste = []

    def Ajouter_animal(self, animal):
        self.liste.append(animal)
        print(self.liste)
    
    def faire_parler_tout_le_monde(self):
        for animal in self.liste:
            animal.parle()
        # Faire une boucle sur le self.liste
        # Appeller la méthode Parle de chaque élément de cette liste
        
Le_chien = Chien("Rex", "Chien")
Le_chat  = Chat("Fleur","Chat")
Le_chat.Parle()
Le_chien.Parle()
Ajouter = Zoo()
Ajouter.Ajouter_animal(Le_chien)
Ajouter.Ajouter_animal(Le_chat)

    
    

    




        


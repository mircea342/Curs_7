from abc import abstractmethod

# clasa Animal este generala, poate reprezenta ORICE animal din natura
class Animal:
    nume = ""
    greutate = ""
    culoare = ""

    # exemplu de ABSTRACTIZARE pentru actiunea de a manca
    # mananca() va fi reimplementata ulterior in clasele Caine si Peste cu detalii specifice
    @abstractmethod
    def mananca(self): # actiunea generica de a manca
        raise NotImplementedError


# Caine este un animal? => DA, deci pot sa mostenesc clasa Animal in clasa Caine
class Caine(Animal):

    rasa = ""
    talie = ""

    def prezentare_caine(self):
        print(f"Cainele are: nume {self.nume} greutate {self.greutate} culoare {self.culoare} rasa {self.rasa} talie {self.talie}")

    # implementare a metodei abstracte mananca() din Animal
    # specifica pentru caine
    def mananca(self):
        print(f"Cainele {self.nume} mananca conform dietei date de veterinar!")

# Peste este un animal? => DA, deci pot sa mostenesc clasa Animal in clasa Peste
class Peste(Animal):
    tip_apa = ""

    def depune_icre(self):
        print(f"Pestele {self.nume} depune icre")

    # implementare a metodei abstracte mananca() din Animal
    # specifica pentru peste
    def mananca(self):
        print(f"Pestele {self.nume} mananca plante marine!")


c1 = Caine()
c1.nume = "Azorel"
c1.greutate = 5
c1.culoare = "alb"
c1.rasa = "european"
c1.talie = "mica"

c1.prezentare_caine()
print("===================")

p1 = Peste()
p1.nume = "Nemo"
p1.tip_apa = "dulce"
p1.depune_icre()

print("===================")

#c1.mananca()
#p1.mananca()


lista_animale = [c1, p1]
for my_animal in lista_animale:
    # POLIMORFISM: am o lista de animale (e.g. un caine si un peste), care toate au metoda mananca() implementata
    # deci pot apela aceeasi metoda pentru fiecare obiect, chiar daca implementarile difera pt peste si caine
    my_animal.mananca()
    # my_animal o data va fi cainele c1, alta data va fi pestele p1 , dar cu ambele pot executa
    # mananca() (de aici si ideea de polimorfism)
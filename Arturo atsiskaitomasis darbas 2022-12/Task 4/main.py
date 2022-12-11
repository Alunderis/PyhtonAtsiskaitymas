# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 



class Movie():
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
        
    def wasExpensive(self):
        if self.budget > 100000000:
            print(True)
        else:
            print(False)
    
kinas1 = Movie("Betmanas", "Christopher Nolan", 500000000)
kinas2 = Movie("Supermenas", "Zack Snyder", 12300000)

kinas1.wasExpensive()
kinas2.wasExpensive()
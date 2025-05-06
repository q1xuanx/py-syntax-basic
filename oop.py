from abc import abstractmethod
class Dog: 
    def __init__(self, name, color):
        self.__name = name
        self.color = color

    @abstractmethod
    def bark(self): 
        pass

    def get_name(self): 
        return self.__name

class Labrador(Dog): 

    def bark(self):
        print('Labrador bark')

class Becgie(Dog): 

    def bark(self):
        print('Becgie bark')

def main(): 
    labrador = Labrador("pet1", "yellow")
    bec = Becgie('pet2', 'black')
    labrador.bark()
    print(labrador.get_name())
    bec.bark()
    print(bec.get_name())

if __name__ == '__main__': 
    main()
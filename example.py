class Human():
    def __init__(self, name, lastname, age, gender) :
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender
        print(f"""Его зовут {name}, а фамилия у него {lastname}. Возраст уже {age}, а пол у него ламинат, хе-хе-хе, шутка :) {gender}""")

Human('Niyzbek', 'Mamaev', '20', 'Male')
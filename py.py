class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek


class Student(Osoba):
    def __init__(self, jmeno, vek):
        super().__init__(jmeno, vek)
        self.predmety = []
        self.znamky = []

    def pridej_predmet(self, predmet):
        self.predmety.append(predmet)

    def ziskej_prumer(self):
        return sum(self.znamky) / len(self.znamky) if self.znamky else 0

    def pridej_znamku(self, znamka):
        self.znamky.append(znamka)

    def informace(self):
        print(f"Jméno: {self.jmeno}")
        print(f"Věk: {self.vek}")
        print(f"Seznam předmětů: {', '.join(self.predmety)}")
        print(f"Průměrná známka: {self.ziskej_prumer():.2f}")


class Ucitel(Osoba):
    def __init__(self, jmeno, vek):
        super().__init__(jmeno, vek)
        self.predmety = []

    def pridat_studenta(self, student, predmet):
        student.pridej_predmet(predmet)
        self.predmety.append(predmet)

    def odebrat_studenta(self, student, predmet):
        student.predmety.remove(predmet) if predmet in student.predmety else None
        self.predmety.remove(predmet) if predmet in self.predmety else None

    def informace(self):
        print(f"Jméno: {self.jmeno}")
        print(f"Věk: {self.vek}")
        print(f"Seznam předmětů: {', '.join(self.predmety)}")



student1 = Student("Martin Hruška", 20)

ucitel1 = Ucitel("Jarda Mrázek", 40)

ucitel1.pridat_studenta(student1, "Matematika")

student1.pridej_predmet("Fyzika")
student1.pridej_znamku(85)
student1.pridej_znamku(90)

print("Informace o studentovi:")
student1.informace()

print("\nInformace o učiteli:")
ucitel1.informace()

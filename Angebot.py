import jobSucheWebService
class Angebot:
    def __init__(self, title, arbeitgeber, ort, strasse, date, entfernung):
        self.title = title
        self.arbeitgeber = arbeitgeber
        self.ort = ort
        self.strasse = strasse
        self.date = date
        self.entfernung = entfernung

    print("Willkommen beim Jobparser als Azubi Fachinformatiker/in - Anwendungsentwicklung.")
    ort_angebot = input("Stadt? : ")
    umkreis_angebot = input("Umkreis? : ")

    def to_string(self):
        if self.strasse:
            strasse_str = f'\nStrasse: {self.strasse}'
        else:
            strasse_str = ''


        return (f"\nBeruf: {self.title}\nArbeitgeber: {self.arbeitgeber}\nOrt:{self.ort}{strasse_str}"
                f"\nVeröffentlichungsdatum:{self.date}\nEntfernung von der ausgewählten Stadt: {self.entfernung}KM\n\n")


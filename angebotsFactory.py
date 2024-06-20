from Angebot import *
def build_angebots(angebots):

    jobs = []

    for angebot in angebots["stellenangebote"]:

        title = angebot["beruf"]
        arbeitgeber = angebot["arbeitgeber"]
        ort = angebot["arbeitsort"]["ort"]

        try:
            strasse = angebot["arbeitsort"]["strasse"]
        except:
            strasse = ""

        date = angebot["aktuelleVeroeffentlichungsdatum"]
        entfernung = angebot["arbeitsort"]["entfernung"]

        angebot_object = Angebot(title, arbeitgeber, ort, strasse, date,entfernung)
        jobs.append(angebot_object)

    return jobs


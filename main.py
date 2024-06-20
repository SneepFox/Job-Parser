import jobSucheWebService
import angebotsFactory


print("Willkommen beim Jobparser als Azubi Fachinformatiker/in - Anwendungsentwicklung.")
ort_angebot = input("Stadt? : ")
umkreis_angebot = input("Umkreis?(km) : ")
angebots = jobSucheWebService.gets_angebots(ort_angebot,umkreis_angebot)
result = angebotsFactory.build_angebots(angebots)

for item in result:
    print(item.to_string())














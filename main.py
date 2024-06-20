import jobSucheWebService
import angebotsFactory
angebots = jobSucheWebService.gets_angebots()
result = angebotsFactory.build_angebots(angebots)

for item in result:
    print(item.to_string())














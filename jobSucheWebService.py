import Angebot
import requests
def gets_angebots():
    url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs"
    params = {
        "angebotsart": 4,
        "ausbildungsart": 0,
        "was": "Anwendungsentwicklung",
        "wo": str(Angebot.Angebot.ort_angebot),
        "umkreis": int(Angebot.Angebot.umkreis_angebot),
        "page": 1,
        "size": 25,
        "pav": "false",
        "facetten": "false"
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru,de-DE;q=0.9,de;q=0.8,ru-US;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Origin": "https://www.arbeitsagentur.de",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "X-API-Key": "jobboerse-jobsuche",
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

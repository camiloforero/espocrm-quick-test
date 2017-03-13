import requests
import json

from django_expa import expaApi


def load_companies():
    api = expaApi.ExpaApi(user="camilo.forero@aiesec.net", pwd="cr2rx6tS")
    api.token = "6036e590449213a850e9a5ac6e71e64524847d547de530fc1fe1f90ddf7cc05a"
    companies = api.get_companies(officeID=1589, program=None, start_date="2017-03-05", end_date="2017-03-13")
    for company in companies["items"]:
        print(company)
        data=json.dumps({
            "type":"",
            "industry":"",
            "assignedUserId":"58c5d30f838d2e363",
            "assignedUserName":"Camilo Forero",
            "name":company["name"],
            "emailAddressData":[{"emailAddress":"","primary":True,"optOut":False,"invalid":False,"lower":""}],
            "emailAddress":"",
            "phoneNumberData":[{"phoneNumber":"","primary":True,"type":"Office"}],
            "phoneNumber":"",
            "website":company["url"],
            "billingAddressPostalCode":"","billingAddressStreet":"","billingAddressState":"","billingAddressCity":"","billingAddressCountry":"","shippingAddressPostalCode":"","shippingAddressStreet":"","shippingAddressState":"","shippingAddressCity":"","shippingAddressCountry":"","sicCode":"",
            "description":"",
            "teamsIds":[],"teamsNames":{}
        })
        print(data)
        r = requests.post(
            "http://104.197.179.91/espocrm/api/v1/Account", 
            data=data,
            verify=False,
            headers={"Authorization":"Basic Y2FtaWxvLmZvcmVyb0BhaWVzZWMubmV0OjUyYjMyNDE5OTAwY2U4MTk1MGEyNzIwZDdjNDM5NTQy", "Content-Type":"application/json"})

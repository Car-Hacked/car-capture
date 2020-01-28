import requests
import json

base_url = 'https://park-a-lot.herokuapp.com/api/v1/garages/'
headers = {'content-type': 'application/json', 'accesstoken': ''}


class Garage:
    def __init__(self, garage):
        self.id = garage['_id']
        self.name = garage['garageName']
        self.address = garage['address']
        self.capacity = garage['capacity']
        self.cars_in_lot = garage['carsInLot']

    def to_dict(self):
        return {
            '_id': self.id,
            'carsInLot': int(self.cars_in_lot)
        }


def get_garages():
    resp = requests.get(base_url)
    garages = []
    for g in resp.json():
        garages.append(Garage(g))
    return garages


def put_garage(garage: Garage):
    payload = json.dumps(garage.to_dict())
    requests.patch(base_url, headers=headers, data=payload)


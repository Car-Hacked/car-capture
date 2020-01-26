import requests

base_url = 'https://park-hack-api.herokuapp.com/garages'


class Garage:
    def __init__(self, garage):
        self.id = garage['_id']
        self.name = garage['name']
        self.location = garage['location']
        self.capacity = garage['capacity']
        self.cars_in_lot = garage['carsInLot']

    def to_dict(self):
        return {
            '_id': self.id,
            'name': self.name,
            'location': self.location,
            'carsInLot': int(self.cars_in_lot),
            'capacity': int(self.capacity)
        }


def get_garages():
    resp = requests.get(base_url)
    garages = []
    for g in resp.json():
        garages.append(Garage(g))
    return garages


def put_garage(garage: Garage):
    requests.put(base_url + '/' + garage.id, data=garage.to_dict())


for garage in get_garages():
    print(garage.id)

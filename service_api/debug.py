import requests

API_URL = 'http://127.0.0.1:8000/'


def post_data(model, data):
    endpoint = '{}{}/?format=json'.format(API_URL, model)
    r = requests.post(
        endpoint, json=data, headers={
            "Content-Type": "application/json"
        })
    return r


send_payload = {
    "id": 1,
    "area": {
        "id": 2,
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[0, 0], [0, 10], [10, 10], [10, 0], [0, 0]]]
        },
        "properties": {
            "company": {
                "name": "New rest company",
                "email": "company@kek.ru",
                "phone": "79527264633",
                "address": "Mosocw"
            },
            "name": "small_square"
        }
    },
    "service_type": 1,
    "price_currency": "RUB",
    "price": "200.00"
}
# Add new service
r = post_data('servicetypeareaprice', data=send_payload)
print(r.content)

url = '{}{}/?contains_geom={{ "type": "Point", "coordinates": [ 5, 5 ] }}'.format(
    API_URL, 'servicetypeareaprice')

print(url)
r = requests.get(url)

print(r.content)


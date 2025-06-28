from typing import List

from request_data import get_film_state

if __name__ == '__main__':
    list_of_films: List[int] = [208639, 208642, 308433, 308641]

    for film in list_of_films:
        print(get_film_state(film, 3678))

# states:
# {'status': 'success', 'message': '', 'data': {'bagTrackingData': {}}}
# {'status': 'success', 'message': '', 'data': {'bagTrackingData': {'bagOrder': {'bagid': '888621', 'city': 'Passau', 'inDate': '2025-01-14T11:02:00+01:00', 'outletid': '203678', 'storeDescription': '', 'storeName': 'Dirk Rossmann GmbH', 'street': 'Kapuzinerstr. 30', 'zip': '94032'}}}}

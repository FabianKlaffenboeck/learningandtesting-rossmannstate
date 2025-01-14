from request_data import get_film_state

if __name__ == '__main__':
    data = get_film_state(888621,3678)
    print(data)

 # states:
 # {'status': 'success', 'message': '', 'data': {'bagTrackingData': {}}}
 # {'status': 'success', 'message': '', 'data': {'bagTrackingData': {'bagOrder': {'bagid': '888621', 'city': 'Passau', 'inDate': '2025-01-14T11:02:00+01:00', 'outletid': '203678', 'storeDescription': '', 'storeName': 'Dirk Rossmann GmbH', 'street': 'Kapuzinerstr. 30', 'zip': '94032'}}}}

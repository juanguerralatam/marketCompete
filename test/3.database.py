# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import json
import requests

data = {
    'name': 'Southern-Style Pulled Pork Sandwich',
    'description': 'Slow-cooked, smoky pulled pork topped with our homemade tangy coleslaw and served on a toasted brioche bun.',
    'price': 14,
    'cost_price': 7
}

def test(data, port=9000):
    # Assuming you want to send a POST request to create a new item in the menu
    response = requests.post(f"http://localhost:{port}/menu/", json=data)
    print(response.text)
    print(response.json())

# Call the test function with the dynamic port
test(data, port=9000)
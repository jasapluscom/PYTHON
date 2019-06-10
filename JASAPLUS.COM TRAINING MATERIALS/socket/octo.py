#!/usr/bin/env python3
'''
octo.py
sample octopus http for python3 training
at www.jasaplus.com
'''
from octopus import Octopus

otto = Octopus(
    concurrency=2, auto_start=True
)

def handle_url_response(url, response):
    print(response.text)

otto.enqueue('https://raw.githubusercontent.com/brandiqa/json-examples/master/src/google_markers.json', handle_url_response)
otto.enqueue('https://raw.githubusercontent.com/brandiqa/json-examples/master/src/products.json', handle_url_response)
otto.wait()

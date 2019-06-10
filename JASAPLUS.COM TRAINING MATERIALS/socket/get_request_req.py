#!/usr/bin/env python3
import requests
r = requests.get('https://raw.githubusercontent.com/LearnWebCode/json-example/master/animals-1.json')
print(r.json())

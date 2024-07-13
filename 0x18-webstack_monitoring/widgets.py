#!/usr/bin/python3

import requests
import json

api_key = 'af0e6d4e667cd43b48733bebdce0bb15'
app_key = '99499cdc53aa6e3fca90d069efaf8def5157ae85'

url = "https://api.datadoghq.com/api/v1/dashboard"

headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

data = {
    "title": "System IO Monitoring Dashboard",
    "widgets": [
        {
            "definition": {
                "type": "timeseries",
                "requests": [
                    {"q": "avg:system.io.r_s{*}"}
                ],
                "title": "Read Requests Per Second"
            }
        },
        {
            "definition": {
                "type": "timeseries",
                "requests": [
                    {"q": "avg:system.io.w_s{*}"}
                ],
                "title": "Write Requests Per Second"
            }
        },
        {
            "definition": {
                "type": "timeseries",
                "requests": [
                    {"q": "avg:system.cpu.user{*}"}
                ],
                "title": "CPU Usage"
            }
        },
        {
            "definition": {
                "type": "timeseries",
                "requests": [
                    {"q": "avg:system.mem.used{*}"}
                ],
                "title": "Memory Usage"
            }
        }
    ],
    "layout_type": "ordered"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    dashboard = response.json()
    print(f"Dashboard created successfully with ID: {dashboard['id']}")
else:
    print(f"Failed to create dashboard. Status code: {response.status_code}, Error: {response.text}")

import os
import sys
import json
import datetime
import urllib.request

setting_path = './settings.txt'
if os.path.isfile(setting_path) is False:
    print(setting_path + ' is not found.')
    sys.exit(1)

with open(setting_path, 'r') as file_handler:
    settings = file_handler.readlines()
    if len(settings) != 2:
        print('settings lenght should be 2')
        sys.exit(1)
    ifttt_service_on_url = settings[0][0:-1]
    ifttt_service_off_url = settings[1][0:-1]
    if ifttt_service_on_url[0:21] != 'ifttt_service_on_url=':
        print('The first line setting should begin with ifttt_service_on_url=')
        sys.exit(1)
    if ifttt_service_off_url[0:22] != 'ifttt_service_off_url=':
        print('The second line setting should begin with ifttt_service_off_url=')
        sys.exit(1)

    switch_on_request = urllib.request.Request(ifttt_service_on_url[21:])
    switch_off_request = urllib.request.Request(ifttt_service_off_url[22:])

    switch_on_request.add_header('Content-Type', 'application/json; charset=utf-8')
    json_payload = {
        'value1': datetime.datetime.now().strftime('%H:%m'),
        'value2': '',
        'value3': '',
    }
    jsondata = json.dumps(json_payload)
    json_data_bytes = jsondata.encode('utf-8')

    switch_on_request.add_header('Content-Length', len(json_data_bytes))
    switch_on_response = urllib.request.urlopen(switch_on_request, json_data_bytes)
    on_resp_text = switch_on_response.readlines()

    switch_off_request.add_header('Content-Type', 'application/json; charset=utf-8')
    switch_off_request.add_header('Content-Length', len(json_data_bytes))
    switch_off_response = urllib.request.urlopen(switch_off_request, json_data_bytes)
    off_resp_text = switch_off_response.readlines()

    if switch_on_response.status == 200:
        print(on_resp_text[0].decode('utf-8'))

    if switch_off_response.status == 200:
        print(off_resp_text[0].decode('utf-8'))

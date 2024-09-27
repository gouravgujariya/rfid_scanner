# import requests
#
# url = "https://megasolutions.microlent.com/localtest/test.php"
#
# payload = {
#     'time': '2024-08-16 19:54:19',
#     'card_no': 'test',
#     'device_sn': 'test',
#     'device_name': 'test',
#     'event_point_name': 'test'
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#     'Content-Type': 'application/x-www-form-urlencoded'
# }
#
# response = requests.post(url, data=payload, headers=headers)
#
# print(response.text)

import getmac



# Get MAC address of the current machine

mac_address = getmac.get_mac_address()

print("Current Machine MAC Address:", mac_address)



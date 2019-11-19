import json
import time

from src import crypt
import requests

# Config
VERSION = 'OnePlus7TProOxygen_14.E.07_GLO_007_1910120134'
IMEI = '000000000000000'
PRODUCT = 'OnePlus7TPro_EEA'
ROM_VERSION = 'HD1913_14_191012'

# Run.
url = 'https://otag.h2os.com/post/Query_Update'

headers = {
    'User-Agent': 'com.oneplus.opbackup/2.1.1.190915111124.7ae7e68',
    'Content-Type': 'application/json'
}

body = {
    "version": "2",
    "otaVersion": VERSION,
    "imei": IMEI,
    "mode": "0",
    "language": "en",
    "productName": PRODUCT,
    "type": "1",
    "romVersion": ROM_VERSION,
    "colorOSVersion": "UNKNOWN",
    "androidVersion": "10",
    "time": int(time.time()*1000.0),
    "registrationId": "UNKNOWN",
    "operator": "UNKNOWN",
    "operator2": "UNKNOWN",
    "trackRegion": "UNKNOWN",
    "uRegion": "UNKNOWN",
    "isRooted": "0",
    "isOnePlus": "1",
    "canCheckSelf": "0"
}

response = requests.post(url, json={
    'params': crypt.encrypt(json.dumps(body))
}, headers=headers, timeout=30)

response_body = response.json()
response_obj = json.loads(crypt.decrypt(response_body['resps']))

print(json.dumps(response_obj, indent=4))

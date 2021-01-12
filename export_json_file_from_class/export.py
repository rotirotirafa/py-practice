import json
import time

from person import person

def export_json():
    try:
        now = time.strftime("%M.%S-%d-%m-%Y")
        file = open('{}-dados.json'.format(now), 'w')
        file.write(str(json.dumps(person.__dict__)))
        file.close()
    except Exception as e:
        print(e)
    

export_json()

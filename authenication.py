import wmi
import json
import requests
import os
import time

class auth:

    def get_hwid():
        c = wmi.WMI()
        hwid = None

        try:
            # Retrieve the HWID using the Win32_ComputerSystemProduct class
            computer_system_product = c.Win32_ComputerSystemProduct()[0]
            hwid = computer_system_product.UUID
        except Exception as e:
            print("Error retrieving HWID:", e)

        return hwid

    def authenticate(hwid, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                hwids_data = json.loads(response.text)

                if hwid in hwids_data["hwids"]:
                    pass
                else:
                    print("Authentication Error, hwid not found!")
                    time.sleep(2.5)
                    os._exit(0)
            else:
                print("Failed to fetch HWID data from the URL")
        except Exception as e:
            print("Error:", e)
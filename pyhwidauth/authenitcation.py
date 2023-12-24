import wmi
import json
import requests

def _get_hwid():
    try:
        computer_system_product = wmi.WMI().Win32_ComputerSystemProduct()[0]
        return computer_system_product.UUID
    except Exception as e:
        return e

def _get_nested_key(data, keys):
    try:
        for key in keys:
            data = data[key]
        return data
    except KeyError:
        return []

def _url_authenticate(hwid, url, keys):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            hwids_data = json.loads(response.text)
            nested_key_data = _get_nested_key(hwids_data, keys)
            if hwid in nested_key_data:
                return(True)
            else:
                return(False)
        else:
            return(f"Status Code: {str(response.status_code)}")
    except Exception as e:
        return e

def _file_authenticate(hwid, file_path, keys):
    try:
        with open(file_path, 'r') as file:
            hwids_data = json.load(file)
            nested_key_data = _get_nested_key(hwids_data, keys)
            if hwid in nested_key_data:
                return(True)
            else:
                return(False)
    except Exception as e:
        return e
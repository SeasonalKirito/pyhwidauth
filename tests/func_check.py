from pyhwidauth import _get_hwid, _url_authenticate, _file_authenticate

print(_url_authenticate("test_hwid", "https://raw.githubusercontent.com/SeasonalKirito/pyhwidauth/main/tests/hwids.json", ["hwids"]))
print(_file_authenticate("test_hwid", "hwids.json", ["hwids"]))
## PYHwidAuth 💾
PYHwidAuth is your assistant in getting you HWID and Verifying 
it in url and file format. (Perferred JSON Format) 🤖
## Installation 📩
Tested on Newest Python Versions, There is only one requirement for this code ✅
```cmd
pip install wmi
pip install git+https://github.com/SeasonalKirito/pyhwidauth.git
```
This pakage is not on pypi at this moment and will not have a ETA on pypi ⌚
## How it works 💽
PYHwidAuth is using two different types of checks (url, file) and checks if the given hwid is in the (url, or file). 📨
## Usage
To define and use all its functions you will do this -|
```py
from pyhwidauth import _get_hwid, _url_authenticate, _file_authenticate
```
 
---
 
Input - 🔤
```py
from pyhwidauth import _get_hwid, _url_authenticate, _file_authenticate

print(_url_authenticate("test_hwid", "https://raw.githubusercontent.com/SeasonalKirito/pyhwidauth/main/tests/hwids.json", ["hwids"]))
print(_file_authenticate("test_hwid", "hwids.json", ["hwids"]))
```
Output - 🔢
```cmd
True
True
```

"""
python creat pip.ini.py
2016-4-30 03:35:11 codegay
"""

import os

ini="""[global]
index-url = https://pypi.doubanio.com/simple/
[install]
trusted-host=pypi.doubanio.com
"""
pippath=os.environ["USERPROFILE"]+"\\pip\\"

if not os.path.exists(pippath):
    os.mkdir(pippath)

with open(pippath+"pip.ini","w+") as f:
    f.write(ini)

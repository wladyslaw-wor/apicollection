import os

os.system("systemctl daemon-reload")
os.system("systemctl restart gunicorn-apicollection")
os.system("systemctl restart nginx")
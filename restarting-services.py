import os

os.system("systemctl daemon-reload")
os.system("echo Restarting daemon: DONE")
os.system("systemctl restart gunicorn-apicollection")
os.system("echo Restarting gunicorn-apicollection: DONE")
os.system("systemctl restart nginx")
os.system("echo Restarting nginx: DONE")
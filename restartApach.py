import subprocess


def restart():
    subprocess.call('sudo systemctl restart httpd',shell=True)


restart()

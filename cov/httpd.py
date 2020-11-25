import subprocess


def restart():
    subprocess.call('sudo systemctl restart httpd',shell=True)


def reload():
    subprocess.call('sudo systemctl reload httpd', shell=True)


def stop():
    subprocess.call('sudo systemctl stop httpd', shell=True)


def start():
    subprocess.call('sudo systemctl start httpd', shell=True)
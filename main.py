# import requests
# import config
# import helper
from pathlib import Path
import pymailtm

account = pymailtm.MailTm().get_account()

# print(account)

print(Path.home())
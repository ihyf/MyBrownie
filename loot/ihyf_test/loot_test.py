import json

from brownie import *
# import brownie.project as project
# from brownie import network
import time
from eth_utils import to_hex, keccak
import base64

"""
ganache-cli --accounts 10 --defaultBalanceEther 10000 --fork https://bsc-dataseed.binance.org --mnemonic brownie --port 8545 --hardfork istanbul"""
"""
https://www.lootproject.com/
"""
p = project.load('/Users/rome/Desktop/ihyf/code/MyBrownie/loot', name="loot")
p.load_config()
network.connect('MyBsc4')

loot = p.Loot.deploy({'from': accounts[0]})

# print(loot.address)

loot.claim(1)
data = loot.tokenURI(1)
data0, data1 = data.split(",")
uri_json = base64.b64decode(data1)
uri_json = eval(uri_json)
print(uri_json["name"])
print(uri_json["description"])
print(uri_json["image"])

img_head, img_data = uri_json["image"].split(",")
img = base64.b64decode(img_data)
print(img)

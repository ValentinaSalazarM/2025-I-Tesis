from fastecdsa import keys
from fastecdsa.curve import Curve, P256
from fastecdsa.point import Point
from Crypto import Random
from Crypto.Util.Padding import unpad, pad
from Crypto.Cipher import AES

from ecdsa import SigningKey
from ecdsa.util import PRNG

import hashlib

import binascii
import logging
import random
import socket
import base64
import time
import json
import os

def Hash(*dataListByte):
    h = hashlib.new("sha256")
    Mydata = b""
    for data in dataListByte:
        Mydata = Mydata + data.to_bytes(32, "big")
    h.update(Mydata)
    HashResult = h.hexdigest()
    HashInt = int(HashResult, 16)
    Hash_value = HashInt % P256.q
    return Hash_value

def Hash_MAPFS(dataListByte):
    h = hashlib.new("sha256")
    result = dataListByte[0].to_bytes(32, 'big')
    for i in range(1, len(dataListByte)):
        result += (dataListByte[i].to_bytes(32, 'big'))
    h.update(result)
    HashResult = h.hexdigest()
    HashInt = int(HashResult, 16)
    Hash_value = HashInt % P256.q
    return Hash_value

def FPUF(Challenge):
    h = hashlib.new("sha256")
    h.update(Challenge.to_bytes(32, "big"))
    HashResult = h.hexdigest()
    HashInt = int(HashResult, 16)
    Response = HashInt % 90000 + 10000
    time.sleep(2.2 / 1000)
    return Response


def DPUF(Challenge, state):
    h = hashlib.new("sha256")
    h.update(Challenge.to_bytes(32, "big") + state.to_bytes(32, "big"))
    HashResult = h.hexdigest()
    HashInt = int(HashResult, 16)
    Response = HashInt % 90000 + 10000
    time.sleep(3.3 / 1000)
    return Response


def truncate_to_16_digits(number):
    # Convertir el número a cadena
    number_str = str(number)
    # Tomar solo los primeros 16 caracteres
    truncated_str = number_str[:16]
    # Convertirlo nuevamente a número (opcional)
    truncated_number = int(truncated_str)
    return truncated_number

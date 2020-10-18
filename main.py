from hashlib import md5

from Account import Account
from Server.Server import Server

matt = Account("Mattias", "klutten99", md5(b"mattias123"))
osk = Account("Oskar", "MrW", md5(b"oskar123"))

srv = Server()

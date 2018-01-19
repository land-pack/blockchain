from bitcointools import random_key
from bitcointools import privtopub
from bitcointools import pubtoaddr
from bitcointools import sha256
from bitcointools import history

#priv = random_key()

priv = sha256("bticoin is ")


pub = privtopub(priv)

print(pub)


addr = pubtoaddr(pub)

print(addr)

print(history(addr))

import os
import sys
from os.path import isfile, join
from scapy.all import *

load_layer('tls')

cap = rdpcap('./encrypted.pcap')

publickey = TLS(cap[5].load)[4].msg[0].certs[0][1].x509Cert
pubmod = publickey[X509_TBSCertificate].subjectPublicKeyInfo.subjectPublicKey.modulus.val
pubexp = publickey[X509_TBSCertificate].subjectPublicKeyInfo.subjectPublicKey.publicExponent.val

files = [join("./keys", f)
         for f in os.listdir("./keys/") if isfile(join("./keys/", f))]
for keyfile in files:
    f = PrivKey(keyfile)
    if f._modulus == pubmod and f._pubExp == pubexp:
        print(keyfile)

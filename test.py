import pyshark, os

CAPTURE_PATH = 'captures/ShadowWIFI-Login-Upload-Download.pcap'
override_prefs={'tls.keylog_file': os.path.abspath('keys/ShadowWIFI-Login-Upload-Download')}

cap = pyshark.FileCapture(CAPTURE_PATH, override_prefs=override_prefs, display_filter='tcp && ip.addr==46.105.132.156')

packet_sizes = []

record = False
for packet in cap:
    if packet.tcp.seq != "25660": continue
    print([str(x) == "<TLS Layer>" for x in packet.layers])
    exit()
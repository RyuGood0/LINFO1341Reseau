import pyshark, os

CAPTURE_PATH = 'captures/ShadowWIFI-Login-Upload-Download.pcap'
override_prefs={'tls.keylog_file': os.path.abspath('keys/ShadowWIFI-Login-Upload-Download')}

cap = pyshark.FileCapture(CAPTURE_PATH, override_prefs=override_prefs, display_filter='tcp && ip.addr==46.105.132.156')

packet_sizes = []

record = False
for packet in cap:
    if packet.ip.src != "192.168.1.34": continue
    
    # get packet with SEQ 2462
    if packet.tcp.seq == "2462":
        record = True

    if record:
        packet_sizes.append(int(packet.length))

    if packet.tcp.seq == "4901342":
        break

# print avg, uniques, total
print("Average packet size: ", sum(packet_sizes) / len(packet_sizes))

packet_size_set = set(packet_sizes)
print("Unique packet sizes: ", len(packet_size_set))
# count for each packet size
for packet_size in packet_size_set:
    packet_sizes_count = packet_sizes.count(packet_size)
    print("Packet size: ", packet_size, " count: ", packet_sizes_count)

print("Total packets: ", len(packet_sizes))
print("Total bytes: ", sum(packet_sizes))
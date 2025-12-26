import sys

def convert_to_le_hex(text):
    if len(text) < 8:
        text = '/' * (8 - len(text)) + text
        print(f"[*] Adjusted text: {text}")
    if len(text) > 8:
        print("[!] Warning: Text is longer than 8 bytes. Only first 8 bytes used.")
        text = text[:8]
    
    # ascii => hex => reverse(le)
    le_hex = "0x" + "".join([f"{ord(c):02x}" for c in reversed(text)])
    print("-" * 30)
    print(f"Original:  {text}")
    print(f"LE Hex:    {le_hex}")
    print("-" * 30)
    print(f"\nAssembly line:\nmov rbx, {le_hex}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 str_to_le.py <Text>")
    else:
        convert_to_le_hex(sys.argv[1])
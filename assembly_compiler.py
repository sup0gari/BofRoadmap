import sys
from pwn import *

def compile_assembly(input_file):

    # x86-64 linux
    context.update(arch='amd64', os='linux')
    try:
        with open(input_file, "r") as f:
            assembly_code = f.read()

        binary_payload = asm(assembly_code)
        hex_string = "".join([f"\\x{b:02x}" for b in binary_payload])

        print(f"\n[+] File: {input_file} ({len(binary_payload)} bytes)")
        print("-" * 40)
        print(f'shellcode = b"{hex_string}"')
        print("-" * 40)
    except FileNotFoundError:
        print(f"[-] Error: '{input_file}' not found.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 assembly_compiler.py <input.asm>")
    else:
        compile_assembly(sys.argv[1])
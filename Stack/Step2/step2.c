#include <stdio.h>
#include <string.h>

void vuln() {
    char buffer[64];
    printf("Buffer address: %p\n", buffer);
    printf("Give me your shellcode: ");
    gets(buffer);
}

int main() {
    vuln();
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void vuln_func() {
    char buffer[64];
    printf("Input data: \n");
    read(0, buffer, 256); // ここでbofを起こしてretしたときのアドレスをmainからガジェットに飛ばす。
}

int main() {
    vuln_func();
    return 0;
}
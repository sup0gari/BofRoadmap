#include <stdio.h>
#include <stdlib.h>

// これを呼べばBOF完了とする
void win() {
    printf("\n[!] SUCCESS: win() function called. BOF done.\n");
    exit(0);
}

int main() {
    char buffer[32];

    printf("win() function is at: %p\n", win);
    printf("Input something: ");

    // 入力サイズをチェックしていない脆弱性
    gets(buffer);

    printf("You entered: %s\n", buffer);

    return 0;
}
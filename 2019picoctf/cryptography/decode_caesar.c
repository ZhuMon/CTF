#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char *cipher = "UFJKXQZQUNB";
    char *key = "SOLVECRYPTO";

    for (; *cipher != '\0'; cipher++) {
        if (*cipher == '{' || *cipher == '}' || *cipher == ' ') {
            printf("%c", *cipher);
            continue;
        }
        printf("%c", ((*cipher - 65) - (*key - 65) + 26) % 26 + 65);
        key++;
    }
    printf("\n");
    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// not success
int main(int argc, char *argv[]){
    char *ascii = "080485e6";
    char str[4];
    // str = malloc((strlen(ascii) / 2) * sizeof(char));
    for (int i = 0; i < 8; i += 2) {
        char mono_char[2];
        mono_char[0] = *(ascii + i);
        mono_char[1] = *(ascii + i + 1);
        printf("%s\n", mono_char);

        str[i / 2] = atoi(mono_char);
        // sprintf(str, "%s%c", str, atoi(mono_char));
        // str = strcat(str, atoi(mono_char));
    }
    printf("%s\n", str);
    return 0;
}

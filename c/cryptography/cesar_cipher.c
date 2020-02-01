#include <stdio.h>
#include <string.h>


char shift_char(char ch, int key){
    // shift character by key
    return (char)(ch + key);
}

char unshift_char(char ch, int key){
    // unshift charcter by key
    return (char)(ch - key);
}

void cesar_encrypt(char *message, int key){
    if ( key < 0 || key > 26){
        printf("Error Encryption: Encryption key should be in range(0,26) included\n");
        return;
    }

    while (*message){
        *message = shift_char(*message, key);
        message++;
    }
}

void cesar_decrypt(char *message, int key){
    if (key < 0 || key > 26){
        printf("Error Decryption: Decryption key should be in range(0,26) included\n");
        return;
    }

    while (*message){
        *message = unshift_char(*message, key);
        message++;
    }
}

int main(){
    printf("Cryptography: Cesar Cipher\n");

    char str[] = "abcdefgh234@#";
    int key = 2;

    printf("Encryption Key: %d\n", key);
    printf("Before Encryption: %s\n", str);
    cesar_encrypt(str, key);
    printf("After Encryption: %s\n", str);
    cesar_decrypt(str, key);
    printf("After Decryption: %s\n", str);
    return 0;
}

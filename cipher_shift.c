#include "stdio.h"
#define BUFFERSIZE 40

char* poorly_encrypt(char *pStr, char *pDest, int string_size) {
  // encrypts a string using a one ascii char shift cipher
  //
  // fill encrypted string with ascii char one shift away from original char
  for (int i = 0; i < string_size; i++) {
    pDest[i] = 1 + *(pStr + i);
  }

  // debug
  printf("%c %s %p \n", *pDest, pDest, &pDest);

  return pDest;
}

int main() {
  char username[] = "john smith";
  char password[] = "abc123";
  char bufferUsername[BUFFERSIZE] = {0};
  char bufferPassword[BUFFERSIZE] = {0};

  // debug
  printf("%c %s %p \n", *username, username, &username);
  printf("%c %s %p \n", *password, password, &password);

  char *pEncrypted_username;
  char *pEncrypted_password;

  if ( (sizeof(bufferUsername) > sizeof(username)) &&
       (sizeof(bufferPassword) > sizeof(password))
     ) {
    pEncrypted_username = poorly_encrypt(username, bufferUsername, sizeof(username));
    pEncrypted_password = poorly_encrypt(password, bufferPassword, sizeof(password));

    printf("Your poorly encrypted username is: %s \n", pEncrypted_username);
    printf("Your poorly encrypted password is: %s \n", pEncrypted_password);
  } else {
    printf("%s %s %d buffer is too small!", __FILE__, __func__, __LINE__);
  }

  return 0;
}

#include<stdio.h>
#include<string.h>
int main(){
char msg[100]; int i;
printf("Enter message:");
scanf(" %[^\n]", msg); 
for(i=0;msg[i];i++) msg[i]+=3;
printf("Encrypted:%s\n",msg);
for(i=0;msg[i];i++) msg[i]-=3;
printf("Decrypted:%s",msg);
}

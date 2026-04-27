#include<stdio.h>
#include<string.h>
int main() {
char d[50];
int c,i,n=0;
printf("Enter Data: ");
scanf("%s", d);
printf("1.count 2.charstuff 3.bitstuff\n");
scanf("%d",&c);
if(c==1) {
printf("Frame:  %lu %s", strlen(d)+1,d);
}
else if(c==2) {
printf("FLAG");
for(i=0;i<strlen(d);i++) {
if(d[i]=='F') 
printf("ESC");
printf("%c",d[i]);
}
printf("FLAG\n");
}
else if(c==3) {
for(i=0;i<strlen(d);i++){
printf("%c",d[i]);
if(d[i]=='1') {
n++;
if(n==5){
printf("0");
n=0;
}
}
else {
n=0;
}
}
printf("\n");
}
return 0;
}

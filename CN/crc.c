#include<stdio.h>
#include<string.h>
int main(){
char d[100],k[20],t[120];
int i,j,n,m,c;
printf("Enter Data: ");
scanf("%s",d);
printf("1.CRC-12 2.CRC-16 3.CRC-CCITT\n");
scanf("%d",&c);
if(c==1) strcpy(k,"1100000001111");
else if(c==2) strcpy(k,"11000000000000101");
else strcpy(k,"10001000000100001");
n=strlen(d); 
m=strlen(k);
strcpy(t,d);
for(i=0;i<m-1;i++) 
t[n+i]='0';
t[n+m-1]='\0';
for(i=0;i<n;i++)
if(t[i]=='1')
for(j=0;j<m;j++)
t[i+j]=(t[i+j]==k[j])?'0':'1';
for(i=n;i<n+m-1;i++) 
printf("%c",t[i]);
return 0;
}

#include<stdio.h>
int main(){
int bucket=10,rate=3,pkt,i;
for(i=0;i<5;i++){
printf("Enter packet:");
scanf("%d",&pkt);
if(pkt>bucket) printf("Dropped\n");
else printf("Accepted\n");
}
}

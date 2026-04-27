#include<stdio.h>
int main(){
 int sent,recv;
 scanf("%d%d",&sent,&recv);
 printf("Dropped=%d\n",sent-recv);
 printf("Throughput=%f",(float)recv/sent);
}

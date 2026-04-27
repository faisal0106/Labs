#include<stdio.h>
int main(){
 int ports[]={21,22,80,443},i;
 for(i=0;i<4;i++)
  printf("Port %d OPEN\n",ports[i]);
}

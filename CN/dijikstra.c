#include <stdio.h>
int main() {
    int d[3][3] = {
        {0,1,4},
        {1,0,2},
        {4,2,0}
    };
    int dist[3], v[3]={0};
    int i,j,u,min;
    for(i=0;i<3;i++) dist[i]=d[0][i];
    v[0]=1;
    for(i=1;i<3;i++) {
        min=999;
        for(j=0;j<3;j++)
            if(!v[j] && dist[j]<min) {
                min=dist[j];
                u=j;
            }
        v[u]=1;
        for(j=0;j<3;j++)
            if(!v[j] && dist[j]>dist[u]+d[u][j])
                dist[j]=dist[u]+d[u][j];
    }
    for(i=0;i<3;i++)
        printf("%d ",dist[i]);
    return 0;
}

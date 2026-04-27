#include<stdio.h>
int main() {
    int d[3][3] = {
        {0,1,4},
        {1,0,2},
        {4,2,0}
    };
    int i,j,k;
    for(k=0;k<3;k++)
        for(i=0;i<3;i++)
            for(j=0;j<3;j++)
                if(d[i][j] > d[i][k] + d[k][j])
                    d[i][j] = d[i][k] + d[k][j];
    for(i=0;i<3;i++) {
        printf("Node %d:\n", i);
        for(j=0;j<3;j++)
            printf("%d ", d[i][j]);
        printf("\n");
    }
    return 0;
}

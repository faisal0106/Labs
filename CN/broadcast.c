#include <stdio.h>
int main() {
    int g[5][5] = {
        {0,1,1,0,0},
        {1,0,0,1,1},
        {1,0,0,0,1},
        {0,1,0,0,0},
        {0,1,1,0,0}
    };
    int visited[5] = {0};
    int q[5], front = 0, rear = 0;
    visited[0] = 1;
    q[rear++] = 0;
    while (front < rear) {
        int u = q[front++];
        for (int v = 0; v < 5; v++) {
            if (g[u][v] && !visited[v]) {
                visited[v] = 1;
                printf("%c -> %c\n", u+'A', v+'A');
                q[rear++] = v;
            }
        }
    }
    return 0;
}

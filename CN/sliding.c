#include <stdio.h>
int main() {
int i = 0, j, w, n, ack;
printf("Frames and Window: ");
scanf("%d%d", &n, &w);
while(i < n) {
printf("Sending: ");
for(j = 0; j < w && (i + j) < n; j++)
printf("%d ", i + j);
printf("\nAck: ");
scanf("%d", &ack);
if(ack == i) {
printf("Lost! Resend\n");
} else {
i = ack;
}
}
return 0;
}

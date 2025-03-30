#include <stdio.h>
#include <stdlib.h>

int main() {
    int N;
    scanf("%d", &N);

    double* list = (double*)malloc(sizeof(double) * N);

    for (int i = 0; i < N; i++) {
        scanf("%lf", &list[i]);
    }

    double max = list[0];
    for (int i = 1; i < N; i++) {
        if (list[i - 1] > 1) {
            list[i] = list[i] * list[i - 1];
        }

        if (list[i] > max) max = list[i];
    }

    printf("%.3f", max);
}
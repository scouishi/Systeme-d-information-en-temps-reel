#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define TAILLE 8000

void tache_1() {
    long long int *a1 = malloc(TAILLE*sizeof(long long int));
    long long int *a2 = malloc(TAILLE*sizeof(long long int));
    long long int *resultat = malloc(TAILLE*sizeof(long long int));

    for(int i = 0; i < TAILLE; i++) {
        a1[i] = rand()%100000;
        a2[i] = rand()%100000;
    }

    for(int i = 0; i < TAILLE; i++) {
        resultat[i] = a1[i]*a2[i];
    }

    free(a1);
    free(a2);
    free(resultat);
}

int main() {
    srand(time(NULL));

    tache_1();

    return 0;
}

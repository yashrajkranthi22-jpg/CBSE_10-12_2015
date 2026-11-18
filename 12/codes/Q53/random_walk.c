#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ITERATIONS 10000
#define STEPS 5

int main()
{
    FILE *fp;
    int displacement;

    srand(time(NULL));

    fp = fopen("random_walk.dat", "w");

    if (fp == NULL)
    {
        printf("Error opening file.\n");
        return 1;
    }

    for (int i = 0; i < ITERATIONS; i++)
    {
        displacement = 0;

        // Perform five steps in each experiment.
        for (int j = 0; j < STEPS; j++)
        {
            if ((double)rand() / ((double)RAND_MAX + 1.0) < 0.5)
                displacement++;
            else
                displacement--;
        }

        // Save the net displacement.
        fprintf(fp, "%d\n", displacement);
    }

    fclose(fp);

    printf("10000 experiments completed.\n");
    printf("Results saved in random_walk.dat\n");

    return 0;
}

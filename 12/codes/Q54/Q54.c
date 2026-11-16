#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ITERATIONS 10000

int main()
{
    srand(time(NULL));

    int evidence_count = 0;
    int favorable_count = 0;

    FILE *fp = fopen("simulation.csv", "w");

    if (fp == NULL)
    {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(fp, "iteration,experimental_probability\n");

    for (int i = 1; i <= ITERATIONS; i++)
    {
        int die = rand() % 6 + 1;

        int tosses;

        if (die == 1 || die == 2)
            tosses = 3;
        else
            tosses = 1;

        int tails = 0;

        for (int j = 0; j < tosses; j++)
        {
            int coin = rand() % 2;

            if (coin == 1)
                tails++;
        }

        if (tails == 1)
        {
            evidence_count++;

            if (die >= 3)
                favorable_count++;
        }

        if (evidence_count > 0)
        {
            double probability =
                (double)favorable_count / evidence_count;

            fprintf(fp, "%d,%.8f\n", i, probability);
        }
        else
        {
            fprintf(fp, "%d,nan\n", i);
        }
    }

    fclose(fp);

    printf("Total iterations: %d\n", ITERATIONS);
    printf("Experiments with exactly one tail: %d\n",
           evidence_count);
    printf("Favorable experiments: %d\n",
           favorable_count);

    if (evidence_count > 0)
    {
        printf("Experimental probability: %.6f\n",
               (double)favorable_count / evidence_count);
    }

    printf("Theoretical probability: %.6f\n", 8.0 / 11.0);

    return 0;
}

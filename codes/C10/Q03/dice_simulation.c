#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Generates a fair random integer between 1 and 6. */
int roll_die(void)
{
    unsigned long long range = (unsigned long long)RAND_MAX + 1ULL;
    unsigned long long limit = range - (range % 6ULL);
    unsigned long long value;

    /* Rejection sampling avoids modulo bias. */
    do
    {
        value = (unsigned long long)rand();
    } while (value >= limit);

    return (int)(value % 6ULL) + 1;
}

int main(void)
{
    const int ITERATIONS = 10000;

    int die1, die2, product;

    /* Seed the random number generator. */
    srand((unsigned int)time(NULL));

    /* Open the data file for writing. */
    FILE *fp = fopen("dice_data.dat", "w");

    if (fp == NULL)
    {
        printf("Error: Could not create dice_data.dat\n");
        return 1;
    }

    /* Simulate 10,000 rolls of two dice. */
    for (int i = 0; i < ITERATIONS; i++)
    {
        die1 = roll_die();
        die2 = roll_die();

        product = die1 * die2;

        /* Store both dice outcomes and their product. */
        fprintf(fp, "%d %d %d\n", die1, die2, product);
    }

    fclose(fp);

    printf("Simulation completed successfully.\n");
    printf("%d iterations written to dice_data.dat\n", ITERATIONS);

    return 0;
}

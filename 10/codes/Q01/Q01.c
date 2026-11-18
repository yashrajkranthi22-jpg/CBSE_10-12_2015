#include <stdio.h>
#include <math.h>

double F(double x)
{
    return x * (x - 3.0);
}

double dF(double x)
{
    return 2.0 * x - 3.0;
}

int main(void)
{
    double x = 4.0;
    double x_next;
    double tolerance = 1e-12;
    int converged = 0;

    printf("Newton-Raphson Method\n\n");

    printf("%-5s %-18s %-15s %-15s %-18s\n",
           "n", "x_n", "F(x_n)", "F'(x_n)", "x_(n+1)");

    for (int n = 0; n < 100; n++)
    {
        double fx = F(x);
        double dfx = dF(x);

        // Avoid division by zero near x = 3/2.
        if (fabs(dfx) < 1e-14)
        {
            printf("Derivative is too close to zero.\n");
            return 1;
        }

        // Newton-Raphson iteration.
        x_next = x - fx / dfx;

        printf("%-5d %-18.10f %-15.6e %-15.10f %-18.10f\n",
               n, x, fx, dfx, x_next);

        // Check convergence.
        if (fabs(x_next - x) < tolerance)
        {
            x = x_next;
            converged = 1;
            break;
        }

        x = x_next;
    }

    printf("\n");

    if (converged)
    {
        printf("Approximate root = %.12f\n", x);
        printf("F(root) = %.12e\n", F(x));

        if (fabs(x - 3.0) < tolerance)
        {
            printf("Verification successful: x = 3.\n");
        }
    }
    else
    {
        printf("Newton-Raphson method did not converge.\n");
    }

    return 0;
}

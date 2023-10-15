#include <stdio.h>
#include <math.h>
#include <stdlib.h> // for rand() and srand()
#include <time.h>   // for seeding the random number generator

// Define the CDF function for Y
double cdf_Y(double y) {
    return 1.0 - 1.0 / exp(y); // CDF of Y based on the given transformation
}

int main() {
    // Seed the random number generator
    srand(time(NULL));

    FILE *dataFile = fopen("cdf_data.txt", "w");

    if (!dataFile) {
        printf("Error: Could not open data file for writing.\n");
        return 1;
    }

    double y, cdf;

    // Generate random values of X from a uniform distribution [1, 5]
    // Then compute Y = log_e(X) and calculate the CDF of Y
    for (y = 0.0; y <= 5.0; y += 0.1) {
        double x = 1.0 + (4.0 * rand() / (double)RAND_MAX); // Generate random X from a uniform distribution [1, 5]
        double generated_Y = log(x); // Compute Y = log_e(X)
        double cdf_X = 1.0 - 1.0 / x; // CDF of X
        cdf = cdf_Y(generated_Y);
        fprintf(dataFile, "%.5f %.5f %.5f %.5f\n", x, cdf_X, generated_Y, cdf);
    }

    fclose(dataFile);

    printf("Data file 'cdf_data.txt' generated.\n");

    return 0;
}

#include <stdio.h>
#include <math.h>

// Define the PDF function
double pdf(double x) {
    if (x >= 1.0) {
        return 1.0 / (x * x);
    }
    return 0.0;
}

// Calculate the CDF of Y
double cdf_y(double y) {
    double sum = 0.0;
    double dx = 0.0001; // Small step size for numerical integration
    double x;

    for (x = 1.0; x <= exp(y); x += dx) {
        sum += pdf(x) * dx;
    }

    return sum;
}

int main() {
    FILE *dataFile = fopen("cdf_data.txt", "w");
    
    if (!dataFile) {
        printf("Error: Could not open data file for writing.\n");
        return 1;
    }

    double y, cdf;

    // Calculate and write the CDF data
    for (y = 0.0; y <= 5.0; y += 0.1) {
        cdf = cdf_y(y);
        fprintf(dataFile, "%.2f %.5f\n", y, cdf);
    }

    fclose(dataFile);

    printf("Data file 'cdf_data.txt' generated.\n");

    return 0;
}
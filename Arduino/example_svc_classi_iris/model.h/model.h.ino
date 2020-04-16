/**
 * Compute kernel between feature vector and support vector.
 * Kernel type: linear
 */
double compute_kernel(double x[4], ...) {
    va_list w;
    double kernel = 0.0;
    va_start(w, 4);
    for (uint16_t i = 0; i < 4; i++)
            kernel += x[i] *  va_arg(w, double) ;
    return kernel;
}
/**
 * Predict class for features vector
 */
int predict(double *x) {
    double kernels[27] = { 0 };
    double decisions[3] = { 0 };
    int votes[3] = { 0 };
        kernels[0] = compute_kernel(x,   5.1  , 3.3  , 1.7  , 0.5 );
        kernels[1] = compute_kernel(x,   4.8  , 3.4  , 1.9  , 0.2 );
        kernels[2] = compute_kernel(x,   4.5  , 2.3  , 1.3  , 0.3 );
        kernels[3] = compute_kernel(x,   6.9  , 3.1  , 4.9  , 1.5 );
        kernels[4] = compute_kernel(x,   6.3  , 3.3  , 4.7  , 1.6 );
        kernels[5] = compute_kernel(x,   6.1  , 2.9  , 4.7  , 1.4 );
        kernels[6] = compute_kernel(x,   5.6  , 3.0  , 4.5  , 1.5 );
        kernels[7] = compute_kernel(x,   6.2  , 2.2  , 4.5  , 1.5 );
        kernels[8] = compute_kernel(x,   5.9  , 3.2  , 4.8  , 1.8 );
        kernels[9] = compute_kernel(x,   6.3  , 2.5  , 4.9  , 1.5 );
        kernels[10] = compute_kernel(x,   6.8  , 2.8  , 4.8  , 1.4 );
        kernels[11] = compute_kernel(x,   6.7  , 3.0  , 5.0  , 1.7 );
        kernels[12] = compute_kernel(x,   6.0  , 2.7  , 5.1  , 1.6 );
        kernels[13] = compute_kernel(x,   5.4  , 3.0  , 4.5  , 1.5 );
        kernels[14] = compute_kernel(x,   5.1  , 2.5  , 3.0  , 1.1 );
        kernels[15] = compute_kernel(x,   4.9  , 2.5  , 4.5  , 1.7 );
        kernels[16] = compute_kernel(x,   6.5  , 3.2  , 5.1  , 2.0 );
        kernels[17] = compute_kernel(x,   6.0  , 2.2  , 5.0  , 1.5 );
        kernels[18] = compute_kernel(x,   6.3  , 2.7  , 4.9  , 1.8 );
        kernels[19] = compute_kernel(x,   6.2  , 2.8  , 4.8  , 1.8 );
        kernels[20] = compute_kernel(x,   6.1  , 3.0  , 4.9  , 1.8 );
        kernels[21] = compute_kernel(x,   7.2  , 3.0  , 5.8  , 1.6 );
        kernels[22] = compute_kernel(x,   6.3  , 2.8  , 5.1  , 1.5 );
        kernels[23] = compute_kernel(x,   6.0  , 3.0  , 4.8  , 1.8 );
        kernels[24] = compute_kernel(x,   6.3  , 2.5  , 5.0  , 1.9 );
        kernels[25] = compute_kernel(x,   6.5  , 3.0  , 5.2  , 2.0 );
        kernels[26] = compute_kernel(x,   5.9  , 3.0  , 5.1  , 1.8 );
        decisions[0] = 1.452844497
                    + kernels[0] * 0.67075289
                    + kernels[2] * 0.077097563
                    + kernels[14] * -0.747850454
        ;
        decisions[1] = 1.507713125
                    + kernels[0] * 0.043820415
                    + kernels[1] * 0.159872087
                    + kernels[15] * -0.203692502
        ;
        decisions[2] = 6.780971185
                    + kernels[3]
                    + kernels[4]
                    + kernels[5]
                    + kernels[6]
                    + kernels[7]
                    + kernels[8]
                    + kernels[9]
                    + kernels[10] * 0.243261886
                    + kernels[11]
                    + kernels[12]
                    + kernels[13]
                    - kernels[15]
                    - kernels[16]
                    - kernels[17]
                    - kernels[18]
                    - kernels[19]
                    - kernels[20]
                    + kernels[21] * -0.437859818
                    - kernels[22]
                    - kernels[23]
                    + kernels[24] * -0.645105348
                    + kernels[25] * -0.160296721
                    - kernels[26]
        ;
        votes[decisions[0] > 0 ? 0 : 1] += 1;
        votes[decisions[1] > 0 ? 0 : 2] += 1;
        votes[decisions[2] > 0 ? 1 : 2] += 1;
                int classVal = -1;
        int classIdx = -1;
        for (int i = 0; i < 3; i++) {
            if (votes[i] > classVal) {
                classVal = votes[i];
                classIdx = i;
            }
        }
        return classIdx;
}

#pragma once
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
    double kernels[119] = { 0 };
    double decisions[3] = { 0 };
    int votes[3] = { 0 };
        kernels[0] = compute_kernel(x,   4.9  , 3.0  , 1.4  , 0.2 );
        kernels[1] = compute_kernel(x,   4.6  , 3.1  , 1.5  , 0.2 );
        kernels[2] = compute_kernel(x,   5.4  , 3.9  , 1.7  , 0.4 );
        kernels[3] = compute_kernel(x,   4.9  , 3.1  , 1.5  , 0.1 );
        kernels[4] = compute_kernel(x,   5.4  , 3.7  , 1.5  , 0.2 );
        kernels[5] = compute_kernel(x,   4.8  , 3.4  , 1.6  , 0.2 );
        kernels[6] = compute_kernel(x,   5.7  , 3.8  , 1.7  , 0.3 );
        kernels[7] = compute_kernel(x,   5.4  , 3.4  , 1.7  , 0.2 );
        kernels[8] = compute_kernel(x,   5.1  , 3.7  , 1.5  , 0.4 );
        kernels[9] = compute_kernel(x,   5.1  , 3.3  , 1.7  , 0.5 );
        kernels[10] = compute_kernel(x,   4.8  , 3.4  , 1.9  , 0.2 );
        kernels[11] = compute_kernel(x,   5.0  , 3.0  , 1.6  , 0.2 );
        kernels[12] = compute_kernel(x,   5.0  , 3.4  , 1.6  , 0.4 );
        kernels[13] = compute_kernel(x,   5.2  , 3.5  , 1.5  , 0.2 );
        kernels[14] = compute_kernel(x,   4.7  , 3.2  , 1.6  , 0.2 );
        kernels[15] = compute_kernel(x,   4.8  , 3.1  , 1.6  , 0.2 );
        kernels[16] = compute_kernel(x,   5.4  , 3.4  , 1.5  , 0.4 );
        kernels[17] = compute_kernel(x,   4.9  , 3.1  , 1.5  , 0.1 );
        kernels[18] = compute_kernel(x,   4.9  , 3.1  , 1.5  , 0.1 );
        kernels[19] = compute_kernel(x,   5.1  , 3.4  , 1.5  , 0.2 );
        kernels[20] = compute_kernel(x,   4.5  , 2.3  , 1.3  , 0.3 );
        kernels[21] = compute_kernel(x,   5.0  , 3.5  , 1.6  , 0.6 );
        kernels[22] = compute_kernel(x,   5.1  , 3.8  , 1.9  , 0.4 );
        kernels[23] = compute_kernel(x,   4.8  , 3.0  , 1.4  , 0.3 );
        kernels[24] = compute_kernel(x,   7.0  , 3.2  , 4.7  , 1.4 );
        kernels[25] = compute_kernel(x,   6.4  , 3.2  , 4.5  , 1.5 );
        kernels[26] = compute_kernel(x,   6.9  , 3.1  , 4.9  , 1.5 );
        kernels[27] = compute_kernel(x,   5.5  , 2.3  , 4.0  , 1.3 );
        kernels[28] = compute_kernel(x,   6.5  , 2.8  , 4.6  , 1.5 );
        kernels[29] = compute_kernel(x,   5.7  , 2.8  , 4.5  , 1.3 );
        kernels[30] = compute_kernel(x,   6.3  , 3.3  , 4.7  , 1.6 );
        kernels[31] = compute_kernel(x,   4.9  , 2.4  , 3.3  , 1.0 );
        kernels[32] = compute_kernel(x,   6.6  , 2.9  , 4.6  , 1.3 );
        kernels[33] = compute_kernel(x,   5.2  , 2.7  , 3.9  , 1.4 );
        kernels[34] = compute_kernel(x,   5.0  , 2.0  , 3.5  , 1.0 );
        kernels[35] = compute_kernel(x,   5.9  , 3.0  , 4.2  , 1.5 );
        kernels[36] = compute_kernel(x,   6.0  , 2.2  , 4.0  , 1.0 );
        kernels[37] = compute_kernel(x,   6.1  , 2.9  , 4.7  , 1.4 );
        kernels[38] = compute_kernel(x,   5.6  , 2.9  , 3.6  , 1.3 );
        kernels[39] = compute_kernel(x,   6.7  , 3.1  , 4.4  , 1.4 );
        kernels[40] = compute_kernel(x,   5.6  , 3.0  , 4.5  , 1.5 );
        kernels[41] = compute_kernel(x,   5.8  , 2.7  , 4.1  , 1.0 );
        kernels[42] = compute_kernel(x,   6.2  , 2.2  , 4.5  , 1.5 );
        kernels[43] = compute_kernel(x,   5.6  , 2.5  , 3.9  , 1.1 );
        kernels[44] = compute_kernel(x,   5.9  , 3.2  , 4.8  , 1.8 );
        kernels[45] = compute_kernel(x,   6.1  , 2.8  , 4.0  , 1.3 );
        kernels[46] = compute_kernel(x,   6.3  , 2.5  , 4.9  , 1.5 );
        kernels[47] = compute_kernel(x,   6.1  , 2.8  , 4.7  , 1.2 );
        kernels[48] = compute_kernel(x,   6.4  , 2.9  , 4.3  , 1.3 );
        kernels[49] = compute_kernel(x,   6.6  , 3.0  , 4.4  , 1.4 );
        kernels[50] = compute_kernel(x,   6.8  , 2.8  , 4.8  , 1.4 );
        kernels[51] = compute_kernel(x,   6.7  , 3.0  , 5.0  , 1.7 );
        kernels[52] = compute_kernel(x,   6.0  , 2.9  , 4.5  , 1.5 );
        kernels[53] = compute_kernel(x,   5.7  , 2.6  , 3.5  , 1.0 );
        kernels[54] = compute_kernel(x,   5.5  , 2.4  , 3.8  , 1.1 );
        kernels[55] = compute_kernel(x,   5.5  , 2.4  , 3.7  , 1.0 );
        kernels[56] = compute_kernel(x,   5.8  , 2.7  , 3.9  , 1.2 );
        kernels[57] = compute_kernel(x,   6.0  , 2.7  , 5.1  , 1.6 );
        kernels[58] = compute_kernel(x,   5.4  , 3.0  , 4.5  , 1.5 );
        kernels[59] = compute_kernel(x,   6.0  , 3.4  , 4.5  , 1.6 );
        kernels[60] = compute_kernel(x,   6.7  , 3.1  , 4.7  , 1.5 );
        kernels[61] = compute_kernel(x,   6.3  , 2.3  , 4.4  , 1.3 );
        kernels[62] = compute_kernel(x,   5.6  , 3.0  , 4.1  , 1.3 );
        kernels[63] = compute_kernel(x,   5.5  , 2.5  , 4.0  , 1.3 );
        kernels[64] = compute_kernel(x,   5.5  , 2.6  , 4.4  , 1.2 );
        kernels[65] = compute_kernel(x,   6.1  , 3.0  , 4.6  , 1.4 );
        kernels[66] = compute_kernel(x,   5.8  , 2.6  , 4.0  , 1.2 );
        kernels[67] = compute_kernel(x,   5.0  , 2.3  , 3.3  , 1.0 );
        kernels[68] = compute_kernel(x,   5.6  , 2.7  , 4.2  , 1.3 );
        kernels[69] = compute_kernel(x,   5.7  , 3.0  , 4.2  , 1.2 );
        kernels[70] = compute_kernel(x,   5.7  , 2.9  , 4.2  , 1.3 );
        kernels[71] = compute_kernel(x,   6.2  , 2.9  , 4.3  , 1.3 );
        kernels[72] = compute_kernel(x,   5.1  , 2.5  , 3.0  , 1.1 );
        kernels[73] = compute_kernel(x,   5.7  , 2.8  , 4.1  , 1.3 );
        kernels[74] = compute_kernel(x,   6.3  , 3.3  , 6.0  , 2.5 );
        kernels[75] = compute_kernel(x,   5.8  , 2.7  , 5.1  , 1.9 );
        kernels[76] = compute_kernel(x,   7.1  , 3.0  , 5.9  , 2.1 );
        kernels[77] = compute_kernel(x,   6.3  , 2.9  , 5.6  , 1.8 );
        kernels[78] = compute_kernel(x,   6.5  , 3.0  , 5.8  , 2.2 );
        kernels[79] = compute_kernel(x,   4.9  , 2.5  , 4.5  , 1.7 );
        kernels[80] = compute_kernel(x,   7.3  , 2.9  , 6.3  , 1.8 );
        kernels[81] = compute_kernel(x,   6.7  , 2.5  , 5.8  , 1.8 );
        kernels[82] = compute_kernel(x,   7.2  , 3.6  , 6.1  , 2.5 );
        kernels[83] = compute_kernel(x,   6.5  , 3.2  , 5.1  , 2.0 );
        kernels[84] = compute_kernel(x,   6.4  , 2.7  , 5.3  , 1.9 );
        kernels[85] = compute_kernel(x,   6.8  , 3.0  , 5.5  , 2.1 );
        kernels[86] = compute_kernel(x,   5.7  , 2.5  , 5.0  , 2.0 );
        kernels[87] = compute_kernel(x,   5.8  , 2.8  , 5.1  , 2.4 );
        kernels[88] = compute_kernel(x,   6.4  , 3.2  , 5.3  , 2.3 );
        kernels[89] = compute_kernel(x,   6.5  , 3.0  , 5.5  , 1.8 );
        kernels[90] = compute_kernel(x,   6.0  , 2.2  , 5.0  , 1.5 );
        kernels[91] = compute_kernel(x,   6.9  , 3.2  , 5.7  , 2.3 );
        kernels[92] = compute_kernel(x,   5.6  , 2.8  , 4.9  , 2.0 );
        kernels[93] = compute_kernel(x,   6.3  , 2.7  , 4.9  , 1.8 );
        kernels[94] = compute_kernel(x,   6.7  , 3.3  , 5.7  , 2.1 );
        kernels[95] = compute_kernel(x,   7.2  , 3.2  , 6.0  , 1.8 );
        kernels[96] = compute_kernel(x,   6.2  , 2.8  , 4.8  , 1.8 );
        kernels[97] = compute_kernel(x,   6.1  , 3.0  , 4.9  , 1.8 );
        kernels[98] = compute_kernel(x,   6.4  , 2.8  , 5.6  , 2.1 );
        kernels[99] = compute_kernel(x,   7.2  , 3.0  , 5.8  , 1.6 );
        kernels[100] = compute_kernel(x,   7.4  , 2.8  , 6.1  , 1.9 );
        kernels[101] = compute_kernel(x,   6.4  , 2.8  , 5.6  , 2.2 );
        kernels[102] = compute_kernel(x,   6.3  , 2.8  , 5.1  , 1.5 );
        kernels[103] = compute_kernel(x,   6.1  , 2.6  , 5.6  , 1.4 );
        kernels[104] = compute_kernel(x,   7.7  , 3.0  , 6.1  , 2.3 );
        kernels[105] = compute_kernel(x,   6.3  , 3.4  , 5.6  , 2.4 );
        kernels[106] = compute_kernel(x,   6.4  , 3.1  , 5.5  , 1.8 );
        kernels[107] = compute_kernel(x,   6.0  , 3.0  , 4.8  , 1.8 );
        kernels[108] = compute_kernel(x,   6.9  , 3.1  , 5.4  , 2.1 );
        kernels[109] = compute_kernel(x,   6.7  , 3.1  , 5.6  , 2.4 );
        kernels[110] = compute_kernel(x,   6.9  , 3.1  , 5.1  , 2.3 );
        kernels[111] = compute_kernel(x,   5.8  , 2.7  , 5.1  , 1.9 );
        kernels[112] = compute_kernel(x,   6.8  , 3.2  , 5.9  , 2.3 );
        kernels[113] = compute_kernel(x,   6.7  , 3.3  , 5.7  , 2.5 );
        kernels[114] = compute_kernel(x,   6.7  , 3.0  , 5.2  , 2.3 );
        kernels[115] = compute_kernel(x,   6.3  , 2.5  , 5.0  , 1.9 );
        kernels[116] = compute_kernel(x,   6.5  , 3.0  , 5.2  , 2.0 );
        kernels[117] = compute_kernel(x,   6.2  , 3.4  , 5.4  , 2.3 );
        kernels[118] = compute_kernel(x,   5.9  , 3.0  , 5.1  , 1.8 );
        decisions[0] = 1.927091981
                    + kernels[0] * 0.01
                    + kernels[1] * 0.01
                    + kernels[2] * 0.01
                    + kernels[3] * 0.01
                    + kernels[4] * 0.008325496
                    + kernels[5] * 0.01
                    + kernels[6] * 0.01
                    + kernels[7] * 0.01
                    + kernels[8] * 0.01
                    + kernels[9] * 0.01
                    + kernels[10] * 0.01
                    + kernels[11] * 0.01
                    + kernels[12] * 0.01
                    + kernels[13] * 0.01
                    + kernels[14] * 0.01
                    + kernels[15] * 0.01
                    + kernels[16] * 0.01
                    + kernels[17] * 0.01
                    + kernels[18] * 0.01
                    + kernels[19] * 0.01
                    + kernels[20] * 0.01
                    + kernels[21] * 0.01
                    + kernels[22] * 0.01
                    + kernels[23] * 0.01
                    + kernels[27] * -0.01
                    + kernels[31] * -0.01
                    + kernels[33] * -0.01
                    + kernels[34] * -0.01
                    + kernels[35] * -0.01
                    + kernels[36] * -0.01
                    + kernels[38] * -0.01
                    + kernels[41] * -0.01
                    + kernels[43] * -0.01
                    + kernels[45] * -0.01
                    + kernels[53] * -0.01
                    + kernels[54] * -0.01
                    + kernels[55] * -0.01
                    + kernels[56] * -0.01
                    + kernels[62] * -0.01
                    + kernels[63] * -0.01
                    + kernels[64] * -0.008325496
                    + kernels[66] * -0.01
                    + kernels[67] * -0.01
                    + kernels[68] * -0.01
                    + kernels[69] * -0.01
                    + kernels[70] * -0.01
                    + kernels[72] * -0.01
                    + kernels[73] * -0.01
        ;
        decisions[1] = 1.903052146
                    + kernels[2] * 0.01
                    + kernels[5] * 0.009057676
                    + kernels[6] * 0.01
                    + kernels[7] * 0.01
                    + kernels[9] * 0.01
                    + kernels[10] * 0.01
                    + kernels[11] * 0.01
                    + kernels[12] * 0.01
                    + kernels[14] * 0.01
                    + kernels[15] * 0.01
                    + kernels[16] * 0.01
                    + kernels[21] * 0.01
                    + kernels[22] * 0.01
                    + kernels[75] * -0.01
                    + kernels[79] * -0.01
                    + kernels[86] * -0.01
                    + kernels[90] * -0.01
                    + kernels[92] * -0.01
                    + kernels[93] * -0.01
                    + kernels[96] * -0.01
                    + kernels[97] * -0.01
                    + kernels[102] * -0.01
                    + kernels[107] * -0.01
                    + kernels[111] * -0.01
                    + kernels[115] * -0.009057676
                    + kernels[118] * -0.01
        ;
        decisions[2] = 4.290112142
                    + kernels[24] * 0.01
                    + kernels[25] * 0.01
                    + kernels[26] * 0.01
                    + kernels[27] * 0.01
                    + kernels[28] * 0.01
                    + kernels[29] * 0.01
                    + kernels[30] * 0.01
                    + kernels[32] * 0.01
                    + kernels[33] * 0.01
                    + kernels[35] * 0.01
                    + kernels[36] * 0.01
                    + kernels[37] * 0.01
                    + kernels[38] * 0.01
                    + kernels[39] * 0.01
                    + kernels[40] * 0.01
                    + kernels[41] * 0.01
                    + kernels[42] * 0.01
                    + kernels[43] * 0.01
                    + kernels[44] * 0.01
                    + kernels[45] * 0.01
                    + kernels[46] * 0.01
                    + kernels[47] * 0.01
                    + kernels[48] * 0.01
                    + kernels[49] * 0.01
                    + kernels[50] * 0.01
                    + kernels[51] * 0.01
                    + kernels[52] * 0.01
                    + kernels[54] * 0.01
                    + kernels[55] * 0.00980237
                    + kernels[56] * 0.01
                    + kernels[57] * 0.01
                    + kernels[58] * 0.01
                    + kernels[59] * 0.01
                    + kernels[60] * 0.01
                    + kernels[61] * 0.01
                    + kernels[62] * 0.01
                    + kernels[63] * 0.01
                    + kernels[64] * 0.01
                    + kernels[65] * 0.01
                    + kernels[66] * 0.01
                    + kernels[68] * 0.01
                    + kernels[69] * 0.01
                    + kernels[70] * 0.01
                    + kernels[71] * 0.01
                    + kernels[73] * 0.01
                    + kernels[74] * -0.01
                    + kernels[75] * -0.01
                    + kernels[76] * -0.01
                    + kernels[77] * -0.01
                    + kernels[78] * -0.01
                    + kernels[79] * -0.01
                    + kernels[80] * -0.01
                    + kernels[81] * -0.01
                    + kernels[82] * -0.01
                    + kernels[83] * -0.01
                    + kernels[84] * -0.01
                    + kernels[85] * -0.01
                    + kernels[86] * -0.01
                    + kernels[87] * -0.01
                    + kernels[88] * -0.01
                    + kernels[89] * -0.01
                    + kernels[90] * -0.01
                    + kernels[91] * -0.01
                    + kernels[92] * -0.01
                    + kernels[93] * -0.01
                    + kernels[94] * -0.01
                    + kernels[95] * -0.01
                    + kernels[96] * -0.01
                    + kernels[97] * -0.01
                    + kernels[98] * -0.01
                    + kernels[99] * -0.01
                    + kernels[100] * -0.01
                    + kernels[101] * -0.01
                    + kernels[102] * -0.01
                    + kernels[103] * -0.01
                    + kernels[104] * -0.00980237
                    + kernels[105] * -0.01
                    + kernels[106] * -0.01
                    + kernels[107] * -0.01
                    + kernels[108] * -0.01
                    + kernels[109] * -0.01
                    + kernels[110] * -0.01
                    + kernels[111] * -0.01
                    + kernels[112] * -0.01
                    + kernels[113] * -0.01
                    + kernels[114] * -0.01
                    + kernels[115] * -0.01
                    + kernels[116] * -0.01
                    + kernels[117] * -0.01
                    + kernels[118] * -0.01
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

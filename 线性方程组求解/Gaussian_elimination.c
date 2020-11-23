#include <stdio.h>

void Gaussian_elimination(double temp_A[][100], double temp_b[], int num)
{
    double A[100][100], b[100], x[100];
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
            A[i][j] = temp_A[i][j];
        b[i] = temp_b[i];
    }
    for (int i = 1; i < num; i++)
    {
        for (int j = i; j < num; j++)
        {
            double get_A = A[j][i-1] / A[i-1][i-1];
            b[j] = b[j] - get_A * b[i-1];
            for (int k = 0; k < num; k++)
                A[j][k] = A[j][k] - get_A * A[i-1][k];
        }
    }

    for (int i = num - 1; i >= 0; i--)
    {
        double temp = b[i];
        for (int j = num - 1; j > i; j--)
        {
            temp = temp - A[i][j] * x[j];
        }
        x[i] = temp / A[i][i];
    }

    for (int i = 0; i < num; i++)
    {
        printf("x%d = %.1f%s", i, x[i], i==4?"":"   ");
    }
}

int main()
{
    
    // 系数矩阵，常数矩阵
    double A[100][100], b[100];
    int num; // num：未知数的个数
    printf("请输入未知数的个数：");
    scanf("%d", &num);
    printf("请按顺序输入增广矩阵的值：\n");
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
            scanf("%lf", &A[i][j]);
        scanf("%lf", &b[i]);
    }
    Gaussian_elimination(A, b, num);
    return 0;
}
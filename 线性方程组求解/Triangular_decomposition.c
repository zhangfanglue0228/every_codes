#include <stdio.h>

double sumU(double L[][100] ,double U[][100], int k, int j )
{
    double result_U = 0.0;
    for (int r = 1; r <= k - 1; r++)
        result_U += L[k-1][r-1] * U[r-1][j-1];
    return result_U;
}//计算求和L

double sumL(double L[][100] ,double U[][100], int i, int k)
{
    double result_L = 0.0;
    for (int r = 0; r <= k - 1; r++)
        result_L += L[i-1][r-1] * U[r-1][k-1];
    return result_L;
}//计算求和U

double sumY(double L[][100] ,double y[], int k)
{
    double result_y = 0.0;
    for (int j = 1; j <= k - 1; j++)
    {
        result_y += L[k-1][j-1] * y[j-1];
    }
    return result_y;
}

double sumX(double U[][100] ,double x[] ,int k ,int n){
    double result_x = 0.0;
    for (int j = k + 1; j <= n; j++)
    {
        result_x += U[k-1][j-1] * x[j-1];
    }
    return result_x;
}

void Triangular_decomposition(double temp_A[][100], double temp_b[], int num)
{
    double A[100][100], b[100], L[100][100], U[100][100], x[100] = {0.0}, y[100] = {0.0};
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
            A[i][j] = temp_A[i][j];
        b[i] = temp_b[i];
    }

    // 计算L，U
    for (int i = 1; i <= num; i++)
    {
        L[i-1][i-1] = 1;//对角线元素为1
        for (int j = i; j <= num; j++)
        {
            //由于数组下标从0开始 所以i-1,j-1
            U[i-1][j-1] = A[i-1][j-1] - sumU(L,U,i,j);
            if(j + 1 <= num)
                L[j][i-1] = (A[j][i-1] - sumL(L,U,j+1,i))/U[i-1][i-1];//i变j+1，j变i 
        }
    }

    y[0] = b[0];
    for (int i = 2; i <= num; i++)
    {
        y[i - 1] = b[i - 1] - sumY(L, y, i);
    }
    for (int i = num; i >= 1; i--)
    {
        x[i-1] =(y[i-1] - sumX(U, x, i, num)) / U[i - 1][i - 1];
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
    Triangular_decomposition(A, b, num);
    return 0;
}
#include <iostream>
#include <Eigen/Dense>
#include <Eigen/Eigenvalues>
#include <math.h>

using namespace Eigen;
using namespace std;

// 条件数
double Matrix_cond_2()
{
    Matrix4d A, A_T, A_inverse, A_inverse_T;
    A << 1, 2, -12, 8,
        5, 4, 7, -2,
        -3, 7, 9, 5,
        6, -12, -8, 3;
    A_inverse = A.inverse();
    A_T = A.transpose();
    A_inverse_T = A_inverse.transpose();
    EigenSolver<Matrix4d> es1(A * A_T);
    EigenSolver<Matrix4d> es2(A_inverse * A_inverse_T);

    Matrix4d resolve_A = es1.pseudoEigenvalueMatrix();
    Matrix4d resolve_A_inverse = es2.pseudoEigenvalueMatrix();

    return sqrt(resolve_A.maxCoeff()) * sqrt(resolve_A_inverse.maxCoeff());
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
    printf("2-条件数：%f", Matrix_cond_2());
    return 0;
}
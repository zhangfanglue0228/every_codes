#include <stdio.h>
#include <math.h>
#include <windows.h>

// 秦九韶算法
double func_qin(double coefficients[], int n, double x)
{
    double res = coefficients[n - 1];
    for (int i = n - 2; i >= 0; i--)
    {
        res = res * x + coefficients[i];
    }
    return res;
}

// 直接计算法
double func_common(double coefficients[], int n, double x)
{
    double res = 0.0;
    for (int i = 0; i < n; i++)
    {
        res = res + coefficients[i] * pow(x, i);
    }
    return res;
}

int main()
{
    double run_time;
    LARGE_INTEGER time_start;	//开始时间
	LARGE_INTEGER time_over;	//结束时间
    double dqFreq;		//计时器频率
	LARGE_INTEGER f;	//计时器频率
	QueryPerformanceFrequency(&f);
	dqFreq=(double)f.QuadPart;

    int n;  // 多项式项数
    double x, coefficients[100], res;  // 需求值的x和多项式系数
    printf("Enter the number of polynomials: ");
    scanf("%d", &n);
    printf("Enter the coefficients from the high order\n");
    for (int i = n - 1; i >= 0; i--)
    {
        scanf("%lf", &coefficients[i]);
    }
    printf("Enter the value you want to evaluate: ");
    scanf("%lf", &x);
    // 秦九韶算法
    QueryPerformanceCounter(&time_start);	//计时开始
    res = func_qin(coefficients, n, x);
    QueryPerformanceCounter(&time_over);	//计时开始
    run_time=1000000*(time_over.QuadPart-time_start.QuadPart)/dqFreq;
    printf("\n%.3f\n", res);
    printf("Qin Jiushao's algorithm time: %fus\n\n", run_time);
    //直接计算发
    QueryPerformanceCounter(&time_start);	//计时开始
    res = func_common(coefficients, n, x);
    QueryPerformanceCounter(&time_over);	//计时开始
    run_time=1000000*(time_over.QuadPart-time_start.QuadPart)/dqFreq;
    printf("%.3f\n", res);
    printf("Direct calculation time: %fus\n", run_time);
    return 0;
}
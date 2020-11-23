#include <stdio.h>
#include <math.h>
#include <windows.h>

#define wucha 1e-6

double fx(double x) { return 2 * x * x - sin(x) - 1; } // fx函数
double dfx(double x) { return 4 * x - cos(x); }       // fx的导数函数

// 二分法
void Dichotomy()
{
    int count = 0;
    double left = 0;
    double right = 1;
    double x = 0.5;
    double res, before_x;
    printf("Dichotomy method:\n");
    printf("%03d: x = %.8f, f(x) = %.8f, error = NULL\n", count, x, fx(x));
    do
    {
        count++;
        res = fx(x);
        before_x = x;
        if (res > 0)    right = x;
        if (res < 0)    left = x;
        printf("%03d: x = %.8f, f(x) = %.8f, error = %.8f\n", count, x, fx(x), fabs(before_x - x));

        x = (left + right) / 2;
    }while(fabs(before_x - x) >= wucha);
}

// 迭代法
// 迭代公式
double iterative_fx(double x) { return sqrt((1 + sin(x)) / 2); }

void Iterative()
{
    int count = 0;  // 迭代次数
    double before_x;
    double x = 1.0; // 迭代初始x值
    printf("Iterative method:\n");
    printf("%03d: x = %.8f, f(x) = %.8f, error = NULL\n", count, x, fx(x));

    do
    {
        count++;
        before_x = x;
        x = iterative_fx(x);
        printf("%03d: x = %.8f, f(x) = %.8f, error = %.8f\n", count, x, fx(x), fabs(before_x - x));
    } while (fabs(before_x - x) >= wucha);
}

// 牛顿迭代法
void NewTownIterative()
{
    int count = 0;  // 迭代次数
    double before_x;
    double x = 0.0; // 迭代初始x值
    printf("NewTown iterative method:\n");
    printf("%03d: x = %.8f, f(x) = %.8f, error = NULL\n", count, x, fx(x));

    do
    {
        count++;
        before_x = x;
        x = before_x - (fx(before_x) / dfx(before_x));
        printf("%03d: x = %.8f, f(x) = %.8f, error = %.8f\n", count, x, fx(x), fabs(before_x - x));
    } while (fabs(before_x - x) >= wucha);
}

// Steffensen加速迭代法
// 迭代公式
double steffensen_fx(double x){
    return x - ((iterative_fx(x) - x) * (iterative_fx(x) - x)) / (iterative_fx(iterative_fx(x)) - 2 * iterative_fx(x) + x);
}

void Steffensen()
{
    int count = 0;  // 迭代次数
    double before_x;
    double x = 0.0; // 迭代初始x值
    printf("Steffensen iterative method:\n");
    printf("%03d: x = %.8f, f(x) = %.8f, error = NULL\n", count, x, fx(x));

    do
    {
        count++;
        before_x = x;
        x = steffensen_fx(x);
        printf("%03d: x = %.8f, f(x) = %.8f, error = %.8f\n", count, x, fx(x), fabs(before_x - x));
    } while (fabs(before_x - x) >= wucha);
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

    QueryPerformanceCounter(&time_start);	//计时开始
    Dichotomy();
    QueryPerformanceCounter(&time_over);	//计时结束
    run_time=1000000*(time_over.QuadPart-time_start.QuadPart)/dqFreq;
    printf("time required: %.3fus\n\n", run_time);


    QueryPerformanceCounter(&time_start);	//计时开始
    Iterative();
    QueryPerformanceCounter(&time_over);	//计时结束
    run_time=1000000*(time_over.QuadPart-time_start.QuadPart)/dqFreq;
    printf("time required: %.3fus\n\n", run_time);

    QueryPerformanceCounter(&time_start);	//计时开始
    NewTownIterative();
    QueryPerformanceCounter(&time_over);	//计时结束
    run_time=1000000*(time_over.QuadPart-time_start.QuadPart)/dqFreq;
    printf("time required: %.3fus\n\n", run_time);

    QueryPerformanceCounter(&time_start);	//计时开始
    Steffensen();
    QueryPerformanceCounter(&time_over);	//计时结束
    run_time=1000000*(time_over.QuadPart-time_start.QuadPart)/dqFreq;
    printf("time required: %.3fus\n\n", run_time);


    return 0;
}
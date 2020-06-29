#include "GL\glut.h"
#include <math.h>
#include <Windows.h>
#include <stdio.h>

// 点类，记录一个点的x和y信息，设置一个setxy函数用于更改一个点的坐标信息
class Point
{
public:
    int x, y;
    void setxy(int _x, int _y) 
    {
        x = _x;
        y = _y;
    }
};

// 计数点的数量
static int NUM = 0;
int n = 0;

// 是否显示辅助线
int flag = 0;

//Point数组用于存储用户绘制的所有点
static Point points[10];

//初始化函数
void init(void)
{
    glClearColor(0.5, 0.5, 0.5, 0); //设定背景为灰色
    glPointSize(3.0); //设定点的大小
    glMatrixMode(GL_PROJECTION); // 设定合适的矩阵
    glLoadIdentity();
    gluOrtho2D(0.0, 500.0, 0.0, 500.0); //平行投影，四个参数分别是x,y范围
}

//绘制点
void draw_Point(Point p)
{
    glBegin(GL_POINTS);
    glVertex2f(p.x, p.y);
    glEnd();
    glFlush();
}

// 绘制直线
void draw_line(Point p1, Point p2) {
    glBegin(GL_LINES);
    glVertex2f(p1.x, p1.y);
    glVertex2f(p2.x, p2.y);
    glEnd();
    glFlush();
}

// 阶乘函数
long long factorial(int t)
{
    long long res = 1;
    for (int i = 2; i <= t; i++)
        res = res * i;
    return res;
}

// 排列组合C运算
double C_clau(int n, int m)
{
    return factorial(n) / (factorial(m) * factorial(n - m));
}

// 幂函数
double mypow(double num, int n)
{
    if (n == 0)
        return 1;
    double res = num;
    for (int i = 1; i < n; i++)
        res = res * num;
    return res;
}

//绘制贝塞尔曲线
Point draw_Bezier(Point* p, double t)
{
    Point tem_p;
    int res_x = 0;
    int res_y = 0;
    for (int i = 0; i <= NUM; i++)
    {
        double magni = 0.0;
        // 贝塞尔曲线点上坐标的位置
        magni = C_clau(NUM, i) * mypow(1 - t, NUM - i) * mypow(t, i);
        res_x = res_x + p[i].x * magni;
        res_y = res_y + p[i].y * magni;
    }
    tem_p.setxy(res_x, res_y);
    return tem_p;
}

// 求线上t时刻时绘制辅助线的端点位置信息
Point add(Point p1, Point p2, double t)
{
    Point p;
    p.x = p1.x + (-p1.x + p2.x) * t;
    p.y = p1.y + (-p1.y + p2.y) * t;
    return p;
}

// 递归实现绘制在绘制贝塞尔曲线时的辅助线
void draw(Point* p, int n, double t)
{
    glLineWidth(1);
    glColor3f(1 - t, 1 - t, 1 - t);//循环生成辅助线的颜色
    if (n <= 2)
        return;
    Point x[30] = {};
    for (int i = 0; i < n - 1; i++)
        x[i] = add(p[i], p[i + 1], t);
    for (int i = 0; i < n - 2; i++)
        draw_line(x[i], x[i + 1]);
    draw(x, n - 1, t);
}


// 鼠标事件
void mouseFunction(int button, int state, int x, int y) 
{
    if (state == GLUT_DOWN)
    {
        points[NUM].setxy(x, 500 - y); // 记录鼠标点击位置的坐标
        glColor3f(0.0, 0.0, 0.0);  // 设置绘制点的颜色为黑色
        draw_Point(points[NUM]);  // 绘制鼠标点击位置的点

        glColor3f(0.0, 0.0, 0.0);  // 设置绘制线的颜色为黑色
        if (NUM > 0) draw_line(points[NUM - 1], points[NUM]);  // 不为第一个点时显示点之间的连线
        
        if (NUM == n) 
        {
            //绘制贝塞尔曲线   
            glColor3f(1, 0.5, 0.5); // 设定曲线的颜色
            Point p_current = points[0]; // 设为第一次绘制的起点为用户绘制的第一个点
            for (double t = 0.0; t <= 1.0; t += 0.0002)
            {
                Point P = draw_Bezier(points, t);
                if (flag == 1)
                    draw(points, n + 1, t);  // 绘制在绘制贝塞尔曲线时的辅助线
                draw_line(p_current, P);  // 绘制对应贝塞尔曲线上的点和上一点之间的直线
                p_current = P;  // 更新起点
            }
            NUM = 0;
        }
        else 
            NUM++;
    }
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    glFlush();
}

int main(int argc, char* argv[])
{
    int temp;
    printf("请输入贝塞尔曲线阶数：");
    scanf("%d", &n);
    printf("是否显示绘制曲线辅助线（0/1）：");
    scanf("%d", &flag);

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutInitWindowSize(500, 500);    //显示框的大小
    glutInitWindowPosition(100, 100);
    glutCreateWindow("3阶Bezier曲线");

    init(); // 初始化
    glutMouseFunc(mouseFunction); // 添加鼠标事件
    glutDisplayFunc(display); // 执行显示   
    glutMainLoop();
    return 0;
}
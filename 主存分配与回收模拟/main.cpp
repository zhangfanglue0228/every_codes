#include<stdio.h>  
#include<conio.h>
#include<string.h>
#include<stdlib.h> 

typedef struct free_table//定义一个空闲区说明表结构  
{
    int num; //分区序号    
    long begin; //起始地址    
    long size;   //分区大小    
    int status;   //分区状态 
}free_table;

typedef struct Node// 线性表的双向链表存储结构 
{
    free_table data;
    struct Node* pre; //前趋指针   
    struct Node* next;  //后继指针 
}Node, * LinkList;

LinkList first; //分区链表头结点 
LinkList end;  //分区链表尾结点  
int flag;//需要被删除的分区序号   

int Initblock()//开创带头结点的内存空间链表 
{
    first = (LinkList)malloc(sizeof(Node));
    end = (LinkList)malloc(sizeof(Node));
    first->pre = NULL;
    first->next = end;
    end->pre = first;
    end->next = NULL;
    end->data.num = 1;
    end->data.begin = 10;
    end->data.size = 246;
    end->data.status = 0;
    return true;
}

//菜单
void menu()
{
    printf("\n*************内存分配和回收***********\n");
    printf("--------------------------------------\n");
    printf("                 0.退出                  \n");
    printf("             1.首次适应算法          \n");
    printf("             2.最佳适应算法          \n");
    printf("--------------------------------------\n");
}

void update_num()//分区序号重新排序 
{
    Node* p = first->next;
    int i = 1;
    while (p)
    {
        p->data.num = i++;
        p = p->next;
    }
}

//显示主存分配情况 
void show()
{
    int flag = 0;//用来记录分区序号    
    Node* p = first;
    p->data.num = 0;
    p->data.begin = 0;
    p->data.size = 10;
    p->data.status = 1;
    update_num();
    printf("\n\t\t主存空间分配情况\n");
    printf("----------------------------------------------------------\n\n");
    printf("分区序号\t起始地址\t分区大小\t分区状态\n\n");
    while (p)
    {
        printf("%d\t\t%d\t\t%d", p->data.num, p->data.begin, p->data.size);
        if (p->data.num == 0)
            printf("\t\t操作系统\n");
        else if (p->data.status == 0)
            printf("\t\t空闲\n");
        else
            printf("\t\t已分配\n");
        p = p->next;
    }
    printf("----------------------------------------------------------\n\n");
}

//首次适应算法  
int First_fit(int request)
{
    //为申请作业开辟新空间且初始化    
    Node* p = first->next;
    LinkList temp = (LinkList)malloc(sizeof(Node));
    temp->data.size = request;
    temp->data.status = 1;
    while (p)
    {
        if ((p->data.status == 0) && (p->data.size == request))
        {
            //有大小恰好合适的空闲块       
            p->data.status = 1;
            return true;
            break;
        }
        else if ((p->data.status == 0) && (p->data.size > request))
        {
            //有空闲块能满足需求且有剩余        
            temp->pre = p->pre;
            temp->next = p;
            temp->data.begin = p->data.begin;
            temp->data.num = p->data.num;
            p->pre->next = temp;
            p->pre = temp;
            p->data.begin = temp->data.begin + temp->data.size;
            p->data.size -= request;
            p->data.num += 1;
            return true;
            break;
        }
        p = p->next;
    }
    return false;
}

//最佳适应算法  
int Best_fit(int request)
{
    int ch; //记录最小剩余空间    
    Node* p = first;
    Node* q = NULL; //记录最佳插入位置     
    LinkList temp = (LinkList)malloc(sizeof(Node));
    temp->data.size = request;
    temp->data.status = 1;
    p->data.num = 1;
    while (p) //初始化最小空间和最佳位置    
    {
        if ((p->data.status == 0) && (p->data.size >= request))
        {
            if (q == NULL)
            {
                q = p;
                ch = p->data.size - request;
            }
            else if (q->data.size > p->data.size)
            {
                q = p;
                ch = p->data.size - request;
            }
        }
        p = p->next;
    }
    if (q == NULL) return false;//没有找到空闲块   
    else if (q->data.size == request)
    {
        q->data.status = 1;
        return true;
    }
    else
    {
        temp->pre = q->pre;
        temp->next = q;
        temp->data.begin = q->data.begin;
        temp->data.num = q->data.num;
        q->pre->next = temp;
        q->pre = temp;
        q->data.begin += request;
        q->data.size = ch;
        q->data.num += 1;
        return true;
    }
    return true;
}

//分配主存  
int allocation(int a)
{
    int request;//申请内存大小    
    printf("请输入申请分配的主存大小(单位:KB):");
    scanf("%d", &request);
    if (request < 0 || request == 0)
    {
        printf("分配大小不合适，请重试！");
        return false;
    }
    switch (a)
    {
    case 1: //默认首次适应算法 
        if (First_fit(request) == 1) printf("****分配成功！****");
        else printf("****内存不足，分配失败！****");
        return true;
        break;
    case 2: //选择最佳适应算法              
        if (Best_fit(request) == 1) printf("****分配成功！****");
        else printf("****内存不足，分配失败！****");
        return true;
        break;
    }
}

//主存回收  
int recovery(int flag)
{
    Node* p = first;
    if (flag == 0)
    {
        printf("系统主存空间，禁止操作！\n");
        return false;
    }
        
    while(p)
    {
        if (p->data.num == flag)
        {
            p->data.status = 0;
            if (p->pre->data.status != 0 && p->next->data.status != 0)
                break;
            if (p->pre->data.status == 0 && p->next->data.status != 0)  // 前为空闲区
            {
                p->pre->data.size = p->pre->data.size + p->data.size;
                p->pre->next = p->next;
                p->next->pre = p->pre;
            }
            else if (p->pre->data.status != 0 && p->next->data.status == 0)  // 后为空闲区
            {
                p->next->data.size = p->next->data.size + p->data.size;
                p->next->data.begin = p->data.begin;
                p->pre->next = p->next;
                p->next->pre = p->pre;
            }
            else if (p->pre->data.status == 0 && p->next->data.status == 0)  //前后都为空闲区 
            {
                p->next->data.size = p->next->data.size + p->data.size + p->pre->data.size;
                p->next->data.begin = p->pre->data.begin;
                p->pre->pre->next = p->next;
                p->next->pre = p->pre->pre;
                /*p->pre->data.size = p->pre->data.size + p->data.size + p->next->data.size;
                p->next->next->pre = p->pre;
                p->pre->next = p->next->next;*/
            }
            break;
        }
        p = p->next;	
    }
    printf("****回收成功****");
    return true;
}

void main()
{
    int i;  //操作选择标记     
    int a;//算法选择标记      

    while (1)
    {
        menu();
        printf("请选择输入所使用的内存分配算法 (0~3):");
        scanf("%d", &a);
        Initblock(); //开创空间表     
        First_fit(10);
        First_fit(25);
        First_fit(20);
        First_fit(45);
        recovery(3);
        while (a < 0 || a>2)
        {
            printf("\n输入错误，请重新选择输入所使用的内存分配算法 (0~3):");
            scanf("%d", &a);
        }
        switch (a)
        {
        case 1:printf("\n\t****使用首次适应算法：****\n");
            break;
        case 2:printf("\n\t****使用最佳适应算法：****\n");
            break;
        case 0:printf("\n\t**********退出***********\n");
            return;
        }
        while (1)
        {
            show();
            printf("\t1: 分配内存\t2: 回收内存\t0: 退出当前内存分配算法\n");
            printf("请输入您的操作：");
            scanf("%d", &i);
            if (i == 1)
                allocation(a); // 分配内存         
            else if (i == 2)  // 内存回收         
            {
                printf("请输入您要释放的分区号：");
                scanf("%d", &flag);
                recovery(flag);
            }
            else if (i == 0)
            {
                printf("\n退出当前内存分配算法，返回主菜单\n");
                break; //退出   
            }
            else //输入操作有误         
            {
                printf("输入有误，请重新输入！");
                continue;
            }
        }
    }
}
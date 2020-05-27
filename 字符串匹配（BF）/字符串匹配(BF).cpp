#include <iostream>
#include <ctime>
using namespace std;
int BF(char* s1, char* s2);
int main()
{
	char s1[100], s2[100];
	while (cin >> s1 >> s2)
	{
		clock_t starttime, endtime;
		starttime = clock();
		int flag = BF(s1, s2);
		if (flag == -1)cout << "无法匹配" << endl;
		else cout << "匹配成功，匹配位置为第" << flag + 1 << "位" << endl;
		endtime = clock();
		cout << "BF算法运行时间为" << (endtime - starttime) / CLOCKS_PER_SEC << "s" << endl << endl;
	}
	return 0;
}
int BF(char* s1, char* s2)
{
	if (s1 == '\0' || s2 == '\0')return -1;
	int len_1 = strlen(s1);
	int len_2 = strlen(s2);
	if (len_2 > len_1)return -1;
	char* p = s1;
	char* temp = s1;
	char* q = s2;
	while (*p != '\0')
	{
		if (*p == *q)
		{
			p++;
			q++;
		}
		else
		{
			p = temp++;
			q = s2;
		}
		if (*q == '\0')return (p - s1) - (q - s2);
	}
	return -1;
}
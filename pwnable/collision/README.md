# Collision
## Environment
```
ssh col@pwnable.kr -p2222
pw: guest
```
![](./question.png)

## Flow
* 登入後，查看檔案 
```
col@pwnable:~$ ls -l
total 16
-r-sr-x--- 1 col_pwn col     7341 Jun 11  2014 col
-rw-r--r-- 1 root    root     555 Jun 12  2014 col.c
-r--r----- 1 col_pwn col_pwn   52 Jun 11  2014 flag
```
* 查看 col.c，會發現要輸入 20 個字元，並且經由下方 function 轉換後要等於 0x21DD09EC
```
unsigned long check_password(const char* p){
	int* ip = (int*)p;
	int i;
	int res=0;
	for(i=0; i<5; i++){
		res += ip[i];
	}
	return res;
}
``` 
* 首先要先搞懂 `int* ip = (int*)p;` 是什麼意思，

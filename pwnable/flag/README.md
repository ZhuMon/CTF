# flag
## Download
```
$ wget http://pwnable.kr/bin/flag
```
## Flow
* 題目提示說這是一個 binary file
* 執行看看
    ```
    $ chmod +x flag
    $ ./flag
    I will malloc() and strcpy the flag there. take it.
    ```
* 發現他只有印出一段文字
* 使用 gdb 跑跑看
    ```
    $ gdb ./flag
    (gdb) disass main
    No symbol table is loaded.  Use the "file" command.
    ```
* 發現並沒有 symbol table, 無法查看 main 的 assembly code
* 
## Flag
```
UPX...? sounds like a delivery service :)
```

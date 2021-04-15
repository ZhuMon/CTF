# random
## environment
```
ssh random@pwnable.kr -p2222
pw: guest
```
## Flow
* goto `/tmp` create a file, and print a random value, to know what is the value
* random ^ 0xdeadbeef = `<input>`
* input `<input>` after `./random`

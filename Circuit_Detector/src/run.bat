x86_64-w64-mingw32-gcc -c -Wall -Werror -fpic *.c -o Detect.o
x86_64-w64-mingw32-gcc -shared  *.c -o Detect.dll
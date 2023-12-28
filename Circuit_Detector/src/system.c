#include "Detect.h"

DWORD WINAPI YourThreadFunction(LPVOID lpParam) {
    // Your recursive function or code here
    return 0;
}

int main() {
    const DWORD stackSize = 16 * 1024 * 1024; // 16 MB stack size
    HANDLE hThread = CreateThread(NULL, stackSize, YourThreadFunction, NULL, 0, NULL);
    if (hThread == NULL) {
        printf("Thread creation failed!\n");
        return 1;
    }

    // Other code...

    CloseHandle(hThread);
    return 0;
}

#include "stdio.h"
#include "stdlib.h"

int main(int argc, char const *argv[])
{
    /* code */
    int num = atoi(argv[1]);
    int first = 1, second=2, tmp=0;
    int sum = 0;
    while(second<num){
        if(second%2==0){
            sum+=second;
        }
        tmp = first;
        first = second;
        second = second+tmp;    
    }
    printf("%d", sum);
    return 0;
}

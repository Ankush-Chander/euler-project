#include <stdio.h>
#include <stdlib.h>

 long gcd(long a, long b)
 {
     if (b == 0)
         return a;
     return gcd(b, a % b);
 }

long lcm(long x, long y){
    long result = (x*y)/gcd(x,y);
    return result;
}

int main(int argc, char const *argv[])
{
    /* code */
    int num = atoi(argv[1]);
    long smallest_multiple = 1;
    for(int i = num;i>=1;i--){
        smallest_multiple = lcm(smallest_multiple,i);
    }
    printf("%ld",smallest_multiple);

}

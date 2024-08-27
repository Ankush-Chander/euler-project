/*
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
 */
#include "stdio.h"
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int n = atoi(argv[1]);
    int sum = 0;
    for(int i=1; i< n; i++){
        if((i%3==0) || (i%5==0)){
            sum = sum + i;
        }        
    }
    printf("%d", sum);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>


typedef unsigned long long int ulli;

void populate_sieve(char *sieve, ulli size){
    for(ulli i=0;i<size;i++){
        sieve[i] = '0';
    }
    for(ulli j=2;j<size ; j++){
        if(sieve[j]=='1' || sieve[j]=='2'){            
            continue;
        }else{
            sieve[j] = '1';
            for(ulli multiple=2;j*multiple < size;multiple++){
                sieve[j*multiple] = '2';
            }            
        }
    }    
    return;
}



int main(int argc, char const *argv[])
{
    //600851475143
    ulli num = atol(argv[1]);
    // prime factors are usually lot smaller than the actual number
    // restrict the size of the array 
    ulli size = num/2 > 100000000? 100000000 : num/2; 
    
    char *sieve=calloc(size,sizeof(char));
    printf("sieve: %p\n",sieve);
    sieve[0] = '1';
    // printf("%s: %c", "sieve[0]", sieve[0]);
    
    // populate all primes in array
    populate_sieve(sieve, size);            
            
    ulli candidate_factor = 2, max = num;
    for(;candidate_factor<size && candidate_factor<=max;candidate_factor++){
        if(sieve[candidate_factor]=='1' &&num%candidate_factor==0){             
            max = num/candidate_factor;
            printf("%llu\n", candidate_factor);            
    }
    free(sieve);
    return 0;
}

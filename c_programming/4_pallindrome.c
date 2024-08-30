#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_number_pallindrome(int n){
    int ENOUGH = 10;
    char str[ENOUGH];
    sprintf(str, "%d", n);
    for(int i=0;i < strlen(str);i++){
        if(str[i]!=str[strlen(str)-i-1]){
            return 0;
        }
    } 
    return 1;
    
}

int find_power(int x, int y){
    int power=1;
    for(int i=0;i<y;i++){
        power*=x;
    }
    return power;
}

int main(int argc, char const *argv[])
{
    /* code */
    int num = atoi(argv[1]);
    int largest_number =  find_power(10,num)-1;
    int smallest_number =  find_power(10,num-1);
    int max= 0;
    for(int i=largest_number;i>=smallest_number;i--){
        for(int j=largest_number;j>=smallest_number;j--){
            if(is_number_pallindrome(i*j)){
                if(max<i*j){
                    max=i*j;
                }
            }
    }
    }
    printf("max=%d\n",max);
    return 0;
}

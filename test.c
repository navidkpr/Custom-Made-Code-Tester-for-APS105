#include <stdio.h>
#include <stdbool.h> 
#include <math.h>

bool validateInputs(double left, double right, int n){
    
    if(left<-10.0 || right>10.0 || right<=left || n<=0){
        return true;
    } 
    else{
        return false;
    }
}

double evalFunc(double x){
    
    double height = 2*pow(x,2) - 7*x - 2;
    return height;
}

int main(void){
    
    double left, right, midSum=0, leftSum=0, rightSum=0; 
    int n, cnt;
    
    do{
            
        printf("Enter the Left boundary: a, Right boundary: b, and No. of rectangles to use. To exit enter 0 0 0\n");
        scanf("%lf %lf %d",&left, &right, &n);
            
        if(validateInputs(left,right,n)){
            printf("Invalid inputs...\n\n");
        }
            
        if(left == 0 && right == 0 && n == 0){
            printf("Terminating main!\n");
            return 0;
        }
        
    } while(validateInputs(left,right,n));
    
    double x = left;
    double stepSize = (right-left)/n;
    printf("With Step Size: %0.4lf\n",stepSize);

    
    for(cnt=0;cnt<n;cnt++){
        midSum += evalFunc((2*x+stepSize)/2)*stepSize;
        leftSum += evalFunc(x)*stepSize;
        rightSum += evalFunc(x+stepSize)*stepSize;
        x+=stepSize;
    }

    printf("The approximate integral of the f(x) = 2(x^2)-7x-2\nBound between %0.2lf and %0.2lf, using %d rectangles is as follows\n\n",left,right,n);
    
    printf("Mid point evaluation approximate: %0.4lf\n",midSum);
    printf("Left point evaluation approximate: %0.4lf\n",leftSum);
    printf("Right point evaluation approximate: %0.4lf\n",rightSum);
        
	return 0;
}


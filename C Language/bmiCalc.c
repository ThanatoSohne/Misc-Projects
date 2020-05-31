#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*A program to convert user's weight (in lbs) and height (in inches)
*into a BMI and then decide where in the range the user is:
*from underweight to morbidly obese.*/

int main()
{

int weightINlbs, heightINinches;
float weightINkgs, heightINm, bmiIndex;
float mkg = 0.45359237;
float dmeter = 0.0254;

printf("Please enter your weight in lbs:\n");
scanf("%d", &weightINlbs);
printf("Please enter your height in inches:\n");
scanf("%d", &heightINinches);

weightINkgs = (float)weightINlbs*mkg;
heightINm = (float)heightINinches*dmeter;

bmiIndex = weightINkgs/pow(heightINm,2);

if (bmiIndex<18.5) {
  printf("Your BMI indicates that you are underweight!\n");
}
else if (bmiIndex>=18.5 && bmiIndex<=24.9) {
  printf("Your BMI indicates that you are of normal and healthy weight!\n");
}
else if (bmiIndex>=25 && bmiIndex<=29.9){
  printf("Your BMI indicates that you are overweight!\n");
}
else {
  printf("Your BMI indicates that you are morbidly obese!\n");
}
return 0;
}
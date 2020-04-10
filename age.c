#include <stdio.h>
#include <stdlib.h>

int main ()
{
int age;
printf("enter the age number\n");
scanf("%d\n",age);

if (age>18)
{
 {
 printf("the age is greater than 18\n");
 }
     if (age<21)
 {
 printf("the age is greater than 18 but less than 21\n");
 }
     else
 {
 printf("the age is greater than 18 but not less than 21\n");
 }

}else
{
printf("the age is not greater or equal to 18\n");
}
}

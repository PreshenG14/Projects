#include <p24fj128ga010.h>
#include <math.h>
float *p1; // array pointer 1
float *p2; // array pointer 2
float *p3; // array pointer 3
int i; // counter
float array1[15]; // first array
float array2[15]; // second array
float array3[15]; // third array
float x;
float y;
float rms;
main()
{
// first array - millivolt values using a pointer
p1 = array1; // pointer value will become address of first element of array
for(i=0; i<15; i=i+1) // -20 to 120 = 150
{
*p1 = 300+(i*100);
p1++;
}
// second array - with millivolt values using a pointer
p2 = array2; // pointer value will become address of first element of array
for(i=0; i<15; i=i+1) // -20 to 120 = 150
{
*p2 = array1[i]*0.05;
p2++;
x = x + array2[i];
}
y = (x*x)/2;
rms = sqrt(y);
// fill the third array
p3 = array3; // pointer value will become address of first element of array
for(i=0; i<15; i=i+1)
{
*p3 = (array1[i]-array2[i]);
p3++;
}
} //end main
//rms = 530.3301
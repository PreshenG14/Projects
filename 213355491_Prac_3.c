// Preshen Govender
// 21355491
// Practical Project 3
// MCYS401

#include <p24fj128ga010.h>
int ana,dig,x;

main()
{
	AD1PCFG = 0xFFFF;
	TRISB = 0x0000;
	T1CON = 0x8000;

	while(1)
	{
		ana = 3;
		dig = 0;

		for(x=0;x<15;x++)
		{ 
			dig=ana*31; // 1023/33
			TMR1 = 0;
			while(TMR1 < 1700);
			PORTB = dig;
			ana = ana+1;
		}
	}
}


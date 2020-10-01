// Preshen Govender
// 21355491
// Practical Project 2 - Sem1 2020
// Interrupt Program


#include <p24fj128ga010.h>

int clktick=0;

void _ISR _T1Interrupt( void)		// Timer1 interrupt service routine
{
	clktick++;							// Increment clktick
 	_T1IF = 0;						// Clear the interrupt flag
} 									// T1Interrupt

main()
{

 // Initialize Timer 1, T1ON, Prescaler, Internal Clock

 	_T1IP = 4;						// Default Value
 	TMR1 = 0; 						// Reset Timer
 	PR1 = 25-1; 					// Set Period Register (Consider Prescalar)
	TRISB = 0x000; 					// set PORTB as 16-bit output
	AD1PCFG= 0xffff;				// set PORTB as digital output

 // Configure Timer1

 	T1CON = 0x8000;				

 // Initialize the Timer1 Interrupt, clear the flag, enable the source

 	_T1IF = 0;
 	_T1IE = 1;

 // Initialize the Processor Priority Level

 	_IPL = 0; // this is the default value anyway

 // Main Loop

	 while( 1)
 {
		PORTB = clktick;			// Write clktick to PORTB

 }								    // main loop
}								    // main


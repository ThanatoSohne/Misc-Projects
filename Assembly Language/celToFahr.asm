#Ein schnell und nah genug Umrechner von Celsius in Fahrenheit

.data

Fragen: 	.asciiz "Please enter a temperature in Celsius to get a temperature in Fahrenheit: "
Antwort: 	.asciiz "Here is the temperature in Fahrenheit: "

.text

li $t0, 2 	                  #Legt 2 in $t0
li $t1, 32 	                  #Legt 32 in $t1
add $t2, $t2, 0 	                  #Initialisiert zu 0

li $v0, 4			
la $a0, Fragen 
syscall 

addi $v0, $0, 5
syscall
add $a0, $0, $v0	          	#Benutzereingaben aufnehmen und in $a0 einfügen.

add $t2, $a0, 0		          #Legt Benutzereingaben in $t2
mult $t2, $t0		          #Wert multiplizieren in $t2 mit $t0
mflo $t4
add $t5, $t4, $t1	          	#Addiere nun 32 zum Wert von mflo

li $v0, 4			
la $a0, Antwort 
syscall 

add $a0, $0, $t5
addi $v0, $0, 1
syscall			          #Die geschätzte Temperatur in Fahrenheit ausdrucken
INCLUDE IRVINE32.INC
.data
user_prmpt0 byte "Please enter two integers to subtract: ", 0 
user_prmpt1 byte "Please enter two integers to multiply: ", 0 
user_prmpt2 byte "Please enter two integers to divide. Enter the dividend followed by the divisor: ", 0 
user_prmpt3 byte "Please enter the power followed by the exponent: ", 0 
user_prmpt4 byte "Please enter the index of the Fibonacci sequence: ", 0
user_prmpt5 byte "Please enter 10 array elements: ", 0

.code
main proc
	;;Question 1: subtract two given integers
	Mov edx, offset user_prmpt0  
	Call WriteString; don't change this line 
	Call CRLF ; print new line 
	;Add subtraction logic after this line


	;;Question 2: Multiply two integers
	
	mov edx, offset user_prmpt1
	Call WriteString
	Call CRLF
	;;Write your code after this line



	;;Question 3: divide two integers
	mov edx, offset user_prmpt2
	Call WriteString
	Call CRLF
	;;Write your code after this line

	;; Question 4: find the power
	mov edx, offset user_prmpt3
	Call WriteString
	Call CRLF
	;;Write your code after this line

	;; Question 5: find the fibonacci sequence until a given index
	mov edx, offset user_prmpt4
	Call WriteString
	Call CRLF
	;;Write your code after thils line


	;;Question 6: reverse the array
	;; Write your code after this line
	mov edx, offset user_prmpt5
	Call WriteString
	exit
	
main endp

end main
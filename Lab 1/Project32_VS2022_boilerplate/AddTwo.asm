; AddTwo.asm - adds two 32-bit integers.
; Chapter 3 example

include irvine32.inc
.data

.code
main proc
	mov	eax,5				
	add	eax,6				
	call dumpregs
main endp
end main
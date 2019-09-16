;nasm -f bin exam.asm -o exam.bin

mov ax, WORD 0xb800
mov ds, Word ax
mov [0x00], byte 'a'
mov [0x02], byte 's'
mov [0x04], byte 'm'
jmp $


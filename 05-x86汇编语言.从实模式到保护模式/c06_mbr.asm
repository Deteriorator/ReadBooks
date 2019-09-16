;nasm -f bin c06_mbr.asm -o c06_mbr.bin
;代码清单6-1
;文件名：c06_mbr.asm
;文件说明：硬盘主引导扇区代码
;创建日期：2011-4-12 22:12 
      
jmp near start   ;跳过非指令的数据区
         
mytext:
    db 'L',0x07,'a',0x07,'b',0x07,'e',0x07,'l',0x07,' ',0x07,'o',0x07,\
        'f',0x07,'f',0x07,'s',0x07,'e',0x07,'t',0x07,':',0x07
number:
	db 0,0,0,0,0
start:
    mov ax,0x7c0                  ;设置数据段基地址 
    mov ds,ax  
    mov ax,0xb800                 ;设置附加段基地址 
    mov es,ax        
    cld
    mov si,mytext                 
    mov di,0
    mov cx,(number-mytext)/2      ;实际上等于 13
    rep movsw
     
    ;得到标号所代表的偏移地址
    mov ax,number
         
    ;计算各个数位
    mov bx,ax
    mov cx,5                      ;循环次数 
    mov si,10                     ;除数 
digit: 
    xor dx,dx                     ;清零操作
    div si
    mov [bx],dl                   ;保存数位
    inc bx                        ;Inc 加一指令
    loop digit                    ;将循环次数减一，cx的内容
         
	;显示各个数位
    mov bx,number 
    mov si,4                      
show:
    mov al,[bx+si]                ;获取数据区万位数字
    add al,0x30                   ;将数字转换为ASCII码
    mov ah,0x04                   ;0x04是显示属性，黑底红字，无加亮，无闪烁
    mov [es:di],ax                ;将数字传送到显示缓冲区
    add di,2                      ;DI 指向缓冲区的下一个单元
    dec si                        ;dec 将操作数内容减一
    jns show                      ;sf符号位，jns条件转移指令，当sf为1时，不跳转，顺序执行下一条指令
         
    mov word [es:di],0x0744       ;07表示黑底白字，44是D的ASCII码

    jmp near $                    ;无限循环 $标记等同于标号，可看成是隐藏在当前行行首的标号
;除去0x55和0xaa，剩余的主引导扇区(512字节)内容是510字节,$$表示当前汇编节(段)的起始汇编地址
times 510-($-$$) db 0                
                 db 0x55,0xaa

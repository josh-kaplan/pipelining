; program2.s
;
; Josh Kaplan
; _jk@jhu.edu
;
; Runs the same commands as program 1, but in a different order.
; This removes pipelining hazards and should speedup execution.

global start

section .text

start:
    mov     ecx, 0

repeat:    
    ; Do some things without pipelining hazards
    push    dword 0
    push    dword 1
    pop     eax
    pop     ebx
    add     eax, 1
    add     ebx, 1

    ; Loop
    add     ecx, 1
    cmp     ecx, 25000000  ; Loop counter - must be the same as program 1
    jle     repeat

    ; Exit
    mov     eax, 1
    push    dword 0
    sub     esp, 4
    int     0x80



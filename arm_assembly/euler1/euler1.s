/* program finds the sum of numbers that are multiples of 3 and 5 from range 0 to 1000 */
/* printed answer : 233168 */

.extern printf    /*assembly directive, uses the C function printf as subroutine for debugging*/
.global main      /*assembly directive, tells where to begin execution of program*/
.align 2          /*assembly directive, tells memory addresses only work in chunks of 4 bytes*/

/*declaring constants*/
.equ loop_start,0
.equ loop_end,1000

/*renaming registers*/
counter .req r4
sum  .req r5
remainder  .req r6
max_bound .req r7

main:
        push {ip,lr}

        ldr counter, =loop_start  /*initializing loop counter to 0*/
        mov sum, #0
        mov remainder, #0
        ldr max_bound, =loop_end

        count_up:
                mov r2, counter
                mov r3, #3
                bl mod_x
                mov remainder, r0
                /* for debugging
                mov r1, r0
                ldr r0, =debug_param1
                bl printf
                */
                cmp remainder, #0
                bne check_mod5
                        add sum, sum, counter
                        b update_counter
                check_mod5:
                        mov r2, counter
                        mov r3, #5
                        bl mod_x
                        mov remainder, r0
                        /* for debugging
                        mov r1, r0
                        ldr r0, =debug_param1
                        bl printf
                        */
                        cmp remainder, #0
                        bne update_counter
                                add sum, sum, counter
                update_counter:
                        add counter, counter, #1    /*ARM doesn't have increment instruction?*/
                        cmp counter, max_bound
                        blt count_up

        ldr r0, =printf_param1
        mov r1, sum      /* second argument for printf*/
        bl printf

        mov r0, #0
        pop {ip,pc}
        
        # r2 is the diviend, r3 is the modulo divisor
        mod_x:
                subtract_loop:
                        subs r2, r2, r3   /*subtracts r3 from r2, save to r2*/
                        bpl subtract_loop  /*branch if positive or 0*/
                add r0, r2, r3  /*r0 stores the return result*/
                bx lr   /*branches to return address stored in link register*/

        debug_param1: .asciz "This is a debugging statement -> %d\n"
        printf_param1: .asciz "Sum of multiples of 3 or 5 below 1000 -> %d\n"  /*label for string input into printf*/


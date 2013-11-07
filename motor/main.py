#!/usr/bin/env python


# main method
if __name__=="__main__":

    # initializing parameters
    GPIO.setwarnings(False)  #disables not at default(input)-pin-setting warnings

    GPIO.setmode(GPIO.BCM)
    wheel_tl_pin1 = 4  # wheel top left
    wheel_tl_pin2 = 17  # for backward control
    wheel_tr_pin1 = 21  # wheel top right
    wheel_tr_pin2 = 22  # for backward control
    wheel_bl_pin1 = 18  # wheel bottom left
    wheel_bl_pin2 = 23  # for backward control
    wheel_br_pin1 = 24  # wheel bottom right
    wheel_br_pin2 = 25  # for backward control
    servo_top_pin = 7  # servo top
    servo_bot_pin = 8  # servo bottom
    init_wheel_duty_cycle = 50
    init_servo_duty_cycle = 30
    dir_forward = 0
    dir_right = 90
    dir_backward = 180
    dir_left = 270
    dc_motor_freq = 50
    servo_freq = 180  # use to drive SG-90 servo only

    # gpio pin pwm init (channel numbers, pin1 starting duty cycle, starting direction, pwm frequency)
    wheel_tl = Wheel (wheel_tl_pin1, wheel_tl_pin2, init_wheel_duty_cycle, dir_forward, dc_motor_freq)
    wheel_tr = Wheel (wheel_tr_pin1, wheel_tr_pin2, init_wheel_duty_cycle, dir_forward, dc_motor_freq)
    wheel_bl = Wheel (wheel_bl_pin1, wheel_bl_pin2, init_wheel_duty_cycle, dir_forward, dc_motor_freq)
    wheel_br = Wheel (wheel_br_pin1, wheel_br_pin2, init_wheel_duty_cycle, dir_forward, dc_motor_freq)
    servo_side = Servo (servo_top_pin, init_servo_duty_cycle, servo_freq)
    servo_bottom = Servo (servo_bot_pin, init_servo_duty_cycle, servo_freq)

    mouse_car = Car (wheel_tl,wheel_tr,wheel_bl,wheel_br)
    
    # performing test servo sweep...
    # servo_sweep (servo_bottom)

    # i = key_input ()
    # for s in i:
    #     if s == sys.stdin:
    #         str_line = sys.stdin.readline().strip()
    #         chars = list (str_line)
    #         for char in chars:
    #             if char == 'w':
    #                 print 'forward'
    #             elif char == 'a':
    #                 print 'left'
    #             elif char == 'd':
    #                 print 'right'
    #             elif char == 's':
    #                 print 'back'
                            

    try:
        while 1:
            time.sleep (1)
            
    except KeyboardInterrupt:
        pass

    wheel_tl.terminate ()
    wheel_tr.terminate ()
    wheel_bl.terminate ()
    wheel_br.terminate ()
    servo_side.terminate ()
    servo_bottom.terminate ()
    GPIO.cleanup()
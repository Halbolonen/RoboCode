from sbot import motors, arduino, AnalogPin
import sys
    
def set_motors(left,right): 
    motors.set_power(0,left) 
    motors.set_power(1,right)  

def turn_left(speed):
    set_motors(-speed, speed)
    
def turn_right(speed):
    turn_left(-speed)
    
def line_follow_turn_left(speed):
    set_motors(speed, speed * 1.5)
    
def line_follow_turn_right(speed):
    set_motors(speed * 1.5, speed)

def sharp_lf_turn_right(speed):
    set_motors(speed, 0)

def sharp_lf_turn_left(speed):
    set_motors(0, speed)
    
def get_front_ultrasound_distance():
    return arduino.measure_ultrasound_distance(2,3)

def find_target(markerlist, target): 
    for marker in markerlist: 
        if marker.id == target: 
            return marker 
    return None

def find_closest_marker(markerlist, visited_marker_list):
    shortest_distance = sys.float_info.max
    shortest_marker = None
    for marker in markerlist:
        if marker.position.distance < shortest_distance and not marker in visited_marker_list:
            shortest_distance = marker.position.distance
            shortest_marker = marker
    return shortest_marker
    
def task5():
    robo_speed = 0.2

    def set_state(state): 
        match state:
            case "forward":
                set_motors(robo_speed,robo_speed) 
            case "left":
                line_follow_turn_left(robo_speed)
            case "right":
                line_follow_turn_right(robo_speed)
            case "corner_left":
                sharp_lf_turn_left(robo_speed)
            case "corner_right":
                sharp_lf_turn_right(robo_speed)
    
    current_state = ""
    
    while True: 
        left_IR = arduino.analog_read(AnalogPin.A0) 
        centre_IR = arduino.analog_read(AnalogPin.A1) 
        right_IR = arduino.analog_read(AnalogPin.A2)

        print(left_IR, centre_IR, right_IR)
        if left_IR < 1.2 and centre_IR > 3.5 and right_IR < 1.2: 
            current_state="forward" 
            corrected_line_excursion = False
        elif (left_IR > 3.5 and centre_IR < 1.2) or left_IR < 1.2 :
            current_state="left"
            last_turning_state = "left"
            corrected_line_excursion = False
        elif (centre_IR < 1.2 and right_IR > 3.5) or right_IR < 1.2:
            current_state="right"
            last_turning_state = "right"
            corrected_line_excursion = False
        elif (left_IR > 1.2 and centre_IR > 1.2 and right_IR > 1.2):
            if (last_turning_state == "left"):
                current_state = "corner_left"
            else:
                current_state = "corner_right"
        set_state(current_state)

task5()
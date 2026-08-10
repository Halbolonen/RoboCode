from sbot import motors, utils

while True:
    # 1 is left 0 is right
    motors.set_power(0, 0.5)
    motors.set_power(1, 0.475)
    utils.sleep(5)
    motors.set_power(0,0)
    motors.set_power(1,0)
    utils.sleep(5)
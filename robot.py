from sbot import motors, utils

while True:
    motors.set_power(0, 0.5)
    motors.set_power(1, 0)
    utils.sleep(2)

    motors.set_power(1, 0.5)
    utils.sleep(2)

    motors.set_power(0, 0)
    utils.sleep(2)

    motors.set_power(0,0.5)
    motors.set_power(1,-0.5)
    utils.sleep(5)

    motors.set_power(0,0)
    motors.set_power(1,0)
    utils.sleep(2)
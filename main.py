basic.show_icon(IconNames.HEART)

def on_forever():
    for i in range(4):
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 120)
        basic.pause(1000)

        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(200)

        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, 120)
        basic.pause(450)

        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(200)

basic.forever(on_forever)
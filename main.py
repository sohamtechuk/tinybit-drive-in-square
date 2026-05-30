def on_forever():
    Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 120)
    basic.pause(1000)

    Tinybit.RGB_Car_Big(Tinybit.enColor.Red)
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, 120)
    basic.pause(450)

    Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 120)
    basic.pause(1000)

    Tinybit.RGB_Car_Big(Tinybit.enColor.Blue)
    Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinLeft, 120)
    basic.pause(450)

    Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
    Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
    basic.pause(500)

basic.forever(on_forever)
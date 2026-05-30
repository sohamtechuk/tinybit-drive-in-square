basic.showIcon(IconNames.Heart)
basic.forever(function on_forever() {
    for (let i = 0; i < 4; i++) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 120)
        basic.pause(1000)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(200)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, 120)
        basic.pause(450)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(200)
    }
})

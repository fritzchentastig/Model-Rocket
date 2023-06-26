# Model-Rocket

## Description

This is a Project by fritchentastig and xByNilzz

It consists of the code used on the arduino, plans for the electrical circuits, the math and models we use to calculate all of this.

All of this is for our project, do not use this stuff if you don't know what all of this means and know how to adapt this to your project.

## Table of content

1. Explanations
    1. Electrical Wiring
    2. Rocket Computer
    3. The RES-Computer
2. Hardware
    1. Motor
    2. Shell
    3. Nozzle
    4. Cone
    5. Fins
6. Real-world tests
7. The future of the Project


## Explanations

### electrical wiring
The wiring is simple and a diagramm can be found in (../Electrical)

The 10kOhm Resistors are pulldown resistors. The resistors in the led circuits prevent burning the LED.

### Rocket-Computer
The Rocket-Computer is a Raspberry Pico running MicroPython. It serves as the rocket´s brain. after being armed and the start sequenze initiated it gives a countdown via an external LED and after being started it counts down a predetermined number of seconds. This Number is calculated before via an external software. We decided not to run these calculations on the Pico because it would be a hard task for the RP2040 of the Pico.

The RC does **not** control the fuel ignition for safety reasons. It just gives a countdown to start. It can determine when and if it started by connecting to the startpad of the rocket.

### The RES-Computer
The RES(Rocket-Enviremont-Simulator) is another Raspberry Pico that is connect (not directly) to the Rocket-Computer. It can read out action the RC performs and can signals to the RC. From the RCs perspective it will look like a real flight.

## Hardware

### Motor

The rocket uses standart D9P model rocket motors.

### Shell

The Shell is made of plexiglass

### Nozzle

The Nozzle is made out of bent sheet metal: Soon

### Cone

The cone is resin 3d printed. Files available: Soon

### Fins

The fins are made of plywood and cut with a saw.

# Real-world tests

To be done

# The future of the project

This Project is *mainly* a school project. Although it is planned to continue this project regular commits are not to be expected after June 28.


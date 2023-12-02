from patterns import Factory, ControlSystem

if __name__ == '__main__':
    light = Factory.get("Light")
    camera = Factory.get("Camera")

    control_system = ControlSystem()

    control_system.attach(light)
    control_system.attach(camera)

    control_system.hack_event()


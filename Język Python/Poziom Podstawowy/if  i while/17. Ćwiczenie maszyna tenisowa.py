def route():
    while True:
        if front() > 0.5:
            move
            continue
        elif left() > 0.5:
                turnL()
                move()
        elif right() > 0.5:
                turnR()
                move()
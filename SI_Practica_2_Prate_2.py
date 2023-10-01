import Leap, sys, thread, time

class SampleListener(Leap.Listener):
    # ... (mismo que antes)

    def on_frame(self, controller):
        frame = controller.frame()

        # Check if there are hands in the frame
        if not frame.hands.is_empty:
            # Get the first hand (assuming one hand is used for gestures)
            hand = frame.hands[0]

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            pitch = direction.pitch * Leap.RAD_TO_DEG
            roll = normal.roll * Leap.RAD_TO_DEG
            yaw = direction.yaw * Leap.RAD_TO_DEG

            # Save the angles to a text file
            with open("gesture_data.txt", "a") as file:
                # Write the angles to the file (comma-separated)
                file.write(f"{pitch},{roll},{yaw}\n")

        # Rest of the code remains the same

    # ... (El resto de la clase es lo mismo)


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()

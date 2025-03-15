import os  # For use in locating paths
from playsound import playsound  # For playing the alarm sounds
import time  # For sleeping

# Set up the progress bar characters
barChar = "⣿"
progressChar = "█"

# Set the work and rest times in minutes
workTime = 50  # minutes
restTime = 10  # minutes

# Convert the minutes for work and rest into seconds
workTimeS = workTime * 60
restTimeS = restTime * 60

# Initiate the session counter (not used)
session = 1

# Retrieve the path to the script (used for playing the sound)
path = os.path.dirname(__file__)
bells = os.path.join(path, "Pomodoro Alarm Bells.mp3")


# The rendering function
def renderProgressBar(message, currentTime, fullTime, colour):
    # Clear the screen before writing anything new to the screen
    os.system("clear")
    progress = 1 - currentTime / fullTime  # Calculate the progress percentage

    # Format the progress percentage as a percentage
    progressString = format(progress, ".0%")

    # Calculate the individual minutes of the timer
    minutes = str(int(currentTime / 60)).zfill(2)
    # Calculate the individual seconds of the timer
    seconds = str(currentTime % 60).zfill(2)

    # join the minutes and seconds variable together to get the countdown
    timer = " %s:%s " % (minutes, seconds)

    # === Calculate the width of the current window ===
    windowWidth = os.get_terminal_size()[0] - len(message) - len(progressString) - 3
    progressWidth = int(windowWidth * progress)
    timerStart = int(windowWidth / 2 - (len(timer) / 2))

    # === Draw the progress bar ===
    bar = barChar * windowWidth + " " + progressString  # build the initial bar
    # Add the message to the bar, as well as the progress part of the bar
    bar = message + " " + progressChar * progressWidth + bar[progressWidth:]
    # Add the timer in the middle of the progress bar
    bar = (
        bar[: timerStart + len(message)]
        + timer
        + bar[timerStart + len(timer) + len(message) :]
    )

    print("")  # Add a little blank line
    print(colour + bar + "\033[1;00m")  # Write the bar to the screen


while True:  # Loop indefinitely
    currentTime = workTimeS  # Set the current time to the work time seconds

    # Count down for the work time
    for i in range(workTimeS):  # loop though all the seconds of work
        # Call the render progress bar function
        renderProgressBar(" [Working]", currentTime, workTimeS, "\033[1;34m")

        # Sleep for one second and count decrement the current time by one
        time.sleep(1)
        currentTime -= 1

    # Play the alarm sound to indicate that the timer has run out
    renderProgressBar(" [Working]", currentTime, workTimeS, "\033[1;34m")
    playsound(bells)

    currentTime = restTimeS

    for i in range(restTimeS):
        # Call the render progress bar function
        renderProgressBar(" [Resting]", currentTime, restTimeS, "\033[1;31m")

        # Sleep for one second and count decrement the current time by one
        time.sleep(1)
        currentTime -= 1

    # Play the alarm sound to indicate that the timer has run out
    renderProgressBar(" [Resting]", currentTime, restTimeS, "\033[1;31m")
    playsound(bells)

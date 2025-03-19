import os  # For use in locating paths
from playsound import playsound  # For playing the alarm sounds
import time  # For sleeping

# ======================== C O N F I G U R A T I O N ======================== #

# Set up the progress bar characters
barChar = "⣿"
progressChar = "█"

# Set the work and rest times in minutes
prepTime = 2
workTime = 50  # minutes
restTime = 10  # minutes

# =========================================================================== #

# Convert the minutes for work and rest into seconds
second = 60  # minutes
prepTimeS = prepTime * second
workTimeS = workTime * second
restTimeS = restTime * second

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
    progressString = format(progress, ".0%") + " │"

    # Calculate the individual minutes of the timer
    minutes = str(int(currentTime / 60)).zfill(2)
    # Calculate the individual seconds of the timer
    seconds = str(currentTime % 60).zfill(2)

    # join the minutes and seconds variable together to get the countdown
    timer = " %s:%s " % (minutes, seconds)

    # === Calculate the width of the current window ===
    windowWidth = os.get_terminal_size()[0]
    barWidth = windowWidth - len(message) - len(progressString) - 2
    progressWidth = int(barWidth * progress)
    timerStart = 1 + int(barWidth / 2 - (len(timer) / 2))

    # === Draw the progress bar ===
    bar = barChar * barWidth + " " + progressString  # build the initial bar
    # Add the message to the bar, as well as the progress part of the bar
    bar = message + " " + progressChar * progressWidth + bar[progressWidth:]
    # Add the timer in the middle of the progress bar
    bar = (
        bar[: timerStart + len(message)]
        + timer
        + bar[timerStart + len(timer) + len(message) :]
    )

    # Create the surrounding lines to make the app prettier, but also have
    # more colour so it's easier to see the colour at a glance

    top = "╭" + "─" * (windowWidth - 2) + "╮"
    bottom = "╰" + "─" * (windowWidth - 2) + "╯"

    print(colour + top)
    print(bar)  # Write the bar to the screen
    print(bottom + "\033[1;00m")


# Get ready timer
currentTime = prepTimeS
for i in range(prepTimeS):
    # Call the render progress bar function
    renderProgressBar("│[Preparing]", currentTime, prepTimeS, "\033[1;32m")

    # Sleep for one second and count decrement the current time by one
    time.sleep(1)
    currentTime -= 1

# Play the alarm sound to indicate that the timer has run out
playsound(bells, False)


while True:  # Loop indefinitely
    currentTime = workTimeS  # Set the current time to the work time seconds

    # Count down for the work time
    for i in range(workTimeS):  # loop though all the seconds of work
        # Call the render progress bar function
        renderProgressBar("│[Working]", currentTime, workTimeS, "\033[1;34m")

        # Sleep for one second and count decrement the current time by one
        time.sleep(1)
        currentTime -= 1

    # Play the alarm sound to indicate that the timer has run out
    renderProgressBar("│[Working]", currentTime, workTimeS, "\033[1;34m")
    playsound(bells, False)

    currentTime = restTimeS

    for i in range(restTimeS):
        # Call the render progress bar function
        renderProgressBar("│[Resting]", currentTime, restTimeS, "\033[1;31m")

        # Sleep for one second and count decrement the current time by one
        time.sleep(1)
        currentTime -= 1

    # Play the alarm sound to indicate that the timer has run out
    renderProgressBar("│[Resting]", currentTime, restTimeS, "\033[1;31m")
    playsound(bells, False)

import turtle
import pandas as pd

# Setup Turtle Screen 
display = turtle.Screen()
display.title("Indian States Quiz")
display.setup(width = 600, height = 600)
display.bgpic('indian-map.gif')    # Set image as background

# Load Data from CSV file
data = pd.read_csv('states_list.csv')
all_states = data.State.to_list()

# Stores All the Guessed States
guessed_states = []   

# Main Loop 
while len(guessed_states) < 28:
    user_input = display.textinput(f"Guess State {len(guessed_states)}/28","Go on")
   
    # If User closes Input or Clicks Cancel 
    if user_input is None:
        break

    # Change Input to title Case
    user_input = user_input.title()

    # Breaks out of While Loop if User Enters exit
    if user_input == "Exit":
        break

    # Fetching Coordinates and Writing Data
    if user_input in all_states:
        guessed_states.append(user_input)
        data1 = data[data.State == user_input]
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(data1.x.item(), data1.y.item()) 
        writer.write(user_input,font=("Arial",8,'normal'))

    elif user_input not in all_states:
        # Show error in the next prompt
        display.textinput("Invalid State!", f"'{user_input}' is not valid.\nPress OK to try again." )

# Stores All Missed States
missed_states = [ state for state in all_states if state not in guessed_states]

df = pd.DataFrame(missed_states,columns=['Missed States'])

# Creates a CSV file which contains All Missed States 
df.to_csv('learn_states.csv')

turtle.done()
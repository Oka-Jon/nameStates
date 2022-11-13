import turtle
import pandas

FONT = ('Arial', 8, 'normal')
LIVES_FONT = ('Arial', 20, 'normal')

state_data = pandas.read_csv("50_states.csv")
state_list = state_data["state"].to_list()

screen = turtle.Screen()
screen.setup(width=800, height=500)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_text = turtle.Turtle()
state_text.penup()
state_text.hideturtle()
lives = turtle.Turtle()
lives.penup()
lives.hideturtle()

playing = True
correct = 0
guessed = []
lives_remaining = 3

with open("highscore.txt") as f:
    high_info = f.readlines()
    high_user = high_info[0][:-1]
    high_score = int(high_info[1])

lives.goto(0, 220)
lives.write(f"Tries Remaining: {lives_remaining} | High Score: {high_score} by {high_user}", align="center",
            font=LIVES_FONT)

while playing:
    answer = screen.textinput(title=f"{correct}/50 States Named", prompt="Write a State Name")
    answer_cap = answer.title()
    if answer_cap in state_list and answer_cap not in guessed:
        is_there = state_data[state_data.state == answer_cap]
        state_text.goto(int(is_there.x), int(is_there.y))
        state_text.write(f"{answer_cap}", align="center", font=FONT)
        guessed.append(answer_cap)
        correct += 1
    else:
        if lives_remaining == 0:
            playing = False
            lives.goto(0, 0)
            lives.write("Game Over", align="center", font=LIVES_FONT)
            continue
        lives_remaining -= 1
        lives.clear()
        lives.write(f"Tries Remaining: {lives_remaining} | High Score: {high_score} by {high_user}", align="center",
                    font=LIVES_FONT)

if len(guessed) > high_score:
    user = screen.textinput(title="Player Name", prompt="Enter your name for the high score")
    with open("highscore.txt", mode="w") as f:
        f.write(f"{user}\n{len(guessed)}")

screen.exitonclick()

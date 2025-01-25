from turtle import Turtle, Screen;
import pandas;

screen = Screen();
screen.title('US States Game');
image = 'Day 25/us_state_game/blank_states_img.gif'

screen.addshape(image);

turtle = Turtle();

turtle.shape(image);

score = 0;


states_data = pandas.read_csv('Day 25/us_state_game/50_states.csv');
right_answer = [];
all_states = states_data.state.to_list();

while len(right_answer) < 50:

    answer = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state name").capitalize();

    try:

        if answer == 'Exit':
            states_left = [item for item in all_states if item not in right_answer];
            states_left_csv = pandas.DataFrame(states_left);
            states_left_csv.to_csv('Day 25/us_state_game/states_left.csv');
            break;
        


        my_data = states_data[states_data.state == answer];
        if my_data.state.item() not in right_answer:
            if answer == my_data.state.item():
                state_name = my_data.state.item();
                state_x = my_data.x.item();
                state_y = my_data.y.item();
                score += 1;
                right_answer.append(state_name);

                state_turtle = Turtle();
                state_turtle.color('black');
                state_turtle.penup();
                state_turtle.hideturtle();
                state_turtle.goto(state_x, state_y);
                state_turtle.write(arg=f"{state_name}", align='center', font=('verdana', 13, 'italic'));
                print(right_answer);


        
    except:
        print('no');


turtle.mainloop();
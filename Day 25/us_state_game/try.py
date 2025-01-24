import pandas;


states_data = pandas.read_csv("Day 25/us_state_game/50_states.csv");

answer = "Alaska"

my_data = states_data[states_data.state == answer];

try:
    if answer == my_data.state.item():
        state_name = my_data.state.item();
        state_x = my_data.x.item();
        state_y = my_data.y.item();
        
except:
    print('no');
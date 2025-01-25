import pandas;


states_data = pandas.read_csv("Day 25/us_state_game/50_states.csv");

answer = "risab"

states = states_data.state.to_list();

if answer in states:
    print('yes')
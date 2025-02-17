import time
current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    time_now = time.time();
    function()
    after_function_time = time.time();
    time_difference = after_function_time - time_now;
    print(f"{function.__name__} run speed: {time_difference} ");
    

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

# fast_decorator = speed_calc_decorator(fast_function);
# print('fast_function run speed', fast_decorator());
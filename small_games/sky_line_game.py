def sky_line(my_str):
    for i in range (0, len(my_str)):       
        if i % 2 == 0:
            my_str = my_str[:i] + my_str[i:].capitalize()
        
    return my_str

print(sky_line('TTTest'))
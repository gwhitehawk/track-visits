import math

width = 100
height = 30
label_step = 5
label_pad = 10

def print_bar_chart(x_values, y_values):
    result = ""
    
    # get y range
    max = y_values[0]
    min = y_values[0]
    
    for y in y_values:
        if y > max:
            max = y

        if y < min:
            min = y
    
    # get x range
    number_of_vals = len(x_values)

    # scale y axis, 1 row = vert_step
    vert_step = float(max-min)/height
    
    # scale x axis, 1 x value = hori_step columns
    hori_step = int(round(float(width)/number_of_vals))

    # left figure padding
    pad = ""
    for i in range(label_pad):
        pad += " "

    # draw graph row by row
    for row in range(height):

        # label every label_step th row    
        if (row%label_step == 0):
            label = str(round(min+float(max-min)*(height-1-row)/(height-1), 2))
            label_len = label.__len__()
            for i in range(label_pad - label_len):
                label += " "
        else:
            label = pad

        result += label + "|"
        
        for x in range(number_of_vals):
            result += " "
            for i in range(hori_step):
                if (y_values[x] >= min+float(max-min)*(height-1-row)/(height-1)):
                    result += "*"
                else:
                    result += " "
        result += "\n"

    # draw x axis
    x_axis = pad

    for x in range(number_of_vals):
        for i in range(hori_step+1):
            x_axis += "_"

    result += x_axis + "\n"

    # draw x labels
    x_labels = pad + " "
    for x in range(number_of_vals):
        x_labels += " "
        label = str(x_values[x])
        if (label.__len__() > hori_step):
            label = label[:hori_step]
        
        x_labels += label
        for i in range(hori_step-label.__len__()):
            x_labels += " "

    result += x_labels + "\n"
            
    print result 
    return result 
        

from tkinter import *
from random import randint as rand
from math import sqrt, ceil

###

def init(points):
    global tr
    canvas.delete(tr)
    tr = canvas.create_line(points[0], points[1], points[2], points[3], 
    points[4], points[5], points[0], points[1])

def generate(points):
    shift = 100
    for point in range(6):
        points.append(rand(0, 200) + shift) #x1, y1, x2, y2, x3, y3
    return 2 * rand(5, 50) #even length

def is_solution(solution):
    text2.configure(state='normal')
    text2.delete(1.0, END)
    if solution:
        text2.insert(END, "decided", "center")
    else:
        text2.insert(END, "impossible", "center")
    text2.configure(state='disabled')

###

def is_intersect(a1, a2, a3, a4):
    if (a1 > a2): a1, a2 = a2, a1
    if (a3 > a4): a3, a4 = a4, a3
    return max(a1, a3) <= min(a2, a4)

def area(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

def valid_direct(line1, line2):
    return not (is_intersect(line1[0], line1[2], line2[0], line2[2]) and
    is_intersect(line1[1], line1[3], line2[1], line2[3]) and
    area(line1[0], line1[1], line1[2], line1[3], line2[0], line2[1]) * 
    area(line1[0], line1[1], line1[2], line1[3], line2[2], line2[3]) <= 0 and
    area(line2[0], line2[1], line2[2], line2[3], line1[0], line1[1]) * 
    area(line2[0], line2[1], line2[2], line2[3], line1[2], line1[3]) <= 0) #area method

###

def line_border(x1, y1, x2, y2, L, x, y):
    point = []
    cos = x1 * x2 + y1 * y2
    if cos <= 0:
        point.append(x)
        point.append(y)
        return point
    sin = sqrt(1 - cos * cos)
    ctg = cos/sin
    point.append(x + (L/2) * ctg * x2)
    point.append(y + (L/2) * ctg * y2)
    return point

def Iter(bord1, bord2, pr_x, pr_y):
    if pr_x != 0:
        p = (bord1[0] - bord2[0]) / pr_x
    elif pr_y != 0:
        p = (bord1[1] - bord2[1]) / pr_y
    else:
        p = -1
    return p

def algoc(border_point, pr_vec_x, pr_vec_y, op_vec_x, op_vec_y, L):
    answer_points = [0, 0, 0, 0, 0, 0]
    I = Iter(border_point[1], border_point[0], pr_vec_x[0], pr_vec_y[0])
    J = Iter(border_point[3], border_point[2], pr_vec_x[1], pr_vec_y[1])
    K = Iter(border_point[5], border_point[4], pr_vec_x[2], pr_vec_y[2])
    if I < 0 or J < 0 or K < 0: 
        return False, answer_points

    line1 = [0, 0, 0, 0]; line2 = [0, 0, 0, 0]; line3 = [0, 0, 0, 0]

    for i in range(ceil(I) - 1):
        answer_points[0] = border_point[0][0] + i * pr_vec_x[0]
        answer_points[1] = border_point[0][1] + i * pr_vec_y[0]
        for j in range(ceil(J) - 1):
            answer_points[2] = border_point[2][0] + j * pr_vec_x[1]
            answer_points[3] = border_point[2][1] + j * pr_vec_y[1]
            line2[0] = answer_points[2] - L/2 * op_vec_x[1]
            line1[0] = answer_points[0] - L/2 * op_vec_x[0]
            line2[1] = answer_points[3] - L/2 * op_vec_y[1]
            line1[1] = answer_points[1] - L/2 * op_vec_y[0]
            line2[2] = answer_points[2] + L/2 * op_vec_x[1]
            line1[2] = answer_points[0] + L/2 * op_vec_x[0]
            line2[3] = answer_points[3] + L/2 * op_vec_y[1]
            line1[3] = answer_points[1] + L/2 * op_vec_y[0]
            if valid_direct(line1, line2):
                for k in range(ceil(K) - 1):
                    answer_points[4] = border_point[4][0] + j * pr_vec_x[2]
                    answer_points[5] = border_point[4][1] + j * pr_vec_y[2]
                    line3[0] = answer_points[4] - L/2 * op_vec_x[2]
                    line2[0] = answer_points[2] - L/2 * op_vec_x[1]
                    line1[0] = answer_points[0] - L/2 * op_vec_x[0]
                    line3[1] = answer_points[5] - L/2 * op_vec_y[2]
                    line2[1] = answer_points[3] - L/2 * op_vec_y[1] 
                    line1[1] = answer_points[1] - L/2 * op_vec_y[0]
                    line3[2] = answer_points[4] + L/2 * op_vec_x[2]
                    line2[2] = answer_points[2] + L/2 * op_vec_x[1]
                    line1[2] = answer_points[0] + L/2 * op_vec_x[0]
                    line3[3] = answer_points[5] + L/2 * op_vec_y[2]
                    line2[3] = answer_points[3] + L/2 * op_vec_y[1]
                    line1[3] = answer_points[1] + L/2 * op_vec_y[0]
                    if valid_direct(line1, line3) and valid_direct(line2, line3):
                        return True, answer_points
    return False, answer_points

###

def existence(points, L):
    pass

def stupid_existence(points, L): #enumeration
    vec_x = []; vec_y = []; op_vec_x = []; op_vec_y = []; pr_vec_y = []; pr_vec_x = []; 
    for i in range(3):
        vec_x.append(points[2*(i+1) % 6] - points[2*i % 6])
        vec_y.append(points[(2*(i+1) + 1) % 6] - points[(2*i + 1) % 6]) #auxiliary vectors
        if vec_x[i] == 0 and vec_y[i] == 0:
            is_solution(False)
            return

        op_vec_x.append(-vec_y[i]/(sqrt(pow(vec_x[i], 2) + pow(vec_y[i], 2))))
        op_vec_y.append(vec_x[i]/(sqrt(pow(vec_x[i], 2) + pow(vec_y[i], 2))))
        pr_vec_x.append(op_vec_y[i])
        pr_vec_y.append(-op_vec_x[i]) #unit vectors

    border_point = []

    border_point.append(line_border(-pr_vec_x[2], -pr_vec_y[2], pr_vec_x[0], pr_vec_y[0], L, points[0], points[1]))
    border_point.append(line_border(pr_vec_x[1], pr_vec_y[1], -pr_vec_x[0], -pr_vec_y[0], L, points[2], points[3]))
    border_point.append(line_border(-pr_vec_x[0], -pr_vec_y[0], pr_vec_x[1], pr_vec_y[1], L, points[2], points[3]))
    border_point.append(line_border(pr_vec_x[2], pr_vec_y[2], -pr_vec_x[1], -pr_vec_y[1], L, points[4], points[5]))
    border_point.append(line_border(-pr_vec_x[1], -pr_vec_y[1], pr_vec_x[2], pr_vec_y[2], L, points[4], points[5]))
    border_point.append(line_border(pr_vec_x[0], pr_vec_y[0], -pr_vec_x[2], -pr_vec_y[2], L, points[0], points[1]))

    '''
    global li
    for i in range(3):
        canvas.delete(li[2*i])
        canvas.delete(li[2*i + 1])
        li[2*i] = canvas.create_line(border_point[2*i][0] - op_vec_x[i] * L/2, 
        border_point[2*i][1] - op_vec_y[i] * L/2, border_point[2*i][0] + 
        op_vec_x[i] * L/2, border_point[2*i][1] + op_vec_y[i] * L/2, dash=(4, 2))
        li[2*i + 1] = canvas.create_line(border_point[2*i + 1][0] - op_vec_x[i] * L/2,
         border_point[2*i + 1][1] - op_vec_y[i] * L/2, border_point[2*i + 1][0] + 
         op_vec_x[i] * L/2, border_point[2*i + 1][1] + op_vec_y[i] * L/2, dash=(4, 2)) #drawing borders
    '''

    answer_points = [0, 0, 0, 0, 0, 0]
    find, answer_points = algoc(border_point, pr_vec_x, pr_vec_y, op_vec_x, op_vec_y, L)

    global li
    for i in range(3):
        canvas.delete(li[i])

    if not find:
        is_solution(False)
        return
    is_solution(True)
    
    for i in range(3):
        li[i] = canvas.create_line(answer_points[2*i] - op_vec_x[i] * L/2, 
        answer_points[2*i+1] - op_vec_y[i] * L/2, answer_points[2*i] + 
        op_vec_x[i] * L/2, answer_points[2*i+1] + op_vec_y[i] * L/2, dash=(4, 2))

###

def main():
    points = []
    L = generate(points)
    text.configure(state='normal')
    text.delete(1.0, END)
    text.insert(END, L, "center")
    text.configure(state='disabled')
    init(points)
    existence(points, L)
    stupid_existence(points, L)
    root.mainloop()

###

W = H = 400
root = Tk()
root.geometry(str(W) + "x" + str(H) + "+500+200")
panelFrame = Frame(root, width = W, height = 40)
panelFrame.pack(side = 'top')

but_redo = Button(panelFrame, text = 're-', command = main)
but_redo.bind("<Button>")
but_redo.pack()
but_redo.place(x = W/3, y = 0, width = W/3, height = 40)

text = Text(panelFrame)
text.configure(state='disabled', font=("Verdana", 16), cursor="arrow")
text.pack()
text.place(x = 0, y = 0, width = W/3, height = 40)

text2 = Text(panelFrame)
text2.configure(state='disabled', font=("Verdana", 16), cursor="arrow")
text2.pack()
text2.place(x = W*2/3, y = 0, width = W/3, height = 40)

canvas = Canvas(root, width = W, height = H)
canvas.pack()
tr = canvas.create_line(0, 0, 0, 0)
li = [0, 0, 0]

###

if __name__ == '__main__': main()

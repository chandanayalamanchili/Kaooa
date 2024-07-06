import turtle
import time

class Game:
    def __init__(self):
        self.circles = []
        self.vertices = []
        self.curr_vulture_pos = -1
        self.radius = 20
        self.game_ended = False
        self.vulture_count = 0
        self.crow_count = 0
        self.kill_count = 0
        self.prev_i = -1
        self.prev_i_crow = -1
        self.occupancy = [0 for _ in range(10)]
        self.i = 0
        turtle.title("Kaooa board game")
        self.neighbours = {0:[[5,6],[9,8]], 1:[[6,5],[7,8]], 2:[[8,7],[9,5]], 3:[[5,9],[6,7]],4:[[7,6],[8,9]], 5:[[0,None],[6,1],[3,None],[9,2]],6:[[5,0],[7,4],[1,None],[3,None]],7:[[6,3],[8,2],[4,None],[1,None]],8:[[9,0],[7,1],[2,None],[4,None]],9:[[5,3],[0,None],[2,None],[8,4]]}
        self.screen = turtle.Screen()
        self.screen.screensize(800, 800)
        self.screen.tracer(0)
        self.screen.bgcolor("pink")

        self.star = turtle.Turtle()
        self.star.pensize(3)
        self.star.penup()
        self.star.goto(-300, 100)
        self.star.pendown()

        self.star.color("black")

        outer_vertices = []

        self.star.begin_fill()
        for i in range(5):
            outer_vertices.append(self.star.pos())
            self.star.forward(600)
            self.star.right(144)

        inner_vertices = []
        inner_vertices.append(self.get_intersections(outer_vertices[0][0], outer_vertices[0][1], outer_vertices[1][0], outer_vertices[1][1], outer_vertices[2][0],outer_vertices[2][1],outer_vertices[3][0],outer_vertices[3][1]))
        inner_vertices.append(self.get_intersections(outer_vertices[0][0], outer_vertices[0][1], outer_vertices[1][0], outer_vertices[1][1], outer_vertices[3][0],outer_vertices[3][1],outer_vertices[4][0],outer_vertices[4][1]))
        inner_vertices.append(self.get_intersections(outer_vertices[1][0], outer_vertices[1][1], outer_vertices[2][0], outer_vertices[2][1], outer_vertices[4][0],outer_vertices[4][1],outer_vertices[3][0],outer_vertices[3][1]))
        inner_vertices.append(self.get_intersections(outer_vertices[1][0], outer_vertices[1][1], outer_vertices[2][0], outer_vertices[2][1], outer_vertices[4][0],outer_vertices[4][1],outer_vertices[0][0],outer_vertices[0][1]))
        inner_vertices.append(self.get_intersections(outer_vertices[0][0], outer_vertices[0][1], outer_vertices[4][0], outer_vertices[4][1], outer_vertices[2][0],outer_vertices[2][1],outer_vertices[3][0],outer_vertices[3][1]))

        self.vertices.extend(outer_vertices)
        self.vertices.extend(inner_vertices)

        for vertex in self.vertices:
            self.circle = turtle.Turtle()  
            self.circle.penup()
            new_vertex = (vertex[0], vertex[1] - self.radius)
            self.circle.goto(new_vertex)
            self.circle.pendown()
            self.circle.fillcolor('white')
            self.circle.begin_fill()
            self.circle.circle(self.radius)
            self.circle.end_fill()
            self.circles.append(self.circle)

        self.writer = turtle.Turtle()
        self.writer.penup()
        self.flag = False
        self.writer.goto(170, 300)
        self.writer.pendown()
        self.writer.fillcolor('green')
        self.writer.begin_fill()
        self.writer.circle(10)
        self.writer.end_fill()
        self.writer.penup()
        self.writer.goto(170, 325)
        self.writer.pendown()
        self.writer.fillcolor('skyblue')
        self.writer.begin_fill()
        self.writer.circle(10)
        self.writer.end_fill()  
        self.writer.penup()
        self.writer.goto(170, 350)
        self.writer.pendown()
        self.writer.fillcolor('yellow')
        self.writer.begin_fill()
        self.writer.circle(10)
        self.writer.end_fill()      
        self.writer.penup()
        self.writer.goto(200, 300)
        self.writer.write("Yellow is Vulture\nSkyblue is Crow\nGreen is Current selected coin", font=("Times New Roman", 14, "normal"))
        self.writer.hideturtle()

        self.star.hideturtle()
        for circle in self.circles:
            circle.hideturtle()
        self.screen.update()

        self.start_game()
        turtle.mainloop()

    def get_intersections(self, x1, y1, x2, y2, x3, y3, x4, y4):
        m1 = (y2-y1)/(x2-x1)
        m2 = (y4-y3)/(x4-x3)
        x = ((m1 * x1 - y1) - (m2 * x3 - y3)) / (m1 - m2)
        y = m1 * (x - x1) + y1
        return (x, y)

    def is_inside_circle(self, x, y, center):
        return (x - center[0])**2 + (y - center[1])**2 <= self.radius**2
    
    def start_game(self):
        self.writer.goto(0,0)
        self.writer.write("Game Started!!\nPlace a Crow",font=("Poppins","14","bold"),align="center")
        self.screen.onscreenclick(self.select_or_move_circle)

    def select_or_move_circle(self, x, y):
        self.writer.undo()
        # print("self.i value: ",self.i)
        # print("Vulture: ",self.vulture_count)
        self.check_game_end()
        if self.game_ended:
            self.star.reset()
            for circle in self.circles:
                circle.reset()
            self.writer.reset()
            if self.check_crows_win():
                self.writer.goto(0,0)
                self.writer.write("Game Over!!\nCrows win!!",font=("Poppins","32","bold"),align="center" )
            if self.check_vulture_win():
                self.writer.goto(0,0)
                self.writer.write("Game Over!!\nVulture win!!",font=("Poppins","32","bold"),align="center")
        else:
            if self.i % 2 == 0 and self.crow_count < 7:
                for i, center in enumerate(self.vertices):
                    if self.is_inside_circle(x, y, center) and self.occupancy[i] == 0:
                        # print("condition-1")
                        self.circles[i].fillcolor('skyblue') 
                        self.circles[i].begin_fill()
                        self.circles[i].circle(self.radius)
                        self.circles[i].end_fill()
                        self.crow_count += 1
                        self.i += 1
                        self.occupancy[i] = 2
                        break
            elif self.i % 2 == 0 and self.crow_count == 7:
                # print("condition-2")
                for i, center in enumerate(self.vertices):
                    if self.is_inside_circle(x, y, center):
                        if self.occupancy[i] == 2:
                            if self.prev_i_crow != -1:
                                self.circles[self.prev_i_crow].fillcolor('skyblue')
                                self.circles[self.prev_i_crow].begin_fill()
                                self.circles[self.prev_i_crow].circle(self.radius)
                                self.circles[self.prev_i_crow].end_fill()
                            self.prev_i_crow = i
                            # print("green")
                            self.circles[i].fillcolor('green')
                            self.circles[i].begin_fill()
                            self.circles[i].circle(self.radius)
                            self.circles[i].end_fill()
                        elif self.occupancy[i] == 0 and self.prev_i_crow != -1:
                            if self.is_adjacent(i, self.prev_i_crow):
                                self.occupancy[self.prev_i_crow] = 0
                                self.occupancy[i] = 2
                                self.i += 1
                                self.prev_i_crow = -1
                            for i in range(0, len(self.occupancy)):
                                    if self.occupancy[i] == 0:
                                        self.circles[i].fillcolor('white')
                                        self.circles[i].begin_fill()
                                        self.circles[i].circle(self.radius)
                                        self.circles[i].end_fill()
                                    elif self.occupancy[i] == 2:
                                        self.circles[i].fillcolor('skyblue')
                                        self.circles[i].begin_fill()
                                        self.circles[i].circle(self.radius)
                                        self.circles[i].end_fill()
                        break

            elif self.i % 2 != 0 and self.vulture_count == 0:
                # print("condition-3")
                for i, center in enumerate(self.vertices):
                    if self.is_inside_circle(x, y, center) and self.occupancy[i] == 0 and self.vulture_count == 0:
                        self.occupancy[i] = 1
                        self.curr_vulture_pos = i
                        self.i += 1
                        self.vulture_count += 1
                        for i in range(0, len(self.occupancy)):
                                if self.occupancy[i] == 0:
                                    self.circles[i].fillcolor('white')
                                    self.circles[i].begin_fill()
                                    self.circles[i].circle(self.radius)
                                    self.circles[i].end_fill()
                                elif self.occupancy[i] == 1:
                                    self.circles[i].fillcolor('yellow')
                                    self.circles[i].begin_fill()
                                    self.circles[i].circle(self.radius)
                                    self.circles[i].end_fill()
                        break

            elif self.i % 2 != 0 and self.vulture_count != 0:
                # print("condition-4")
                for i, center in enumerate(self.vertices):
                    if self.is_inside_circle(x, y, center):
                        if self.occupancy[i] == 1:
                            self.prev_i = i
                            self.circles[i].fillcolor('green')
                            self.circles[i].begin_fill()
                            self.circles[i].circle(self.radius)
                            self.circles[i].end_fill()
                        elif self.occupancy[i] == 0 and self.prev_i != -1:
                            if self.is_adjacent(i, self.prev_i):
                                self.occupancy[self.prev_i] = 0
                                self.occupancy[i] = 1
                                self.curr_vulture_pos = i
                                self.i += 1
                                self.prev_i = -1
                            elif self.can_jump(self.prev_i, i):
                                # print(self.prev_i)
                                self.kill_count += 1
                                self.occupancy[self.prev_i] = 0
                                self.occupancy[i] = 1
                                self.curr_vulture_pos = i
                                self.i += 1
                                self.flag = True
                                # self.screen.ontimer(self.writer.undo(),5000)
                                self.prev_i = -1
                            for i in range(0, len(self.occupancy)):
                                if self.occupancy[i] == 0:
                                    self.circles[i].fillcolor('white')
                                    self.circles[i].begin_fill()
                                    self.circles[i].circle(self.radius)
                                    self.circles[i].end_fill()
                                elif self.occupancy[i] == 1:
                                    self.circles[i].fillcolor('yellow')
                                    self.circles[i].begin_fill()
                                    self.circles[i].circle(self.radius)
                                    self.circles[i].end_fill()
                        break
        self.check_game_end()
        if self.game_ended:
            self.star.reset()

            self.writer.reset()
            for circle in self.circles:
                circle.reset()
            if self.check_crows_win():
                self.writer.goto(0,0)
                self.writer.write("Crows win",font=("Poppins","32","bold"))
            if self.check_vulture_win():
                self.writer.goto(0,0)
                self.writer.write("Vulture win",font=("Poppins","32","bold"))
        elif self.i % 2 == 0:
            if self.crow_count < 7:
                if self.flag:
                    self.writer.write(f"Crow kill count = {self.kill_count}\nPlace Crow",font=("Poppins","10","bold"),align="center")
                    self.flag = False
                else:
                    self.writer.write("Place Crow",font=("Poppins","14","bold"),align="center")
            elif self.crow_count == 7:
                if self.flag:
                    self.writer.write(f"Crow kill count = {self.kill_count}\nMove Crow",font=("Poppins","10","bold"),align="center")
                    self.flag = False
                else:
                    self.writer.write("Move Crow",font=("Poppins","14","bold"),align="center")
        elif self.i%2 !=0:
            if self.vulture_count == 0:
                self.writer.write("Place Vulture",font=("Poppins","14","bold"),align="center")
            if self.vulture_count != 0:
                self.writer.write("Move Vulture",font=("Poppins","14","bold"),align="center")
        
    def undo_writer(self):
        self.writer.undo()
    
    def check_game_end(self):
        if self.check_crows_win() or self.check_vulture_win():
            self.game_ended = True
            return True
        return False

    def check_vulture_win(self):
        if(self.kill_count == 4):
            self.game_ended = True
            return True
        else:
            return False

    def check_crows_win(self):
        try:
            if self.curr_vulture_pos == -1:
                return False
            for list in self.neighbours[self.curr_vulture_pos]:
                if self.occupancy[list[0]] == 0:
                    return False
                if self.occupancy[list[1]] == 0 and self.occupancy[list[0]] == 2:
                    return False
            self.game_ended = True
            return True
        except:
            return False

    def can_jump(self, i, j):
        # print(i, " ", j)
        try:
            for list in self.neighbours[i]:
                if list[1] == j and self.occupancy[list[0]] == 2 and self.occupancy[j] == 0:
                    self.occupancy[list[0]] = 0
                    return True
            else:
                return False
        except:
            return False

    def is_adjacent(self, i, j):
        try:
            for list in self.neighbours[i]:
                if list[0] == j:
                    return True
            else:
                return False
        except:
            return False

game = Game()
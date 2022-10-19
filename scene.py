from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500


    canvas = start_drawing("Hammock Scene", scene_width, scene_height)


    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_pond(canvas, scene_width, scene_height)
    draw_hammock(canvas)
    draw_fence(canvas, scene_width, scene_height, 35)


    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
    draw_oval(canvas,650,400,700,450,fill= "yellow", outline= "")
    draw_oval(canvas,350,400,550,450,fill= "ghostwhite", outline= "")
    draw_oval(canvas,340,370,500,450,fill= "ghostwhite", outline= "")
    draw_oval(canvas,100,320,310,450,fill= "ghostwhite", outline= "")
    draw_oval(canvas,90,290,250,375,fill= "ghostwhite", outline= "")



def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green3")

    tree_center_x = 380
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)


def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 9
    trunk_height = height / 4
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height


    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="forestGreen")

def draw_pond(canvas):
    draw_oval(canvas, 450,50,640,150,fill= "teal", outline= "")
     
def draw_hammock(canvas):
    draw_arc(canvas,160,130,330,90, start=183, extent= 185, fill="orange", width = 20,outline= "orange")
    draw_line(canvas, 80,115,155,106)
    draw_line(canvas, 340,115,390,145)

def draw_fence(canvas,width, height, interval):
    draw_rectangle(canvas, 0, 30, width, 50, outline= "", fill="white")
    for x in range(0,width,interval):
        draw_rectangle(canvas, x+10, 0, x+30, 75, outline="", fill="white")
        draw_polygon(canvas, x+10, 0, x+30, 75, x+10, 100, outline="", fill="white")
        

main()
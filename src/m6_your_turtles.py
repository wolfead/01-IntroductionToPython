"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Alexander Wolfe.
"""
########################################################################
# done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
#######################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.tracer(2)
turtone = rg.SimpleTurtle()
turtone.pen = rg.Pen('red', 1)
turttwo = rg.SimpleTurtle()
turttwo.pen = rg.Pen('blue', 1)
turttwo.speed = 20
turtone.speed = 20
for k in range(20):
    turtone.draw_regular_polygon(5,30)
    turtone.pen_up()
    turtone.right(90)
    turtone.forward(5)
    turtone.left(90)
    turtone.pen_down()

for k in range(40):
    turttwo.draw_circle(150)
    turttwo.pen_up()
    turttwo.left(90)
    turttwo.forward(5)
    turttwo.right(90)
    turttwo.pen_down()
window.close_on_mouse_click()





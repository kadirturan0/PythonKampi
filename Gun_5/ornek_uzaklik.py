import math

# def uzaklik(x1,x2,y1,y2):
#
#     formul = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
#     print(formul)
#
# uzaklik()

# x1,x2,x3,x4


import math
def uzaklik2(*args):
   x1,x2,y1,y2 = args

   formul = math.sqrt((pow(x2-x1,2) + pow(y2-y1,2)))

   print(formul)

uzaklik2(3,6,3,6)
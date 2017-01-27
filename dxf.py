import ezdxf
from sys import argv

target = open("points.txt","w")

dwg = ezdxf.readfile("smile.dxf")
modelspace = dwg.modelspace()
for e in modelspace:
    print(e.dxftype())
    print("fir on layer: %s\n" % e.points())
    if e.dxftype() == 'POLYLINE':
        for p in e.points():
            x = ((p[0] / 5.0) * 7) - 3.5
            y = ((p[1] / 5.0) * 7) + 5
            target.write(str(x))
            target.write("\n")
            target.write(str(y))
            target.write("\n")
            print 'This is a tuple {0}'.format(p)

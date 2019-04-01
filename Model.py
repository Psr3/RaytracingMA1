import numpy as np
from Wall import *

class Model:

    def __init__(self,xmax,ymax):
        self.xmax=xmax
        self.ymax=ymax
        #self.matrice=np.zeros([xmax_m,ymax_m])

        self.walls = [0]

    def setwalls(self,xmax,ymax,cat):
        #cat est le type d'étage qu'on va utiliser
        if cat==1:
            self.walls=[0]*16
            #1) contour de la maison (en briques)
            self.walls[0]=Wall(0,xmax,0,0,1) #up
            self.walls[1]=Wall(0,xmax,ymax,ymax,1) #down
            self.walls[2]=Wall(0,0,0,ymax,1) #left
            self.walls[3]=Wall(xmax,xmax,0,ymax,1) #right

            #2) les murs en bétons
            self.walls[4]=Wall(174,174,0,124*0.5,2)
            self.walls[5]=Wall(174,174,207*0.5,457*0.5,2)
            self.walls[6]=Wall(174,174,540*0.5,749*0.5,2)
            self.walls[7]=Wall(299,299,0,124*0.5,2)
            self.walls[8]=Wall(299,299,207*0.5,540*0.5,2)
            self.walls[9]=Wall(299,299,623*0.5,431*0.5,2)
            self.walls[10]=Wall(0,224,831*0.5,831*0.5,2)
            #walls[11]=Wall(307,332,831,831,2)
            self.walls[11]=Wall(299,299,831*0.5,700*0.5,2)
            self.walls[12]=Wall(0,175,749*0.5,749*0.5,2)

            #3) les cloisons
            self.walls[13]=Wall(0,174,249*0.5,249*0.5,3)
            self.walls[14]=Wall(299,499,499*0.5,499*0.5,3)
            self.walls[15]=Wall(299,499,749*0.5,749*0.5,3)

        elif cat == 2:
            #ici on va créer un étage simple, avec uniquement 4 murs en brique
            self.walls= [0]*4
            self.walls[0]=Wall(0,xmax,0,0,1) #up
            self.walls[1]=Wall(0,xmax,ymax,ymax,1) #down
            self.walls[2]=Wall(0,0,0,ymax,1) #left
            self.walls[3]=Wall(xmax,xmax,0,ymax,1) #right

        elif cat == 3:
             #ici on va créer un mur infin en béton
            self.walls= [0]*5
            self.walls[0]=Wall(0,1,0,0,2) #up1
            self.walls[1]=Wall(xmax-1,xmax,0,0,2) #up2
            self.walls[2]=Wall(0,1,ymax,ymax,2) #down1
            self.walls[3]=Wall(xmax-1,xmax,ymax,ymax,2) #down2
            self.walls[4]=Wall(xmax/2,xmax/2,0,ymax,2) #down1
            


##    def setmatrice(self):
##     #ajout des walls à la matrice
##        for wall in self.walls:
##            self.matrice[wall.x1:wall.x2+1,wall.y1:wall.y2+1]=wall.mat
##
##    def getmatrice(self):
##        return self.matrice

    def getwalls(self):

        return self.walls

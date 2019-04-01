from fctsmath import *
import math as m
def reflexion(tx,rx,xmax,ymax,walls):
    """
    tx et rx sont des tuples contenant la position en x et en y de l'émetteur et du récepteur
    ATTENTION: les recherches des 4 murs ainsi que des pts images, et l'attribution des rayons sont toujours faits dans l'ordre suivant:
    RIGHT, UP, LEFT, DOWN
    """

    #1) trouver les 4 murs les plus proches dans les 4 directions
    for wall in walls:
##        minright=100000  #valeur très élevée pour que le premier élément de inter... soit d'office le premier min
##        minup=100000
##        minleft=100000
##        mindown=100000
        interright=[]
        interup=[]
        interleft=[]
        interdown=[]
        wallright=[]
        wallup=[]
        wallleft=[]
        walldown=[]
        imright=[]
        imup=[]
        imleft=[]
        imdown=[]
        if wall.x1>=tx[0] and wall.x1==wall.x2: #murs verticaux à droite de tx
            interright.append(line_intersection([tx,(wall.x1,tx[1])],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            wallright.append(wall)
            #calcule l'intersection entre une ligne horizontale partant de tx vers la droite, et le mur
            imright.append((2*wall.x1-tx[0],tx[1]))
##            if abs(interright[0]-tx[0])<minright: #cherche le mur qui a l'intersection la plus proche, cad la difference de x la plus faible
##                minright=abs(interright[0]-tx[0])
##                wallminright=wall



        elif wall.y1>=tx[1] and wall.y1==wall.y2: #murs horizontaux au-dessus de tx
            interrup.append(line_intersection([tx,(tx[0],wall.y1)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            wallup.append(wall)
            #calcule l'intersection entre une ligne verticale partant de tx vers le haut, et le mur
            imup.append((tx[0],2*wall.y1-tx[1]))
##
##            if abs(interrup[1]-tx[1])<minup:
##                minup=abs(interrup[1]-tx[1])
##                wallminup=wall

        elif wall.x1<=tx[0] and wall.x1==wall.x2: #murs verticaux à gauche de tx
            interleft.append(line_intersection([tx,(wall.x1,tx[1])],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            wallleft.append(wall)
            imleft.append((2*wall.x1-tx[0],tx[1]))

##            if abs(interleft[0]-tx[0])<minleft:
##                minleft=abs(interleft[0]-tx[0])
##                wallminleft=wall

        else: #murs horizontaux en-dessous de tx
            interdown.append(line_intersection([tx,(tx[0],wall.y1)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            walldown.append(wall)
            imdown.append((tx[0],2*wall.y1-tx[1]))

##            if abs(interdown[1]-tx[1])<mindown:
##                mindown=abs(interdown[1]-tx[1])
##                wallmindown=wall

##    reswall=[wallminright,wallminup,wallminleft,wallmindown]


    #2) trouver les points images: comprendre les distances à l'aide d'un dessin
##    im=[0]*4
##    im[0]=(2*reswall[0].x1-tx[0],tx[1])
##    im[1]=(tx[0],2*reswall[1].y1-tx[1])
##    im[2]=(2*reswall[2].x1-tx[0],tx[1])
##    im[3]=(tx[0],2*reswall[3].y1-tx[1])

    #3) pts d'intersection entre mur et droite ptimage-rx, et tracer les rayons
##    pt_inter=[]
    rays=[] #2 fois plus grande que pt_inter car 2 rayons par réflexion
##    j=0 #compteur pour les rayons
##    for i in range (0,4):
##        pt_inter[i]=line_intersection([im[i],rx],[(reswall[i].x1,reswall[i].y1),(reswall[i].x2,reswall[i].y2)])
##        rays[j]=[tx,pt_inter[i]] #un rayon=une ligne cad [tuple,tuple]
##        j=j+1
##        rays[j]=[pt_inter[i],rx]
##        j=j+1
    pt_inter_right=[]
    for i in range(0,length(wallright)):
        pt_inter_right.append(line_intersection([imright[i],rx],[(wallright[i].x1,wallright[i].y1),(wallright[i].x2,wallright[i].y2)]))
        #line1=[tx,pt_inter_right[i]]
        ray1=Ray(tx[0],tx[1],pt_inter_right[i][0],pt_inter_right[i][1],1) #rayon 1 entre tx et le pt d'intersection, coef est mis à 1
        #recherche des transmissions de ray1
        for wall in wallright: #juste sur les murs à droite de l'émetteur (logique)
            if line_intersection([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!="no_inter":
                theta_itr=m.pi/2-calcAngle([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]) #angle d'incidence de TRANSMISSION
                ray1.coef=ray1.coef*wall.get_coeff_trans(theta_itr)

        ray2=Ray(pt_inter_right[i][0],pt_inter_right[i][1],rx[0],rx[1],ray1.coef) #rayon 2 entre le pt d'intersection et rx
        #recherche des transmisssions de ray2
        for wall in walls:
            if line_intersection([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])!="no_inter":
                theta_itr=m.pi/2-calcAngle([(ray2.x1,ray2.y1),(ray2.x2,ray2.y2)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
                ray2.coef=ray2.coef*wall.get_coeff_trans(theta_itr)

        theta_i= m.pi/2 - calcAngle([(ray1.x1,ray1.y1),(ray1.x2,ray1.y2)], wallright[i]) #angle d'incidence de REFLEXION
        ray2.coef=ray2.coef*wallright[i].get_coeff_reflex(theta_i) #multiplication du coefficient de ray2
        rays.append(ray1)
        rays.append(ray2)

    pt_inter_up=[]
    i=0
    for i in range(0,length(wallup)):
        pt_inter_up.append(line_intersection([imup[i],rx],[(wallup[i].x1,wallup[i].y1),(wallup[i].x2,wallup[i].y2)]))

    pt_inter_left=[]
    i=0
    for i in range(0,length(wallleft)):
        pt_inter_left.append(line_intersection([imleft[i],rx],[(wallleft[i].x1,wallleft[i].y1),(wallleft[i].x2,walllef[i].y2)]))

    pt_inter_down=[]
    i=0
    for i in range(0,length(walldown)):
        pt_inter_down.append(line_intersection([imdown[i],rx],[(walldown[i].x1,walldown.y1),(walldown[i].x2,walldown[i].y2)]))


    #4) Reflexion double: A FAIRE

    #reflexions double pour tous les murs de droite (s'il y a transmission)
    #calcul des points images seconde Y'' en haut et en bas du mur considéré (ici le droit)
    #la première intuituion serait de chercher à éliminer certains murs: on pourrait chercher à savoir s'il existe des potentielles
    #réflexions dans les murs du haut/bas mais en fait l'ensemble des murs du haut/bas sont suceptible de créer des réflexions
    #on est donc obligé de faire tout les murs possibles
    #création de liste des images secondes, on a déjà celle des premières images
    imsecrightup = []
    imsecrightdown = []
    imsecleftup = []
    imsecleftdown = []
    imsecupright = []
    imsecupdown = []
    imsecdownright = []
    imsecdownleft = []

    #création de la liste des points de deuxième réflexion (le rayon part de l'emetteur touche une première fois le mur
    # est réfléchis, puis touche un second mur (c'est ce point qui sont dans ptreflex2) avant d'aller (c'est ce rayon qui est dans rayreflex2)
    # au recepteur) et des rayons attitrés
    ptreflex2 = []
    rayreflex2 = []
    #création de la liste des points de première réflexion et des rayons attitrés (même principe)
    ptreflex1 = []
    rayreflex1 = []
    #création de la liste des rayons allant du point de première réflexion à l'emetteur
    rayemett = []

    #attention imright doit etre modifié!!! i doit comprendre les points images de tout les murs pas seulement ceux qui possèdent un x
    #ou y égal à xT ou yT


    #afin de récupérer les murs de droite qui permetterons de calculer le point de première réflection il est nécessaire
    #d'ittérer sur des indices et non pas sur des objets, on sait que la liste des murs à droite de l'émetteur et
    #la liste des images à droites évoluent en parallèle onc pour chaque image de droite utilisé il y a le mur de droite correspondant,
    #ils sont au même indice

    ########################################################################################################################
    #Mur de droite

    for i in range(0,len(imright)) :
        im = imright[i]

        #Mur de droite partie haute
        ###############
        for wall in wallup :
            #calcul des points d'image seconde au dessus
            y*u* = (im[0],im[1] - 2 * wall.y1)
            imsecrightup.append(y*u*)

            tempwall = wallright[i]

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),y*u*],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
            p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

            #en effet, il se peut que le mur devant subir la seconde réflexion soit "trop court", et donc que le point p2 se retrouve
            #sur le mur de droite et pas celui du haut, ce qui aurait pour conséquence  que p1 == p2 il faut donc proscrire l'ensemble de
            #ces cas
            if p1 != p2 and p2 != None:
                ptreflex2.append(p2)
                r2 = [p2,(rx[0],rx[1]),1]
                rayreflex2.append(r2)

                #calcul de l'angle d'incidence de deuxième réflexion
                theta_i_2 = m.pi/2 - calcAngle([rx,p2],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

                ptreflex1.append(p1)
                r1 = [p1,p2,1]
                rayreflex1.append(r1)

                #calcul de l'angle d'incidence de première réflexion
                theta_i_1 = m.pi/2 - calcAngle([p2,p1],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

                #tracage des rayons allant de l'emetteur au premier point de réflexion
                r0 = [(tx[0],tx[1]),p1,1]
                rayemett.append(r0)

                #Calcul des coefficients de transmission des rayons emetteur-p1
                for wallbis in wallright:
                    if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != tempwall:
                        #2e cdt du if pour ne pas calculer un coeff de transmission sur le mur sur lequel on est réfléchi
                        theta_itr=m.pi/2-calcAngle([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                for wallbis in walls:
                    if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                        #les 2e et 3e cdts du if sont pour éviter de calculer une transmission sur les 2 murs gauche et haut sur lesquels il ya réflexion
                        theta_itr=m.pi/2-calcAngle([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                r1.coef=r1.coef*r0.coeff*get_coeff_reflex(theta_1)

                #Calcul des coefficients de transmission et réflexion des rayons p2-recepteur
                for wallbis in walls:
                    if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall:
                        #ici pas de 3e cdt car on est juste sur le mur du dessus
                        theta_itr=m.pi/2-calcAngle([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                r2.coef=r2.coef*r1.coeff*r0.coeff*get_coeff_reflex(theta_2)

        ###############
        #Mur de droite partie basse
        for wall in walldown :
            #calcul des points d'image seconde au dessous
            y*d* = (im[0],im[1] + 2 * wall.y1)
            imsecrightdown.append(y*d*)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),y*d*],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
            p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)]))

            if p1 != p2:
                ptreflex2.append(p2)
                r2 = [p2,(rx[0],rx[1]),1]
                rayreflex2.append(r2)

                tempwall = wallright[i]

                ptreflex1.append(p1)
                r1 = [p2,p1,1]
                rayreflex1.append(r1)

                #tracage des rayons allant de l'emetteur au premier point de réflexion
                r0 = [p1,(tx[0],tx[1]),1]
                rayemett.append(r0)

                #Calcul des coefficients de transmission des rayons emetteur-p1
                for wallbis in wallright:
                    if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter":
                        theta_itr=m.pi/2-calcAngle([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                for wallbis in walls:
                    if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter" and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                r1.coef=r1.coef*r0.coeff*get_coeff_reflex(theta_1)

                #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                for wallbis in walls:
                    if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter" and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                r2.coef=r2.coef*r1.coeff*r0.coeff*get_coeff_reflex(theta_2)


    ########################################################################################################################
    #Mur du bas
    for i in range(0,len(imdown)) :
        im = imdown[i]

        #####################
        #Mur du bas partie droite
        for wall in wallright :
            #calcul des points d'image seconde de droite
            y*r* = (im[0] + 2 * wall.x1 , im[1])
            imsecdownright.append(y*r*)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),y*r*],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
            p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

            if p1 != p2:
                ptreflex2.append(p2)
                r2 = [p2,(rx[0],rx[1]),1]
                rayreflex2.append(r2)

                #Il faut maintenant trouver le mur entre Y' et l'émetteur, il possède donc une abscisse de moitié entre Y' et T
                tempwall = walldown[i]

                ptreflex1.append(p1)
                r1 = [p2,p1,1]
                rayreflex1.append(r1)

                #tracage des rayons allant de l'emetteur au premier point de réflexion
                r0 = [p1,(tx[0],tx[1]),1]
                rayemett.append(r0)

                #Calcul des coefficients de transmission des rayons emetteur-p1
                for wallbis in wallright:
                    if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter":
                        theta_itr=m.pi/2-calcAngle([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                for wallbis in walls:
                    if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter" and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                r1.coef=r1.coef*r0.coeff*get_coeff_reflex(theta_1)

                #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                for wallbis in walls:
                    if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter" and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                r2.coef=r2.coef*r1.coeff*r0.coeff*get_coeff_reflex(theta_2)

        ############################
        #Mur du bas partie gauche
        for wall in wallleft :
            #calcul des points d'image seconde de gauche
            y*l* = (im[0],im[1] - 2 * wall.y1)
            imsecdownleft.append(y*l*)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),y*l*],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
            p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)]))

            if p1 != p2
                ptreflex2.append(p2)
                r2 = [p2,(rx[0],rx[1]),1]
                rayreflex2.append(r2)

                tempwall = walldown[i]

                ptreflex1.append(p1)
                r1 = [p2,p1,1]
                rayreflex1.append(r1)

                #tracage des rayons allant de l'emetteur au premier point de réflexion
                r0 = [p1,(tx[0],tx[1]),1]
                rayemett.append(r0)

                #Calcul des coefficients de transmission des rayons emetteur-p1
                for wallbis in wallright:
                    if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter":
                        theta_itr=m.pi/2-calcAngle([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                for wallbis in walls:
                    if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter" and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                r1.coef=r1.coef*r0.coeff*get_coeff_reflex(theta_1)

                #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                for wallbis in walls:
                    if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter" and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                r2.coef=r2.coef*r1.coeff*r0.coeff*get_coeff_reflex(theta_2)


    ########################################################################################################################
    #Mur de gauche

    for i in range(0,len(imleft)) :
        im = imleft[i]

        ####################
        #Mur de gauche partie haute
        for wall in wallup :
            #calcul des points d'image seconde au dessus
            y*u* = (im[0],im[1] - 2 * wall.y1)
            imsecleftup.append(y*u*)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),y*u*],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
            p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

            if p1 != p2
                ptreflex2.append(p2)
                r2 = [p2,(rx[0],rx[1]),1]
                rayreflex2.append(r2)

                #Il faut maintenant trouver le mur entre Y' et l'émetteur, il possède donc une abscisse de moitié entre Y' et T
                tempwall = wallleft[i]

                ptreflex1.append(p1)
                r1 = [p2,p1,1]
                rayreflex1.append(r1)

                #tracage des rayons allant de l'emetteur au premier point de réflexion
                r0 = [p1,(tx[0],tx[1]),1]
                rayemett.append(r0)

                #Calcul des coefficients de transmission des rayons emetteur-p1
                for wallbis in wallright:
                    if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter":
                        theta_itr=m.pi/2-calcAngle([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                for wallbis in walls:
                    if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter" and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                r1.coef=r1.coef*r0.coeff*get_coeff_reflex(theta_1)

                #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                for wallbis in walls:
                    if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter" and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                r2.coef=r2.coef*r1.coeff*r0.coeff*get_coeff_reflex(theta_2)

        ########################
        #Mur de gauche partie basse
        for wall in walldown :
            #calcul des points d'image seconde au dessous
            y*d* = (im[0],im[1] + 2 * wall.y1)
            imsecleftdown.append(y*d*)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_interse([(rx[0],rx[1]),y*d*],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
            p1 = segment_interse([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)]))

            if p1 != p2
                ptreflex2.append(p2)
                r2 = [p2,(rx[0],rx[1]),1]
                rayreflex2.append(r2)

                tempwall = wallleft[i]

                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_interse([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)]))
                ptreflex1.append(p1)
                r1 = [p2,p1,1]
                rayreflex1.append(r1)

                #tracage des rayons allant de l'emetteur au premier point de réflexion
                r0 = [p1,(tx[0],tx[1]),1]
                rayemett.append(r0)

                #Calcul des coefficients de transmission des rayons emetteur-p1
                for wallbis in wallright:
                    if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!="no_inter":
                        theta_itr=m.pi/2-calcAngle([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                for wallbis in walls:
                    if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                r1.coef=r1.coef*r0.coeff*get_coeff_reflex(theta_1)

                #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                for wallbis in walls:
                    if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                r2.coef=r2.coef*r1.coeff*r0.coeff*get_coeff_reflex(theta_2)


    ########################################################################################################################
    #Mur du haut
    for i in range(0,len(imup)) :
        im = imup[i]

        #Mur du bas partie droite
        for wall in wallright :
            #calcul des points d'image seconde de droite
            y*r* = (im[0] + 2 * wall.x1 , im[1])
            imsecdownright.append(y*r*)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),y*r*],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
            p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])

            if p2 != p1
                ptreflex2.append(p2)
                r2 = [p2,(rx[0],rx[1]),1]
                rayreflex2.append(r2)

                #Il faut maintenant trouver le mur entre Y' et l'émetteur, il possède donc une abscisse de moitié entre Y' et T
                tempwall = walldown[i]

                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)])
                ptreflex1.append(p1)
                r1 = [p2,p1,1]
                rayreflex1.append(r1)

                #tracage des rayons allant de l'emetteur au premier point de réflexion
                r0 = [p1,(tx[0],tx[1]),1]
                rayemett.append(r0)

                #Calcul des coefficients de transmission des rayons emetteur-p1
                for wallbis in wallright:
                    if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None:
                        theta_itr=m.pi/2-calcAngle([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                for wallbis in walls:
                    if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                r1.coef=r1.coef*r0.coeff*get_coeff_reflex(theta_1)

                #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                for wallbis in walls:
                    if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                r2.coef=r2.coef*r1.coeff*r0.coeff*get_coeff_reflex(theta_2)

        ################
        #Mur du bas partie gauche
        for wall in wallleft :
            #calcul des points d'image seconde de gauche
            y*l* = (im[0],im[1] - 2 * wall.y1)
            imsecdownleft.append(y*l*)

            #calcul des points de deuxième réflexion et des rayons liants le récepteur au point de seconde réflexion
            p2 = segment_intersec([(rx[0],rx[1]),y*l*],[(wall.x1,wall.y1),(wall.x2,wall.y2)])

            #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
            p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)]))

            if p1 != p2
                ptreflex2.append(p2)
                r2 = [p2,(rx[0],rx[1]),1]
                rayreflex2.append(r2)

                tempwall = walldown[i]

                #calcul des points de de première réflexion et des rayons liants les deux points de réflexion
                p1 = segment_intersec([p2,im],[(tempwall.x1,tempwall.y1),(tempwall.x2,tempwall.y2)]))
                ptreflex1.append(p1)
                r1 = [p2,p1,1]
                rayreflex1.append(r1)

                #tracage des rayons allant de l'emetteur au premier point de réflexion
                r0 = [p1,(tx[0],tx[1]),1]
                rayemett.append(r0)

                #Calcul des coefficients de transmission des rayons emetteur-p1
                for wallbis in wallright:
                    if segment_intersec([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None:
                        theta_itr=m.pi/2-calcAngle([(r0.x1,r0.y1),(r0.x2,r0.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r0.coef=r0.coef*wallbis.get_coeff_trans(theta_itr)

                #Calcul des coefficients de transmission et réflexion des rayons p1-p2
                for wallbis in walls:
                    if segment_intersec([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r1.x1,r1.y1),(r1.x2,r1.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r1.coef=r1.coef*wallbis.get_coeff_trans(theta_itr)

                r1.coef=r1.coef*r0.coeff*get_coeff_reflex(theta_1)

                #Calcul des coefficients de transmission et réflexion des rayons p2-recpteur
                for wallbis in walls:
                    if segment_intersec([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])!=None and wallbis != wall and wallbis != tempwall:
                        theta_itr=m.pi/2-calcAngle([(r2.x1,r2.y1),(r2.x2,r2.y2)],[(wallbis.x1,wallbis.y1),(wallbis.x2,wallbis.y2)])
                        r2.coef=r2.coef*wallbis.get_coeff_trans(theta_itr)

                r2.coef=r2.coef*r1.coeff*r0.coeff*get_coeff_reflex(theta_2)

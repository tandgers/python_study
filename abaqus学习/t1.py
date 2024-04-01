from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
import shutil
import os

import sys
from odbAccess import openOdb

for ODBname in os.listdir("D:/r0333338/Documents/MP/nodal_files_genereren/OBD"): # this is where all your ODB files are located #t hier wordt ook de odb file gekozen die geopend zal worden
    SUBname = ODBname[1:3]  # My subject ID is saved in the ODB name - this helps me create the file #woerdt er hier de 3e tot6e letter van de ODBname gepakt ?
    print 'Current File: '+ODBname #voor check welke file er gebruikt wordt #t (ZIT '.odb' hier bij in ?)
    ODBnamefull = 'D:/r0333338/Documents/MP/nodal_files_genereren/OBD/'+ODBname   # Full path to the ODB file, otherwise abaqus tries to find it in default work directory
    odb = openOdb(path=ODBnamefull)  #open the ODB file

    assembly = odb.rootAssembly     #t declareren van assembly?

    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
    numNodes = 0   #t num nodes op nul zetten 
    f = open("D:/r0333338/Documents/MP/nodal_files_genereren/ODBoutput/nodal.txt", "w") #indien het bestand al bestaat moet er "a" staan ipv "w"
    for name, instance in assembly.instances.items(): #t 'name' is naam van elke part van in de assembly ?
        n = len(instance.nodes) #t tellen van hoeveelheid nodes
        print 'Number of nodes of instance %s: %d' % (name, n) #moet niet in de file staan, kan eigenlijk weggelaten worden. (maar is een goede check?)
        numNodes = numNodes + n #tellen van totaal aantal nodes (globaal over alle parts) maar is eigenlijk niet nodig?
        f.write( "*Part, name=Part-1" + "\n")#moet erin staan volgens de MatchId regels
        f.write( "*Nodes" + "\n")            #moet erin staan volgens de MatchId regels

        if instance.embeddedSpace == THREE_D: #indien het 3D is
            print ' X Y Z' #moet niet in de file staan, maar is een goede check om te zien waar we zitten
            for node in instance.nodes:
                #print node #printen van node
                f.write( str(node.label) + ";" ) #schrijven van nodenummer
                f.write(str(node.coordinates[0]) + ";" + str(node.coordinates[1]) + ";" + str(node.coordinates[2]) + "\n") #schrijven van coordinaten [X;Y;Z] en enter
        else: #indien het 2D is
            print ' X Y' ';0' #moet niet in de file staan, maar is een goede check om te zien waar we zitten
            for node in instance.nodes:
                #print node #printen van node
                f.write( str(node.label) + ";" )
                f.write(str(node.coordinates[0]) + ";" + str(node.coordinates[1]) + ";" + str(node.coordinates[2]) + "\n") #schrijven van coordinaten [X;Y;Z] en enter
        f.write( "*End Part" ) #moet erin staan volgens de MatchId regels
    f.close()
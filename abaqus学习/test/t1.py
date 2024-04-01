# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-01.57.30 176069
# Run by tandgers on Wed Jun  7 23:17:35 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=358.0078125, 
    height=207.47395324707)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(pathName='C:/Temp/Abaqus/2023/0605-1.cae')
#: 模型数据库 "C:\Temp\Abaqus\2023\0605-1.cae" 已打开.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['0604-9'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(name='C:/Temp/0605-1.odb')
#: 模型: C:/Temp/0605-1.odb
#: 装配件个数:         1
#: 装配件实例个数: 0
#: 部件实例的个数:     3
#: 网格数:             3
#: 单元集合数:       24
#: 结点集合数:          22
#: 分析步的个数:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=572.583, 
    farPlane=887.557, width=271.707, height=158.252, viewOffsetX=9.78711, 
    viewOffsetY=-2.2442)
session.viewports['Viewport: 1'].view.setValues(nearPlane=570.946, 
    farPlane=889.195, width=270.93, height=157.799, viewOffsetX=14.1677, 
    viewOffsetY=-16.255)
session.viewports['Viewport: 1'].view.setValues(nearPlane=571.031, 
    farPlane=889.109, width=254.712, height=148.353, viewOffsetX=2.94296, 
    viewOffsetY=-14.5222)
session.viewports['Viewport: 1'].view.setValues(nearPlane=591.975, 
    farPlane=868.166, width=76.6038, height=44.6168, viewOffsetX=-9.83206, 
    viewOffsetY=-0.270951)
odb = session.odbs['C:/Temp/0605-1.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=ELEMENT_NODAL, 
    variable=(('E', INTEGRATION_POINT, ((INVARIANT, 'Max. Principal'), (
    INVARIANT, 'Max. Principal (Abs)'), (INVARIANT, 'Mid. Principal'), (
    INVARIANT, 'Min. Principal'), (COMPONENT, 'E11'), (COMPONENT, 'E22'), (
    COMPONENT, 'E33'), (COMPONENT, 'E12'), )), ), elementSets=(
    "CHENQI-ZUO-1.SET-3", ))
print(len(xyList))
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)

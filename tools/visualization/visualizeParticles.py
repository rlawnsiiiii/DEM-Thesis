# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *

# find source
source = GetActiveSource()

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=source,
    GlyphType='Sphere')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 1
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'Every Nth Point'
glyph1.Stride = 100

UpdatePipeline(time=0.0, proxy=glyph1)

renderView = GetActiveViewOrCreate('RenderView')
glyphDisplay = Show(glyph1, renderView, 'GeometryRepresentation')
renderView.Update()

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np

graph = vi.IPGraph("Graph3D-1")
a = graph.AddAnnotation("1")
d = a.SetDrawType(vi.PDrawItemType.DrawItem_Torus)
d.SetFillColor(0xFF00FF00)
d.SetCoordinates(170.0, 0.0, 0.0, 0);
d.SetCoordinates(50, 0.5, 0.2, 1);




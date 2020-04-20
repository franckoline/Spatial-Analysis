import utilities.gdal_workaround
import utilities.geopy_nominatim as geocode
import utilities.read_from_file_or_net as rfn
from shapely.geometry import shape, mapping, MultiPoint, LineString, Point, Polygon, MultiLineString, MultiPolygon
from shapely.ops import unary_union
import fiona
from fiona.crs import to_string, from_epsg
from collections import OrderedDict
import json
import pyproj
import os

# Downloading geojson files
def geoJson_Download_elements():
    print('url element File downloaded')
    
def geoJson_Download_string():
    print('string url File downloaded')
    
def single_plot():
    print('single polygon plot')
    
def compute_Centroid():
    print('Computing Centroid of polygon')
    
def compute_convexHull():
    print('Compute convex Hull of points')

def compute_centroidWithElement():
    print('Compute Centroids with predefined elements')

def compute_distanceBtw():
    print('Compute distance between points')
    
def joining_line():
    print('Computing Joining lines')
    
def geocode_elements():
    print('geocode elements')
    
def shapeFiles():
    print('Creating shape files')

# Graphical User Interface.
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import TclError
from tkinter import scrolledtext as st
from tkinter import Scrollbar as sb

class MyGUI:
    def __init__(self, my_parent):

        host_name = StringVar()
        layer_id = StringVar()
        srs_id = int()
        property_id = StringVar()
        geom_id = StringVar()
        fproperty_id = StringVar()
        fvalue_id1 = StringVar()
        fvalue_id2 = StringVar()

        PARAMS = {
            "host": host_name,
            "layer": layer_id,
            "srs_code": srs_id,
            "properties": [property_id],
            "geom_field": geom_id,
            "filter_property": fproperty_id,
            "filter_values": [fvalue_id1],
            "filter_values": [fvalue_id2]
        }
        self.my_parent = my_parent

        my_parent.title("GIS Programming - Supplement 2020 -- Name:")

        my_parent.protocol("WM_DELETE_WINDOW", self.catch_destroy)

         
        self.frame1 = ttk.Frame(my_parent, padding=5, border=1)
        self.frame1.grid(row=0, column=0 )
        self.tasks_frame = LabelFrame(self.frame1, padx=15, pady=15, text="Download GeoJson File with unit elements")
        self.tasks_frame.grid(row=0, column=0, sticky=NW)
        
        Label(self.tasks_frame, text="Hostname: ", justify=RIGHT).grid(row=1, column=0, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=host_name).grid(row=1, column=1, sticky=W)
        Label(self.tasks_frame, text="Layer:", justify=RIGHT).grid(row=2, column=0, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=layer_id).grid(row=2, column=1, sticky=W)
        Label(self.tasks_frame, text="Geometry field: ", justify=RIGHT).grid(row=3, column=0, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=geom_id).grid(row=3, column=1, sticky=W)
        Label(self.tasks_frame, text="Properties: ", justify=RIGHT).grid(row=1, column=3, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=property_id).grid(row=1, column=4, sticky=W)
        Label(self.tasks_frame, text="Source Code: ", justify=RIGHT).grid(row=2, column=3, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=srs_id).grid(row=2, column=4, sticky=W)
        Button(self.tasks_frame, width= 30, text="Download Geojson File >", command=geoJson_Download_elements) \
            .grid(row=3, column=4, sticky=NW, pady=5)

        self.tasks_frame = LabelFrame(self.frame1, padx=15, pady=15, text="Download GeoJson File using url string")
        self.tasks_frame.grid(row=3, column=0, sticky=NW)
        Label(self.tasks_frame, text="URL: ", justify=LEFT).grid(row=7, column=0, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=host_name).grid(row=7, column=1, sticky=W)
        Button(self.tasks_frame, width= 30, text="Download Geojson File >", command=geoJson_Download_string) \
            .grid(row=7, column=2, sticky=NW, pady=5)

        self.tasks_frame = LabelFrame(self.frame1, padx=1, pady=1, text="Plot graphs")
        self.tasks_frame.grid(row=9, column=0, sticky=NW)
        Button(self.tasks_frame, width= 30, text="Single Polygon >", command=single_plot) \
            .grid(row=10, column=1, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 30, text="Union Polygon Centroid >", command=compute_Centroid) \
            .grid(row=10, column=2, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 30, text="Convex Hull >", command=compute_convexHull) \
            .grid(row=10, column=3, sticky=NW, pady=5)

        self.tasks_frame = LabelFrame(self.frame1, padx=5, pady=5, text="Plot Centroid Using Element")
        self.tasks_frame.grid(row=11, column=0, sticky=NW)
        Label(self.tasks_frame, text="Name: ", justify=RIGHT).grid(row=12, column=2, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=fproperty_id).grid(row=12, column=3, sticky=W)
        Label(self.tasks_frame, text="Value A:  ",).grid(row=13, column=2, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=fvalue_id1).grid(row=13, column=3, sticky=W)
        Label(self.tasks_frame, text="Value B:  ", justify=RIGHT).grid(row=14, column=2, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=fvalue_id2).grid(row=14, column=3, sticky=W)
        Button(self.tasks_frame, width= 30, text="Centroid >", command=compute_centroidWithElement) \
            .grid(row=13, column=4, sticky=NW, pady=2)

        self.tasks_frame = LabelFrame(self.frame1, padx=10, pady=10, text="Other operations")
        self.tasks_frame.grid(row=16, column=0, sticky=NW)
        Button(self.tasks_frame, width= 20, text="Convex Hull >", command=compute_convexHull) \
            .grid(row=23, column=1, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 20, text="Distance btw Centroids >", command=compute_distanceBtw) \
            .grid(row=23, column=2, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 20, text="Joining Line >", command=joining_line) \
            .grid(row=23, column=3, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 20, text="Geocode Centroid >", command=geocode_elements) \
            .grid(row=23, column=4, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 20, text="Create Shapefiles >", command=shapeFiles) \
            .grid(row=23, column=5, sticky=NW, pady=5)

        self.log_frame = LabelFrame(self.frame1, padx=10, pady=10, text="Log Status")
        self.log_frame.grid(row=25, column=0, sticky=NW)
        self.log_text = st.ScrolledText(self.log_frame, width=100, height=5, wrap=WORD)
        self.log_text.grid(row=0, column=0)

    def catch_destroy(self):
        if messagebox.askokcancel("Quit", "Do you really want to terminate the processs"):
          self.my_parent.destroy()
    

def main_gui():
    root = Tk()
    MyGUI(root)
    root.mainloop()



if __name__=="__main__":
    main_gui()
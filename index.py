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

global host_name
global url2


#Global definitions
def get_stuff_from_geoserver(stuff):
    poly_search_attribute = "nuts3name"
    poly_search_value = "south-west"
    point_search_attribute = "population"
    point_search_value = 5000

    geo_files = {}
    for k,v in stuff.items():
        geo_files[k] = json.loads(rfn.get_stuff_from_net(v))

    # filtered_polys = [feature for feature in geo_files["counties_url"]["features"]
    #                   if poly_search_value in feature["properties"][poly_search_attribute].lower()]
    filtered_polys = []
    for feature in geo_files["counties_url"]["features"]:
        if poly_search_value in feature["properties"][poly_search_attribute].lower():
            filtered_polys.append(feature)

    filtered_points = [point for point in geo_files["geonames_url"]["features"]
                       if point["properties"][point_search_attribute] >= point_search_value]

    merged_polys = [shape(feature["geometry"]) for feature in filtered_polys]
    merged_poly = unary_union(merged_polys)

    # points_in_merged_poly = [point for point in filtered_points
    #                          if merged_poly.contains(shape(point["geometry"]))]
    points_in_merged_poly = []
    for point in filtered_points:
        if merged_poly.contains(shape(point["geometry"])):
            points_in_merged_poly.append(point)



# Downloading geojson files
    
def single_plot():
    print('single polygon plot')
    
def compute_convexHull():
    print('Compute convex Hull of points')

def compute_Centroid():
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
        self.my_parent = my_parent

        my_parent.title("GIS Programming - Supplement 2020 -- Name:")

        my_parent.protocol("WM_DELETE_WINDOW", self.catch_destroy)

        self.frame1 = ttk.Frame(my_parent, padding=5, border=1)
        self.frame1.grid(row=0, column=0 )

        # Download using urls elements
        def geoJson_Download_elements():
            try:
                host = hostName.get()
                selectLayer = layer.get()
                geometryField = geoField.get()
                property_id = props.get()
                source = sourceCode.get()

                self.log_text.insert(END, "Here are the inserted url element for your geoJson file: \n")
                self.log_text.insert(END, "-" * 30 + "\n")
                self.log_text.insert(END, "Host: " + host+"\n")
                self.log_text.insert(END, "Layer: " + selectLayer+"\n")
                self.log_text.insert(END, "Geometry Field: " + geometryField+"\n")
                self.log_text.insert(END, "Property: " + property_id+"\n")
                self.log_text.insert(END, "Source Code: " + source+"\n")


            except Exception as e:
                self.log_text.insert(END, "-" * 30 + "\n")
                self.log_text.insert(END, "There is an error string can not be downloaded due to the following error(s): {}\n".format(e))
                self.log_text.insert(END, "-" * 30 + "\n")
                return

        self.tasks_frame = LabelFrame(self.frame1, padx=15, pady=15, text="Download GeoJson File with unit elements")
        self.tasks_frame.grid(row=0, column=0, sticky=NW)

        hostName = ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="Hostname: ", justify=RIGHT).grid(row=1, column=0, sticky=W)
        hostName.grid(row=1, column=1, sticky=W)

        layer = ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="Layer:", justify=RIGHT).grid(row=2, column=0, sticky=W)
        layer.grid(row=2, column=1, sticky=W)

        geoField = ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="Geometry field: ", justify=RIGHT).grid(row=3, column=0, sticky=W)
        geoField.grid(row=3, column=1, sticky=W)

        props = ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="Properties: ", justify=RIGHT).grid(row=1, column=3, sticky=W)
        props.grid(row=1, column=4, sticky=W)

        sourceCode =ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="Source Code: ", justify=RIGHT).grid(row=2, column=3, sticky=W)
        sourceCode.grid(row=2, column=4, sticky=W)

        Button(self.tasks_frame, width= 30, text="Download Geojson File >", command=geoJson_Download_elements) \
            .grid(row=3, column=4, sticky=NW, pady=5)

        # Download using single url string
        def geoJson_Download_string():
            try:
                urls1 = url1.get()
                stuff = {}
                stuff["counties_url"] = urls1
                # stuff["counties_url"] = "http://193.1.33.31/geoserver/census2011/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=census2011%3Acounties&maxFeatures=50&outputFormat=application%2Fjson"
                stuff["geonames_url"] = url2.get()
                # stuff["geonames_url"] = "http://193.1.33.31/geoserver/TUDublin/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=TUDublin%3Ageonames_ie&outputFormat=application%2Fjson"
                get_stuff_from_geoserver(stuff)
                self.log_text.insert(END, "string url File download status link succecssful\n")
                self.log_text.insert(END, "-" * 30 + "\n")

            except Exception as e:
                self.log_text.insert(END, "-" * 30 + "\n")
                self.log_text.insert(END, "There is an error string can not be downloaded due to the following error(s): {}\n".format(e))
                self.log_text.insert(END, "-" * 30 + "\n")
                return

        self.tasks_frame = LabelFrame(self.frame1, padx=15, pady=15, text="Download GeoJson File using url string")
        self.tasks_frame.grid(row=3, column=0, sticky=NW)
        url1 = ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="counties URL: ", justify=LEFT).grid(row=7, column=0, sticky=W)
        url1.grid(row=7, column=1, sticky=W)

        url2 = ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="geonames URL: ", justify=LEFT).grid(row=7, column=2, sticky=W)
        url2.grid(row=7, column=3, sticky=W)
        Button(self.tasks_frame, width= 30, text="Download Geojson File >", command=geoJson_Download_string) \
            .grid(row=7, column=4, sticky=NW, pady=5)

        # Graph Ploting Block
        self.tasks_frame = LabelFrame(self.frame1, padx=1, pady=1, text="Plot graphs")
        self.tasks_frame.grid(row=9, column=0, sticky=NW)
        Button(self.tasks_frame, width= 30, text="Single Polygon >", command=single_plot) \
            .grid(row=10, column=1, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 30, text="Union Polygon Centroid >", command=compute_Centroid) \
            .grid(row=10, column=2, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 30, text="Convex Hull >", command=compute_convexHull) \
            .grid(row=10, column=3, sticky=NW, pady=5)

        # Centroid Computation Block
        def compute_centroidWithElement():
            try:
                fName = name.get()
                firstElement = aValue.get()
                secondElement = bValue.get()
                self.log_text.insert(END, "Here are the inserted filter element for Centroid: \n")
                self.log_text.insert(END, "-" * 30 + "\n")
                self.log_text.insert(END, "Filter Name: " + fName+"\n")
                self.log_text.insert(END, "Filter Value 1: " + firstElement+"\n")
                self.log_text.insert(END, "Filter Value 2: " + secondElement+"\n")

            except Exception as e:
                self.log_text.insert(END, "-" * 30 + "\n")
                self.log_text.insert(END, "There is an error string can not be downloaded due to the following error(s): {}\n".format(e))
                self.log_text.insert(END, "-" * 30 + "\n")
                return
            print('Computing Centroid of polygon')

        self.tasks_frame = LabelFrame(self.frame1, padx=5, pady=5, text="Plot Centroid Using Element")
        self.tasks_frame.grid(row=11, column=0, sticky=NW)

        name = ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="Name: ", justify=RIGHT).grid(row=12, column=2, sticky=W)
        name.grid(row=12, column=3, sticky=W)
        
        aValue = ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="Value A:  ",).grid(row=13, column=2, sticky=W)
        aValue.grid(row=13, column=3, sticky=W)
        
        bValue = ttk.Entry(self.tasks_frame, width=30)
        Label(self.tasks_frame, text="Value B:  ", justify=RIGHT).grid(row=14, column=2, sticky=W)
        bValue.grid(row=14, column=3, sticky=W)
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
    my_parent= Tk()
    MyGUI(my_parent)
    my_parent.mainloop()



if __name__=="__main__":
    main_gui()
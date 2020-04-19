from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import TclError
from tkinter import scrolledtext as st

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
            # "filter_values": [elf.fvalue_id1, self.fvalue_id2]
        }

        self.my_parent = my_parent

        self.my_parent.title("GIS Programming - Supplement 2019")

        my_parent.protocol("WM_DELETE", self.catch_destroy)

        self.frame1 = ttk.Frame(my_parent, padding=5, border=1)
        self.frame1.grid(row=0, column=0)
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
        Button(self.tasks_frame, width= 30, text="Download Geojson File >") \
            .grid(row=3, column=4, sticky=NW, pady=5)

        self.tasks_frame = LabelFrame(self.frame1, padx=15, pady=15, text="Download GeoJson File using url string")
        self.tasks_frame.grid(row=3, column=0, sticky=NW)
        Label(self.tasks_frame, text="URL: ", justify=LEFT).grid(row=7, column=0, sticky=W)
        Entry(self.tasks_frame, width=30, textvariable=host_name).grid(row=7, column=1, sticky=W)
        Button(self.tasks_frame, width= 30, text="Download Geojson File >") \
            .grid(row=7, column=2, sticky=NW, pady=5)

        self.tasks_frame = LabelFrame(self.frame1, padx=10, pady=1, text="Plot graphs")
        self.tasks_frame.grid(row=9, column=0, sticky=NW)
        Button(self.tasks_frame, width= 30, text="Single Polygon >") \
            .grid(row=11, column=1, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 30, text="Centroid >") \
            .grid(row=11, column=2, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 30, text="Convex Hull >") \
            .grid(row=11, column=3, sticky=NW, pady=5)

        # Label(self.tasks_frame, text="Name: ", justify=LEFT).grid(row=12, column=2, sticky=W)
        # Entry(self.tasks_frame, width=30, textvariable=fproperty_id).grid(row=12, column=3, sticky=W)
        # Label(self.tasks_frame, text="Value A:  ", justify=LEFT).grid(row=13, column=2, sticky=W)
        # Entry(self.tasks_frame, width=30, textvariable=fvalue_id1).grid(row=13, column=3, sticky=W)
        # Label(self.tasks_frame, text="Value B:  ", justify=LEFT).grid(row=14, column=2, sticky=W)
        # Entry(self.tasks_frame, width=30, textvariable=fvalue_id2).grid(row=14, column=3, sticky=W)
        # Button(self.tasks_frame, width= 30, text="Plot Centroid") \
        #     .grid(row=14, column=4, sticky=NW, pady=5)

        self.tasks_frame = LabelFrame(self.frame1, padx=10, pady=10, text="Other operations")
        self.tasks_frame.grid(row=16, column=0, sticky=NW)
        Button(self.tasks_frame, width= 20, text="Convex Hull >") \
            .grid(row=23, column=1, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 20, text="Distance btw Centroids >") \
            .grid(row=23, column=2, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 20, text="Joining Line >") \
            .grid(row=23, column=3, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 20, text="Geocode Centroid >") \
            .grid(row=23, column=4, sticky=NW, pady=5)
        Button(self.tasks_frame, width= 20, text="Create Shapefiles >") \
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
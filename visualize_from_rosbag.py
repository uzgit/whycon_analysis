#!/usr/bin/python3

import matplotlib.pyplot as plt

import sys
import numpy
import pandas

pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)

if( len(sys.argv) < 2 ):

    print("usage: ./visualize_from_rosbag.py <input.bag>")
    quit()

input_filename = sys.argv[1]
data = pandas.read_csv(input_filename)
data.rename(columns={"Unnamed: 0" : "time"}, inplace=True)

print(data.head(10))

print(data.columns)

orientation_x_figure = plt.figure().gca()
orientation_x_figure.plot(data["time"], data["/whycon/markers/markers/0/position/orientation/x"], label="x")
orientation_x_figure.set_title("Orientation (x)")
orientation_x_figure.legend()
#plt.savefig("orientation_x_figure.png", size=(4,7), bbox_inches="tight")

orientation_y_figure = plt.figure().gca()
orientation_y_figure.plot(data["time"], data["/whycon/markers/markers/0/position/orientation/y"], label="y")
orientation_y_figure.set_title("Orientation (y)")
orientation_y_figure.legend()
#plt.savefig("orientation_y_figure.png", size=(4,7), bbox_inches="tight")

orientation_z_figure = plt.figure().gca()
orientation_z_figure.plot(data["time"], data["/whycon/markers/markers/0/position/orientation/z"], label="z")
orientation_z_figure.set_title("Orientation (z)")
orientation_z_figure.legend()
#plt.savefig("orientation_z_figure.png", size=(4,7), bbox_inches="tight")

orientation_w_figure = plt.figure().gca()
orientation_w_figure.plot(data["time"], data["/whycon/markers/markers/0/position/orientation/w"], label="w")
orientation_w_figure.set_title("Orientation (w)")
orientation_w_figure.legend()
#plt.savefig("orientation_w_figure.png", size=(4,7), bbox_inches="tight")

transformed_x_figure = plt.figure().gca()
transformed_x_figure.plot(data["time"], data["/whycon/markers/markers/0/camera_translation/x"], label="x")
transformed_x_figure.set_title("Transformed Position (x)")
transformed_x_figure.legend()
#plt.savefig("transformed_x_figure.png", size=(4,7), bbox_inches="tight")

transformed_y_figure = plt.figure().gca()
transformed_y_figure.plot(data["time"], data["/whycon/markers/markers/0/camera_translation/y"], label="y")
transformed_y_figure.set_title("Transformed Position (y)")
transformed_y_figure.legend()
#plt.savefig("transformed_y_figure.png", size=(4,7), bbox_inches="tight")

transformed_z_figure = plt.figure().gca()
transformed_z_figure.plot(data["time"], data["/whycon/markers/markers/0/camera_translation/z"], label="z")
transformed_z_figure.set_title("Transformed Position (z)")
transformed_z_figure.legend()
#plt.savefig("transformed_x_figure.png", size=(4,7), bbox_inches="tight")

plt.show()
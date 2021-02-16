#!/usr/bin/python3

import matplotlib.pyplot as plt

import sys
import numpy
import pandas
pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)

if len(sys.argv) != 2:
    print("Usage: ./visualize_multiple.py <input csv file>")
    sys.exit()

# extract data
input_filename = sys.argv[1]
data = pandas.read_csv(input_filename)

# data.columns[0] = "time"
data.rename(columns={"Unnamed: 0" : "time"}, inplace=True)
print(data.columns)

print(data.head())

# start_time = data.iloc[0].time
# data["execution_time"] = data.time - start_time
#
# data["negative_straightened_position_x"] = - data.straightened_position_x
# data["negative_straightened_position_y"] = - data.straightened_position_y
# data["negative_straightened_position_z"] = - data.straightened_position_z
# #data = data.where(data.execution_time > 3)
# #data = data.where(data.execution_time < 5)
#
# print(data.head(10))
#
# # plot u
# u_figure = plt.figure().gca()
# u_figure.plot(data.execution_time, data.u, label="u")
# u_figure.set_ylim(0, 640)
# u_figure.set_title("Pixel Position (u)")
# u_figure.legend()
# plt.savefig("u_figure.png", size=(4,7), bbox_inches="tight")
#
# # plot v
# v_figure = plt.figure().gca()
# v_figure.plot(data.execution_time, data.v, label="v")
# v_figure.set_ylim(0, 480)
# v_figure.set_title("Pixel Position (v)")
# v_figure.legend()
# plt.savefig("v_figure.png", size=(4,7), bbox_inches="tight")
#
# # plot angle
# angle_figure = plt.figure().gca()
# angle_figure.plot(data.execution_time, data.angle, label="angle")
# angle_figure.set_ylim(-numpy.pi, numpy.pi)
# angle_figure.set_title("Angle")
# angle_figure.legend()
# plt.savefig("angle_figure.png", size=(4,7), bbox_inches="tight")
#
# id_figure = plt.figure().gca()
# id_figure.plot(data.execution_time, data.id, label="id")
# id_figure.set_ylim(0, 5)
# id_figure.set_title("ID")
# id_figure.legend()
# plt.savefig("id_figure.png", size=(4,7), bbox_inches="tight")
#
# x_figure = plt.figure().gca()
# x_figure.plot(data.execution_time, data.position_x, label="x")
# x_figure.set_title("Position (x)")
# x_figure.legend()
# plt.savefig("x_figure.png", size=(4,7), bbox_inches="tight")
#
# y_figure = plt.figure().gca()
# y_figure.plot(data.execution_time, data.position_y, label="y")
# y_figure.set_title("Position (y)")
# y_figure.legend()
# plt.savefig("y_figure.png", size=(4,7), bbox_inches="tight")
#
# z_figure = plt.figure().gca()
# z_figure.plot(data.execution_time, data.position_z, label="z")
# z_figure.set_title("Position (z)")
# z_figure.legend()
# plt.savefig("z_figure.png", size=(4,7), bbox_inches="tight")
#
# orientation_x_figure = plt.figure().gca()
# orientation_x_figure.plot(data.execution_time, data.orientation_x, label="x")
# orientation_x_figure.set_title("Orientation (x)")
# orientation_x_figure.legend()
# plt.savefig("orientation_x_figure.png", size=(4,7), bbox_inches="tight")
#
# orientation_y_figure = plt.figure().gca()
# orientation_y_figure.plot(data.execution_time, data.orientation_y, label="y")
# orientation_y_figure.set_title("Orientation(y)")
# orientation_y_figure.legend()
# plt.savefig("orientation_y_figure.png", size=(4,7), bbox_inches="tight")
#
# orientation_z_figure = plt.figure().gca()
# orientation_z_figure.plot(data.execution_time, data.orientation_z, label="z")
# orientation_z_figure.set_title("Orientation(z)")
# orientation_z_figure.legend()
# plt.savefig("orientation_z_figure.png", size=(4,7), bbox_inches="tight")
#
# orientation_w_figure = plt.figure().gca()
# orientation_w_figure.plot(data.execution_time, data.orientation_w, label="w")
# orientation_w_figure.set_title("Orientation (w)")
# orientation_w_figure.legend()
# plt.savefig("orientation_w_figure.png", size=(4,7), bbox_inches="tight")
#
# straightened_position_x_figure = plt.figure().gca()
# straightened_position_x_figure.plot(data.execution_time, data.straightened_position_x, label="x")
# straightened_position_x_figure.scatter(data.execution_time, data.negative_straightened_position_x, label="-x", color="red", marker=".", s=1)
# straightened_position_x_figure.set_title("Straightened Position (x)")
# straightened_position_x_figure.legend()
# plt.savefig("straightened_x_figure.png", size=(4,7), bbox_inches="tight")
#
# straightened_position_y_figure = plt.figure().gca()
# straightened_position_y_figure.plot(data.execution_time, data.straightened_position_y, label="y")
# straightened_position_y_figure.scatter(data.execution_time, data.negative_straightened_position_y, label="-y", color="red", marker=".", s=1)
# straightened_position_y_figure.set_title("Straightened Position (y)")
# straightened_position_y_figure.legend()
# plt.savefig("straightened_y_figure.png", size=(4,7), bbox_inches="tight")
#
# straightened_position_z_figure = plt.figure().gca()
# straightened_position_z_figure.plot(data.execution_time, data.straightened_position_z, label="z")
# straightened_position_z_figure.scatter(data.execution_time, data.negative_straightened_position_z, label="-z", color="red", marker=".", s=1)
# straightened_position_z_figure.set_title("Straightened Position (z)")
# straightened_position_z_figure.legend()
# plt.savefig("straightened_z_figure.png", size=(4,7), bbox_inches="tight")
#
# plt.show()
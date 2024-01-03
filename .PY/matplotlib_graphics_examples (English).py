# -*- coding: utf-8 -*-
"""Matplotlib graphics examples.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L0XSm7J7pFUxZ8s5PfnGSz_LvIDKeDpT
"""

import matplotlib.pyplot as plt  # imports the matplotlib library and names it as plt
x = [0, 1, 2, 3, 4]  # creates a list for x values
y = [2, 5, 8, 11, 14]  # creates a list for y values
plt.title('First Degree Function')  # names the graph title

plt.plot(x, y, label="Y(x)", linestyle='--', marker="s", color='purple')  # uses plt.plot to modify the graph contents, providing variables first, then the legend, changing the line style, marker, and finally the color

plt.xlabel("x")  # names the x-axis
plt.legend()  # configures to display the legend
plt.ylabel("y")  # names the y-axis

import matplotlib.pyplot as plt  # imports the matplotlib library and names it as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # creates a list for question 2 with 12 values
y = [25, 20, 12, 10, 15, 18, 12, 14, 14, 15, 25, 30]  # creates a list for question 4 with 12 values
plt.title('Yearly Sales (party articles)')  # names the graph title

plt.plot(x, y, label="Monthly Performance of Party Articles Sales (2023)", linestyle='-', marker="s", color='Red')  # uses plt.plot to modify the graph contents, providing variables first, then the legend, changing the line style, marker, and finally the color

plt.xlabel("Month")  # names the x-axis
plt.legend()  # configures to display the legend
plt.ylabel("Sales (Tens of units)")  # names the y-axis
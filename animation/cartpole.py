import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

ims = []

fig, ax = plt.subplots()

for i in range(100):
    ax.cla()
    y = 0.5
    theta = np.pi
    l = 0.5 + i*0.01
    cart_w = 0.5
    cart_h = 0.25
    bottom_h = 0.05
    ax.set_aspect('equal', adjustable='box')
    ax.plot([y, y+l*np.sin(theta)], [bottom_h+cart_h/2, bottom_h+cart_h/2-(l-bottom_h)*np.cos(theta)], color='#000000')
    cart = patches.Rectangle(xy=(y-cart_w/2, bottom_h), width=0.5, height=0.25, ec='#000000', fill=False)
    wheel_l = patches.Circle(xy=(y-cart_w/4, bottom_h), radius=bottom_h, fc='#000000', ec='#000000')
    wheel_r = patches.Circle(xy=(y+cart_w/4, bottom_h), radius=bottom_h, fc='#000000', ec='#000000')
    ball = patches.Circle(xy=(y+l*np.sin(theta), bottom_h+cart_h/2-l*np.cos(theta)), radius=bottom_h, fc='w', ec='#000000')
    ax.add_patch(cart)
    ax.add_patch(wheel_l)
    ax.add_patch(wheel_r)
    ax.add_patch(ball)
    ims.append(ax)

ani = animation.ArtistAnimation(fig, ims, interval=100)
plt.show()

# def plot():
#     ax.cla()
#     y = 0.5
#     theta = np.pi
#     l = 0.5
#     cart_w = 0.5
#     cart_h = 0.25
#     bottom_h = 0.05
#     ax.set_aspect('equal', adjustable='box')
#     ax.plot([y, y+l*np.sin(theta)], [bottom_h+cart_h/2, bottom_h+cart_h/2-(l-bottom_h)*np.cos(theta)], color='#000000')
#     cart = patches.Rectangle(xy=(y-cart_w/2, bottom_h), width=0.5, height=0.25, ec='#000000', fill=False)
#     wheel_l = patches.Circle(xy=(y-cart_w/4, bottom_h), radius=bottom_h, fc='#000000', ec='#000000')
#     wheel_r = patches.Circle(xy=(y+cart_w/4, bottom_h), radius=bottom_h, fc='#000000', ec='#000000')
#     ball = patches.Circle(xy=(y+l*np.sin(theta), bottom_h+cart_h/2-l*np.cos(theta)), radius=bottom_h, fc='w', ec='#000000')
#     ax.add_patch(cart)
#     ax.add_patch(wheel_l)
#     ax.add_patch(wheel_r)
#     ax.add_patch(ball)

# ani = animation.FuncAnimation(fig, plot, interval=100)
# plt.show()

# y = 0.5
# theta = np.pi
# l = 0.5
# cart_w = 0.5
# cart_h = 0.25
# bottom_h = 0.05
# ax.set_aspect('equal', adjustable='box')
# ax.plot([y, y+l*np.sin(theta)], [bottom_h+cart_h/2, bottom_h+cart_h/2-(l-bottom_h)*np.cos(theta)], color='#000000')
# cart = patches.Rectangle(xy=(y-cart_w/2, bottom_h), width=0.5, height=0.25, ec='#000000', fill=False)
# wheel_l = patches.Circle(xy=(y-cart_w/4, bottom_h), radius=bottom_h, fc='#000000', ec='#000000')
# wheel_r = patches.Circle(xy=(y+cart_w/4, bottom_h), radius=bottom_h, fc='#000000', ec='#000000')
# ball = patches.Circle(xy=(y+l*np.sin(theta), bottom_h+cart_h/2-l*np.cos(theta)), radius=bottom_h, fc='w', ec='#000000')
# ax.add_patch(cart)
# ax.add_patch(wheel_l)
# ax.add_patch(wheel_r)
# ax.add_patch(ball)
# plt.show()
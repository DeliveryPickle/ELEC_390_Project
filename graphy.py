import matplotlib.pyplot as plt
import pandas as pd

lucas_jump_arms_down = pd.read_csv("Lucas/JumpingArmsDown.csv")
lucas_walk_arms_up = pd.read_csv("Lucas/WalkingArmsUp.csv")
elise_jump_back_pocket = pd.read_csv("Elise/JumpingBackPocket.csv")
elise_jump_front_pocket = pd.read_csv("Elise/JumpingFrontPocket.csv")
simon_walk_coat_pocket = pd.read_csv("Simon/WalkingCoatPocket.csv")
simon_walk_front_pocket = pd.read_csv("Simon/WalkingFrontPocket.csv")

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
lucas_jump_arms_down.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False, title='Lucas Jumping Arms Down')

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
lucas_walk_arms_up.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False, title='Lucas Walking Arms Up')

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
elise_jump_back_pocket.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False, title='Elise Jumping Back Pocket')

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
elise_jump_front_pocket.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False, title='Elise Jumping Front Pocket')

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
simon_walk_coat_pocket.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False, title='Simon Walking Coat Pocket')

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
simon_walk_front_pocket.plot(x="Time (s)", ax=ax.flatten()[0:5], subplots=True, sharex=False, title='Simon Walking Front Pocket')

# this might be useless
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(lucas_jump_arms_down.iloc[:, 1], lucas_jump_arms_down.iloc[:, 2], lucas_jump_arms_down.iloc[:, 3])
ax.set_xlabel('Linear Acceleration x (m/s^2)')
ax.set_ylabel('Linear Acceleration y (m/s^2)')
ax.set_zlabel('Linear Acceleration z (m/s^2)')
ax.set_title('x vs y vs z (Jumping Arms Down)')
fig.tight_layout()
plt.show()

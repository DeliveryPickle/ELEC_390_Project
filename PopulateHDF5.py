
import h5py
import numpy as np

elise_walking_front_pocket = np.genfromtxt("Elise/WalkingFrontPocket.csv", delimiter=",", dtype=float, skip_header=1)
elise_walking_back_pocket = np.genfromtxt("Elise/WalkingBackPocket.csv", delimiter=",", dtype=float, skip_header=1)
elise_walking_coat_pocket = np.genfromtxt("Elise/WalkingCoatPocket.csv", delimiter=",", dtype=float, skip_header=1)
elise_walking_arms_up = np.genfromtxt("Elise/WalkingArmsUp.csv", delimiter=",", dtype=float, skip_header=1)
elise_walking_arms_down = np.genfromtxt("Elise/WalkingArmsDown.csv", delimiter=",", dtype=float, skip_header=1)
elise_jumping_front_pocket = np.genfromtxt("Elise/JumpingFrontPocket.csv", delimiter=",", dtype=float, skip_header=1)
elise_jumping_back_pocket = np.genfromtxt("Elise/JumpingBackPocket.csv", delimiter=",", dtype=float, skip_header=1)
elise_jumping_coat_pocket = np.genfromtxt("Elise/JumpingCoatPocket.csv", delimiter=",", dtype=float, skip_header=1)
elise_jumping_arms_up = np.genfromtxt("Elise/JumpingArmsUp.csv", delimiter=",", dtype=float, skip_header=1)
elise_jumping_arms_down = np.genfromtxt("Elise/JumpingArmsDown.csv", delimiter=",", dtype=float, skip_header=1)

simon_walking_front_pocket = np.genfromtxt("Simon/WalkingFrontPocket.csv", delimiter=",", dtype=float, skip_header=1)
simon_walking_back_pocket = np.genfromtxt("Simon/WalkingBackPocket.csv", delimiter=",", dtype=float, skip_header=1)
simon_walking_coat_pocket = np.genfromtxt("Simon/WalkingCoatPocket.csv", delimiter=",", dtype=float, skip_header=1)
simon_walking_arms_up = np.genfromtxt("Simon/WalkingArmsUp.csv", delimiter=",", dtype=float, skip_header=1)
simon_walking_arms_down = np.genfromtxt("Simon/WalkingArmsDown.csv", delimiter=",", dtype=float, skip_header=1)
simon_jumping_front_pocket = np.genfromtxt("Simon/JumpingFrontPocket.csv", delimiter=",", dtype=float, skip_header=1)
simon_jumping_back_pocket = np.genfromtxt("Simon/JumpingBackPocket.csv", delimiter=",", dtype=float, skip_header=1)
simon_jumping_coat_pocket = np.genfromtxt("Simon/JumpingCoatPocket.csv", delimiter=",", dtype=float, skip_header=1)
simon_jumping_arms_up = np.genfromtxt("Simon/JumpingArmsUp.csv", delimiter=",", dtype=float, skip_header=1)
simon_jumping_arms_down = np.genfromtxt("Simon/JumpingArmsDown.csv", delimiter=",", dtype=float, skip_header=1)

lucas_walking_front_pocket = np.genfromtxt("Lucas/WalkingFrontPocket.csv", delimiter=",", dtype=float, skip_header=1)
lucas_walking_back_pocket = np.genfromtxt("Lucas/WalkingBackPocket.csv", delimiter=",", dtype=float, skip_header=1)
lucas_walking_coat_pocket = np.genfromtxt("Lucas/WalkingCoatPocket.csv", delimiter=",", dtype=float, skip_header=1)
lucas_walking_arms_up = np.genfromtxt("Lucas/WalkingArmsUp.csv", delimiter=",", dtype=float, skip_header=1)
lucas_walking_arms_down = np.genfromtxt("Lucas/WalkingArmsDown.csv", delimiter=",", dtype=float, skip_header=1)
lucas_jumping_front_pocket = np.genfromtxt("Lucas/JumpingFrontPocket.csv", delimiter=",", dtype=float, skip_header=1)
lucas_jumping_back_pocket = np.genfromtxt("Lucas/JumpingBackPocket.csv", delimiter=",", dtype=float, skip_header=1)
lucas_jumping_coat_pocket = np.genfromtxt("Lucas/JumpingCoatPocket.csv", delimiter=",", dtype=float, skip_header=1)
lucas_jumping_arms_up = np.genfromtxt("Lucas/JumpingArmsUp.csv", delimiter=",", dtype=float, skip_header=1)
lucas_jumping_arms_down = np.genfromtxt("Lucas/JumpingArmsDown.csv", delimiter=",", dtype=float, skip_header=1)

with h5py.File('./ELEC390_Data.h5', 'a') as hdf:
    Elise = hdf.create_group('/Elise')
    Elise.create_dataset('WalkingFrontPocket', data=elise_walking_front_pocket)
    Elise.create_dataset('WalkingBackPocket', data=elise_walking_back_pocket)
    Elise.create_dataset('WalkingCoatPocket', data=elise_walking_coat_pocket)
    Elise.create_dataset('WalkingArmsUp', data=elise_walking_arms_up)
    Elise.create_dataset('WalkingArmsDown', data=elise_walking_arms_down)
    Elise.create_dataset('JumpingFrontPocket', data=elise_jumping_front_pocket)
    Elise.create_dataset('JumpingBackPocket', data=elise_jumping_back_pocket)
    Elise.create_dataset('JumpingCoatPocket', data=elise_jumping_coat_pocket)
    Elise.create_dataset('JumpingArmsUp', data=elise_jumping_arms_up)
    Elise.create_dataset('JumpingArmsDown', data=elise_jumping_arms_down)

    Simon = hdf.create_group('/Simon')
    Simon.create_dataset('WalkingFrontPocket', data=simon_walking_front_pocket)
    Simon.create_dataset('WalkingBackPocket', data=simon_walking_back_pocket)
    Simon.create_dataset('WalkingCoatPocket', data=simon_walking_coat_pocket)
    Simon.create_dataset('WalkingArmsUp', data=simon_walking_arms_up)
    Simon.create_dataset('WalkingArmsDown', data=simon_walking_arms_down)
    Simon.create_dataset('JumpingFrontPocket', data=simon_jumping_front_pocket)
    Simon.create_dataset('JumpingBackPocket', data=simon_jumping_back_pocket)
    Simon.create_dataset('JumpingCoatPocket', data=simon_jumping_coat_pocket)
    Simon.create_dataset('JumpingArmsUp', data=simon_jumping_arms_up)
    Simon.create_dataset('JumpingArmsDown', data=simon_jumping_arms_down)

    Lucas = hdf.create_group('/Lucas')
    Lucas.create_dataset('WalkingFrontPocket', data=lucas_walking_front_pocket)
    Lucas.create_dataset('WalkingBackPocket', data=lucas_walking_back_pocket)
    Lucas.create_dataset('WalkingCoatPocket', data=lucas_walking_coat_pocket)
    Lucas.create_dataset('WalkingArmsUp', data=lucas_walking_arms_up)
    Lucas.create_dataset('WalkingArmsDown', data=lucas_walking_arms_down)
    Lucas.create_dataset('JumpingFrontPocket', data=lucas_jumping_front_pocket)
    Lucas.create_dataset('JumpingBackPocket', data=lucas_jumping_back_pocket)
    Lucas.create_dataset('JumpingCoatPocket', data=lucas_walking_coat_pocket)
    Lucas.create_dataset('JumpingArmsUp', data=lucas_jumping_arms_up)
    Lucas.create_dataset('JumpingArmsDown', data=lucas_walking_arms_down)






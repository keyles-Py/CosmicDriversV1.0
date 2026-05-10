# Cosmic Drivers V1.0

This is a console-based game built with Python. It was developed to explore fundamental game design concepts, such as infinite loops, collision detection via conditional logic, and customizable gameplay and language settings. Both the player and the environment are rendered using ASCII characters: points are represented by the letter O, and enemies by the letter X.

The map is an array created using NumPy, where all elements (player, points, enemies) are placed randomly. Both the size of the map and the number of points spawned on it can be customized.

## Game Rules:
The map's size can range between a minimum of 4 rows by 11 columns and a maximum of 8 rows by 15 columns. These limits are set due to standard configurations. Using sizes outside of this range may cause issues during execution.
The number of points cannot exceed the total number of available spaces on the map (numRows * numColumns) for logical reasons.

## Notes:
- **Initial lag**: For some reason, there might be a slight lag when rendering the map the first time the code is executed.
- **Console "Skeleton"**: This console-based version is essentially the "skeleton" of another game I made, which includes a graphical interface, images, and sound. In this version, you can see the core game logic visualized purely in the terminal.

Enjoy playing and feel free to explore the code!

example of a match:

![Captura de pantalla mapa](https://github.com/user-attachments/assets/97e5c87f-f899-498e-b201-37173ebd7f75)


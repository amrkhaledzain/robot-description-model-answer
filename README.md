# model answer task 11
## robot description 

### how to run 

- clone this repo in your ws/src
- colcon build & source
- run this command
  ```text
  ros2 launch my_robot_description robot.launch.py 

  ```

---------------------------------------------------

## camera transform 

### Code Equations Explained

* **`x = xc * cos_t + zc * sin_t + tx`**  
  **Forward Distance:** Tilting the camera downward mixes the forward distance ($X$) with depth ($Z$). We use $\cos$ for the main forward component, $\sin$ for the tilt contribution, and add $t_x$ to offset the distance from the camera center to the robot center.

* **`y = yc + ty`**  
  **Sideways Distance:** Since the camera only pitches (rotates around the Y-axis), the sideways position is completely unaffected by rotation—we simply add the physical mounting offset $t_y$.

* **`z = -xc * sin_t + zc * cos_t + tz`**  
  **Height:** The pitch tilt causes forward distance to affect vertical height. We use $-\sin$ to compensate for the axis orientation during downward rotation, apply $\cos$ for the primary height component, and add the mounting height offset $t_z$.

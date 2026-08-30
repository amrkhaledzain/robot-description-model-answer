import math

# Input obstacle 3D points in camera optical frame: [x_c, y_c, z_c]
points = [[2.0, 0.0, -0.2], [3.5, 1.0, -0.3], [1.5, -0.8, -0.1]]

# Camera mounting offset vector (translation relative to body frame origin)
tx, ty, tz = 0.5, 0.0, 0.2

# Camera pitch tilt angle (around Y-axis) converted from degrees to radians
theta_deg = -15
theta_rad = math.radians(theta_deg)


cos_t = math.cos(theta_rad)
sin_t = math.sin(theta_rad)

transformed_points = []

for xc, yc, zc in points:
    # 3D Rigid Body Transformation: P_body = (R_y * P_camera) + T
    
    # 1. X-coordinate: rotated X and Z components + translation along X-axis
    # x = (x_c * cos(theta)) + (z_c * sin(theta)) + tx
    x = xc * cos_t + zc * sin_t + tx

    # 2. Y-coordinate: pitch rotation around Y-axis leaves y_c unchanged + translation along Y-axis
    # y = y_c + ty
    y = yc + ty

    # 3. Z-coordinate: rotated X and Z components + translation along Z-axis
    # z = (-x_c * sin(theta)) + (z_c * cos(theta)) + tz
    z = -xc * sin_t + zc * cos_t + tz

    transformed_points.append([round(x, 2), round(y, 2), round(z, 2)])

# Print resulting transformed points (x, y, z) to console
for i, pt in enumerate(transformed_points, 1):
    print(f"Point {i}: {pt}")
import math

def reward_function(params):

    # input parameters
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    is_left_of_center = params["is_left_of_center"]
    distance_from_center = params["distance_from_center"]
    all_wheels_on_track = params["all_wheels_on_track"]
    track_width = params["track_width"]
    steering_angle = params['steering_angle']
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    progress = params['progress']
    
    # initial reward
    reward = 1.0

    # calculate 5 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 10.0
    elif distance_from_center <= marker_2:
        reward = 5.0
    elif distance_from_center <= marker_3:
        reward = 1.0
    else:
        reward = 1e-3 # likely crashed/ close to off track

    # next and previous waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    
    # direction of center line in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # direction of center line in degrees
    track_direction = math.degrees(track_direction)

    # difference between heading and track angles
    direction_diff = track_direction - heading
    if abs(direction_diff) > 180:
        direction_diff = 360 - direction_diff

    # penalize if difference is too big
    if abs(direction_diff) > 10:
        reward *= 0.25
        # reward *= 0.5 * math.sqrt((180 - direction_diff)/180)

    # reward if steers right way:
    if track_direction >= 6 and steering_angle >= 6 and steering_angle <= 15:
        reward *= 2 
    elif track_direction <= -6 and steering_angle <= -6 and steering_angle >= -15:
        reward *= 2

    # penalize reward if the car is steering too much
    if track_direction < 4 and abs(steering_angle) > 4:
        reward *= 0.5

    # rewarding high speed at appropriate times
    if speed > 1.0 and track_direction <= 5:
        reward *= 2
    elif speed < 0.6 and track_direction > 5:
        reward += 5.0
    else:
        reward -= 2.0

    # simply off the track
    if is_offtrack:
        reward = 1e-3

    return float(reward)
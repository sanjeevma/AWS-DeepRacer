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
    abs_steering = abs(params['steering_angle'])
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    
    # initial reward
    reward = 1.0

    # calculate 5 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.3 * track_width
    marker_4 = 0.4 * track_width
    marker_5 = 0.5 * track_width

    # give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 5.0
    elif distance_from_center <= marker_2:
        reward = 4.0
    elif distance_from_center <= marker_3:
        reward = 2.0
    elif distance_from_center <= marker_4:
        reward = 1.0
    elif distance_from_center <= marker_5:
        reward = 0.1
    else:
        reward = 1e-3 # likely crashed/ close to off track

    # next and previous waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    
    # direction of center line in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # direction of center line in degrees
    track_direction = math.degrees(track_direction)

    # reward greater distance from center towards the turning direction while all wheels are on track
    if (track_direction - heading > 10):
        if (is_left_of_center and all_wheels_on_track):
            reward *= distance_from_center
    if (track_direction - heading < -10):
        if (not is_left_of_center and all_wheels_on_track):
            reward *= distance_from_center

    # difference between heading and track angles
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # penalize if difference is too big
    if direction_diff > 10:
        reward *= 0.5 * math.sqrt((180 - direction_diff)/180)

    # penalize reward if the car is steering too much
    if abs_steering > 15:
        reward *= 0.69

    # rewarding high speed at appropriate times
    if speed > 1.0 and abs_steering < 10:
        reward += 5.0
    elif speed > 0.8 and abs_steering < 20:
        reward += 4.0
    elif speed < 0.6 and abs_steering > 20:
        reward += 5.0
    else:
        reward -= 2.0

    # simply off the track
    if is_offtrack:
        reward = 1e-3

    return float(reward)

def reward_function(params):

    # input parameters
    # waypoints = params['waypoints']
    # closest_waypoints = params['closest_waypoints']
    # heading = params['heading']
    # is_left_of_center = params["is_left_of_center"]
    distance_from_center = params["distance_from_center"]
    # all_wheels_on_track = params["all_wheels_on_track"]
    track_width = params["track_width"]
    steering_angle = params['steering_angle']
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    progress = params['progress']
    
    # initial reward
    reward = 1.0

    # calculate 5 markers that are at varying distances away from the center line
    marker_1 = 0.25 * track_width
    marker_2 = 0.5 * track_width

    # give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 10.0
    elif distance_from_center <= marker_2:
        reward = 2.5
    else:
        reward = 1e-3 # likely crashed/ close to off track

    # # next and previous waypoints
    # next_point = waypoints[closest_waypoints[1]]
    # prev_point = waypoints[closest_waypoints[0]]
    
    # # direction of center line in radians
    # track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # # direction of center line in degrees
    # track_direction = math.degrees(track_direction)

    # # reward greater distance from center towards the turning direction while all wheels are on track
    # if (track_direction - heading > 10):
    #     if (is_left_of_center and all_wheels_on_track):
    #         reward *= distance_from_center
    # if (track_direction - heading < -10):
    #     if (not is_left_of_center and all_wheels_on_track):
    #         reward *= distance_from_center

    # # difference between heading and track angles
    # direction_diff = track_direction - heading
    # if abs(direction_diff) > 180:
    #     direction_diff = 360 - direction_diff

    # # penalize if difference is too big
    # if abs(direction_diff) > 10:
    #     reward *= 0.25
    #     # reward *= 0.5 * math.sqrt((180 - direction_diff)/180)

    # # reward if steers right way:
    # if track_direction > 10 and abs_steering:
    #     reward *= 2 

    # penalize reward if the car is steering too much
    if abs(steering_angle) > 15:
        reward *= 0.5

    # rewarding high speed at appropriate times
    if speed > 1.0:
        reward *= 2
    # elif speed > 0.8 and direction_diff < 20:
    #     reward += 4.0
    # elif speed < 0.6 and direction_diff > 20:
    #     reward += 5.0
    else:
        reward -= 2.0

    reward += progress * 10

    # simply off the track
    if is_offtrack:
        reward = 1e-3

    return float(reward)

def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3 # likely crashed/ close to off track

    return float(reward)

def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    
    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Always return a float value
    return float(reward)

def reward_function(params):
    # Example of penalize steering, which helps mitigate zig-zag behaviors

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15 
    
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
        
    return float(reward)

def reward_function(params):
    # Example of penalize steering, which helps mitigate zig-zag behaviors

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Calculate 3 marks that are farther and father away from the center line
    marker_0 = 0.05 * track_width
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_0:
        reward = 5.0
    elif distance_from_center <= marker_1:
        reward = 1.5
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
        
    if params['speed'] > 1.0:
        reward += 10.0
    elif params['speed'] > .9:
        reward += 5.0
    else:
        reward -= 1.0
    
    if params['is_offtrack']:
        reward = 1e-3
        
        
    return float(reward)

{
    "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
    "x": float,                            # agent's x-coordinate in meters
    "y": float,                            # agent's y-coordinate in meters
    "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
    "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
    "distance_from_center": float,         # distance in meters from the track center 
    "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
    "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": float,                      # agent's yaw in degrees
    "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
    "objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    "objects_location": [(float, float),], # list of object locations [(x,y), ...].
    "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
    "progress": float,                     # percentage of track completed
    "speed": float,                        # agent's speed in meters per second (m/s)
    "steering_angle": float,               # agent's steering angle in degrees
    "steps": int,                          # number steps completed
    "track_length": float,                 # track length in meters.
    "track_width": float,                  # width of the track
    "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center

}
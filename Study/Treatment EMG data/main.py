with open('raw_emg_data_unprocessed/index_finger_motion_raw.csv') as f_index, \
     open('raw_emg_data_unprocessed/little_finger_motion_raw.csv') as f_little, \
     open('raw_emg_data_unprocessed/middle_finger_motion_raw.csv') as f_middle, \
     open('raw_emg_data_unprocessed/rest_finger_motion_raw.csv') as f_rest, \
     open('raw_emg_data_unprocessed/ring_finger_motion_raw.csv') as f_ring, \
     open('raw_emg_data_unprocessed/thumb_motion_raw.csv') as f_thumb, \
     open('raw_emg_data_unprocessed/victory_gesture_motion_raw.csv') as f_victory:

    data_index, data_little, data_middle, data_rest, data_ring, data_thumb, data_victory = ([] for i in range(7))

    for line in f_index:
        data_index.append(list(map(float, line.strip().split(','))))

    for line in f_little:
        data_little.append(list(map(float, line.strip().split(','))))

    for line in f_middle:
        data_middle.append(list(map(float, line.strip().split(','))))

    for line in f_rest:
        data_rest.append(list(map(float, line.strip().split(','))))

    for line in f_ring:
        data_ring.append(list(map(float, line.strip().split(','))))

    for line in f_thumb:
        data_thumb.append(list(map(float, line.strip().split(','))))

    for line in f_victory:
        data_victory.append(list(map(float, line.strip().split(','))))

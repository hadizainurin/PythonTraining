import tensorflow as tf
import math

NUM_CLASSES = 10 # What is this?


def swish(x):
    return x * tf.nn.sigmoid(x)

def round_filters(filters, multiplier):
    depth_divisor = 8 # What is this?
    min_depth = None
    min_depth = min_depth or depth_divisor
    filters = filters * multiplier
    new_filters = max(min_depth, int(filters + depth_divisor / 2) // depth_divisor * depth_divisor)
    if new_filters < 0.9 * filters:
        new_filters += depth_divisor
    return int(new_filters)

def round_repeats(repeats, multiplier):
    if not multiplier:
        return repeats
    return int(math.ceil(multiplier * repeats))

class SEBlock(tf.keras.layers.Layer):
    def __init__(self, input_channels, ratio=0.25):
        return None
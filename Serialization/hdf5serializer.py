import h5py
import numpy as np
    
# # Creates a new dataset in the file test.hdf5 named "test_dataset" with a shape of (100,)
# # and a type of int32.
# with h5py.File("Serialization/test.hdf5", "w") as file: # "w" = write , "r" = read, "r+" = write/read
#     # dataset[0] to retrieve a specific index or dataset[:10] to get a slice from index 0 to index 10
#     print("test")
#     dataset = file.create_dataset("test_dataset", (100,), dtype="i")
#     # h5py datasets follow a Numpy syntax so that we can do slicing, retrieval, get shape, etc.,
#     # similar to Numpy arrays.


Read previously created HDF5 file
with h5py.File("test.hdf5", "r") as file:
    print(file.keys()) # get names of datasets that are in the file
    dataset = file["test_dataset"]
    print(dataset[:2])

# Organize HDF5 file
with h5py.File("Serialization/test.hdf5", "w") as file:
    # Create the groups on the path if they don't exist
    file.create_dataset("group1/dataset1", shape=(10,))
    # creates new group_1 in file
    file.create_group("group_1")
    group1 = file["group_1"]
    # creates dataset inside group1
    group1.create_dataset("dataset1", shape=(10,))
    # to access the dataset
    dataset = file["group_1"]["dataset1"]

# Read previously created HDF5 file
with h5py.File("test.hdf5", "r") as file:
    print(file.keys()) # get names of datasets that are in the file
    dataset = file["test_dataset"]
    print(dataset[:2])
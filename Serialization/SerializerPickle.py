import pickle

# Serialize dictionary and store the byte stream as a file
test_dict = {"Hello" : "World"}

with open("test.pickle", "wb") as outfile:
    # "wb" argument opens the file in binary mode
    pickle.dump(test_dict, outfile)
    # dump method to store byte stream as a file
print("Written object", test_dict)
# now test_dict is stored in the file "test.pickle"!

# Deserialization
# To recover the original object
with open("test.pickle", "rb") as infile:
    #load() method to read serialized byte stream from the file
    test_dict_reconstructed = pickle.load(infile)
print("Reconstructed objet", test_dict_reconstructed)

if test_dict == test_dict_reconstructed:
    print("Reconstruction success")
    
# Get object serialized as a bytes-array type in Python
test_dict_ba = pickle.dumps(test_dict)      # b'\x80\x04\x95\x15
print("Test1: ", test_dict_ba)
test_dict_reconstructed_ba = pickle.loads(test_dict_ba)
print("Test2: ", test_dict_reconstructed)
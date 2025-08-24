import pickle, Pick_Class   # Import pickle module and custom module PickClass

# Open the file 'Student.data' in binary read mode
with open("Student.data", mode="rb") as f:
    while True:   # Loop until end of file
        try:
            # Load one pickled object from the file
            obj = pickle.load(f)

            # Call disp() method of the object (defined inside PickClass)
            obj.disp()
        except EOFError:   # When end of file is reached
            print("DONE!!")
            break          # Exit the loop
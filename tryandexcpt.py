try:
    f = open("demofile.txt", "w")
    try:
        f.write("I have written it within the try block")
    except Exception as write_exception:
        print("Something went wrong while writing the file:", write_exception)
    finally:
        f.close()  # Close the file only if it was successfully opened
except Exception as open_exception:
    print("Something went wrong while opening the file:", open_exception)


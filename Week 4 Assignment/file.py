def read_and_write_file():
    try:
        # Ask user for input file
        input_filename = input("Enter the filename to read: ")
        
        # Read file content
        with open(input_filename, "r") as file:
            content = file.read()
        
        # Modify content (convert to uppercase)
        modified_content = content.upper()
        
        # Define output filename
        output_filename = "modified_" + input_filename
        
        # Write to new file
        with open(output_filename, "w") as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read or written.")

# Run the function
read_and_write_file()

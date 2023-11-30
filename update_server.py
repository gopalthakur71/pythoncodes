def update_server_config(file_path, key, value):
    # Read the existing content of the server configuration file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Update the configuration value for the specified key
    with open(file_path, 'a') as file:
        for line in lines:
            # Check if the line starts with the specified key
            if key in line:
                # Update the line with the new value
                file.write(key + "=" + value + "\n")
                print("File update successfully")
            else:
                # Keep the existing line as it is
                file.write(line)
                print("No change done")

# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'PORT'
new_value = '9000'  # New maximum connections allowed

# Update the server configuration file
update_server_config(server_config_file, key_to_update, new_value)

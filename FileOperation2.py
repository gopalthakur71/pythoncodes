def update_server_config(file_path, key, value):
    line = None
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, 'a') as file:
        updated = False
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
                updated = True
            else:
                file.write(line)

        if not updated:
            file.write(key + "=" + value + "\n")

update_server_config("server.conf", "MAX_CONNECTIONS", "8000")

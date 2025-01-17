def example_helper_function(data):
    """Process the input data and return the result."""
    # Implement your data processing logic here
    return data

def read_file(file_path):
    """Read the contents of a file and return it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """Write the given content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)
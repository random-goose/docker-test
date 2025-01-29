from autogen.coding import DockerCommandLineCodeExecutor, CodeBlock
import tempfile
import os

# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a Docker command line code executor.
executor = DockerCommandLineCodeExecutor(
    image="ubuntu:latest",  # You can use the official Ubuntu image
    timeout=100,
    work_dir=temp_dir.name,
)

# Define the Python code you want to run.
python_code = """
print("Hello World!")
x = 5
y = 10
print(f"The sum of x and y is: {x + y}")
"""

# Write the Python code to a file in the temporary directory.
python_file_path = os.path.join(temp_dir.name, "test_script.py")
with open(python_file_path, "w") as f:
    f.write(python_code)

# Install Python and run the Python file inside the container.
result = executor.execute_code_blocks(
    code_blocks=[
        # Install Python in the Ubuntu container (if not already installed)
        CodeBlock(language="bash", code="apt-get update && apt-get install -y python3"),
    ]
)

# Print the result (includes exit code and output).
print(result)
print()

# Install Python and run the Python file inside the container.
result = executor.execute_code_blocks(
    code_blocks=[
        # Install Python in the Ubuntu container (if not already installed)
        
        CodeBlock(language="bash", code="ls"),
    ]
)

# Print the result (includes exit code and output).
print(result)
print()

# Install Python and run the Python file inside the container.
result = executor.execute_code_blocks(
    code_blocks=[        
        # Run the Python script inside the container
        CodeBlock(language="bash", code=f"python3 test_script.py"),
    ]
)

# Print the result (includes exit code and output).
print(result)
print()

# Stop the executor.
executor.stop()

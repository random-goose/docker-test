from autogen.coding import DockerCommandLineCodeExecutor, CodeBlock
import tempfile

# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a Docker command line code executor.
executor = DockerCommandLineCodeExecutor(
    image="ubuntu:latest",  # You can use the official Ubuntu image
    timeout=100,
    work_dir=temp_dir.name,
)

# Install Python and run the Python file inside the container.
result = executor.execute_code_blocks(
    code_blocks=[
        # Install Python in the Ubuntu container (if not already installed)
        CodeBlock(language="bash", code="apt-get update && apt-get install -y python3 git"),
    ]
)

# Print the result (includes exit code and output).
print(result.output)
print()

# Install Python and run the Python file inside the container.
result = executor.execute_code_blocks(
    code_blocks=[
        # Install Python in the Ubuntu container (if not already installed)
        
        CodeBlock(language="bash", code="git init"),
        CodeBlock(language="bash", code="git clone https://github.com/random-goose/random-hello-world"),
    ]
)

# Print the result (includes exit code and output).
print(result.output)
print()

# Install Python and run the Python file inside the container.
result = executor.execute_code_blocks(
    code_blocks=[        
        # Run the Python script inside the container
        CodeBlock(language="bash", code=f"python3 random-hello-world/hi.py"),
    ]
)

# Print the result (includes exit code and output).
print(result.output)


# Stop the executor.
executor.stop()

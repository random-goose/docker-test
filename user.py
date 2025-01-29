from autogen.coding import DockerCommandLineCodeExecutor, CodeBlock
import tempfile

# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a Docker command line code executor.
executor = DockerCommandLineCodeExecutor(
    image="ubuntu:latest",  # The official Ubuntu image
    timeout=100,
    work_dir=temp_dir.name,
)

while True:

    user_in = input("")

    if user_in == "bruh":
        break

    result = executor.execute_code_blocks(
    code_blocks=[        
        CodeBlock(language="bash", code=user_in),
        ]
    )

    print(result.output)

print("closing")

# Stop the executor.
executor.stop()
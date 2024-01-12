import subprocess
import re

def run_command(command):
    """Run a system command and return its output."""
    return subprocess.check_output(command, shell=True, text=True)

def get_cpu_usage():
    """Returns the CPU usage percentage."""
    # Execute the `top` command with batch mode to get CPU usage
    output = run_command("top -bn1 | grep 'Cpu(s)'")
    # Parse the CPU usage from the output
    usage = re.findall(r'\d+\.\d+', output)
    return float(usage[0])  # Returns the user CPU usage percentage

def get_memory_usage():
    """Returns the memory usage percentage."""
    # Execute the `free` command to get memory usage
    output = run_command("free -m")
    # Parse the memory and free memory values
    lines = output.splitlines()
    mem_values = re.findall(r'\d+', lines[1])
    total_memory = int(mem_values[0])
    used_memory = int(mem_values[1])

    return (used_memory / total_memory) * 100  # Returns memory usage percentage

if __name__ == "__main__":
    # Test the functions
    print("CPU Usage: {:.2f}%".format(get_cpu_usage()))
    print("Memory Usage: {:.2f}%".format(get_memory_usage()))

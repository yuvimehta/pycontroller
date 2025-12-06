"""
Example usage of pycontroller package.
"""

from taskcontroller import task_controller, controller
import time


@task_controller
def example_task():
    """Example long-running task."""
    print("Starting example task...")
    
    for i in range(20):
        print(f"Processing step {i}/20")
        time.sleep(2)
    
    print("Task completed!")
    return "Success"


if __name__ == "__main__":
    print("=" * 60)
    print("PyController Example")
    print("=" * 60)
    print("\nTo control this task from another terminal, run:")
    print("\n  python -c \"from pycontroller import controller; controller.stop = True\"")
    print("  python -c \"from pycontroller import controller; controller.resume = True\"")
    print("  python -c \"from pycontroller import controller; controller.kill = True\"")
    print("\n" + "=" * 60 + "\n")
    
    result = example_task()
    print(f"\nResult: {result}")

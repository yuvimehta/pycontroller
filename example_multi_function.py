"""
Example usage of pycontroller with multiple functions.

This demonstrates how to control multiple decorated functions independently.
"""

from taskcontroller import task_controller, controller
import time


@task_controller
def task_a():
    """First long-running task."""
    print("[TASK A] Starting...")
    
    for i in range(30):
        print(f"[TASK A] Processing step {i}/30")
        time.sleep(1)
    
    print("[TASK A] Completed!")
    return "Task A Success"


@task_controller
def task_b():
    """Second long-running task."""
    print("[TASK B] Starting...")
    
    for i in range(30):
        print(f"[TASK B] Processing step {i}/30")
        time.sleep(1)
    
    print("[TASK B] Completed!")
    return "Task B Success"


@task_controller
def task_c():
    """Third long-running task."""
    print("[TASK C] Starting...")
    
    for i in range(30):
        print(f"[TASK C] Processing step {i}/30")
        time.sleep(1)
    
    print("[TASK C] Completed!")
    return "Task C Success"


def run_single_task(task_name):
    """Run a single task by name."""
    tasks = {
        'task_a': task_a,
        'task_b': task_b,
        'task_c': task_c
    }
    
    if task_name not in tasks:
        print(f"Unknown task: {task_name}")
        print(f"Available tasks: {list(tasks.keys())}")
        return
    
    print("=" * 60)
    print(f"Running {task_name}")
    print("=" * 60)
    print("\nControl this task from another terminal:")
    print(f"\n  # Pause {task_name}")
    print(f"  python -c \"from pycontroller import controller; controller.stop_function('{task_name}')\"")
    print(f"\n  # Resume {task_name}")
    print(f"  python -c \"from pycontroller import controller; controller.resume_function('{task_name}')\"")
    print(f"\n  # Kill {task_name}")
    print(f"  python -c \"from pycontroller import controller; controller.kill_function('{task_name}')\"")
    print(f"\n  # Check status")
    print(f"  python -c \"from pycontroller import controller; print(controller.status('{task_name}'))\"")
    print("\n" + "=" * 60 + "\n")
    
    result = tasks[task_name]()
    print(f"\nResult: {result}")


def run_all_tasks():
    """Run all tasks concurrently using threads."""
    import threading
    
    print("=" * 60)
    print("Running Multiple Tasks Concurrently")
    print("=" * 60)
    print("\nControl tasks from another terminal:")
    print("\n  # Pause specific task")
    print("  python -c \"from pycontroller import controller; controller.stop_function('task_a')\"")
    print("\n  # Resume specific task")
    print("  python -c \"from pycontroller import controller; controller.resume_function('task_a')\"")
    print("\n  # Pause ALL tasks")
    print("  python -c \"from pycontroller import controller; controller.stop_all()\"")
    print("\n  # Resume ALL tasks")
    print("  python -c \"from pycontroller import controller; controller.resume_all()\"")
    print("\n  # Kill specific task")
    print("  python -c \"from pycontroller import controller; controller.kill_function('task_b')\"")
    print("\n  # List all running functions")
    print("  python -c \"from pycontroller import controller; print(controller.list_functions())\"")
    print("\n  # Check status of all functions")
    print("  python -c \"from pycontroller import controller; import json; print(json.dumps(controller.status(), indent=2))\"")
    print("\n" + "=" * 60 + "\n")
    
    # Create threads for each task
    thread_a = threading.Thread(target=task_a, name="TaskA-Thread")
    thread_b = threading.Thread(target=task_b, name="TaskB-Thread")
    thread_c = threading.Thread(target=task_c, name="TaskC-Thread")
    
    # Start all threads
    thread_a.start()
    time.sleep(0.5)  # Stagger starts slightly
    thread_b.start()
    time.sleep(0.5)
    thread_c.start()
    
    # Wait for all threads to complete
    thread_a.join()
    thread_b.join()
    thread_c.join()
    
    print("\n" + "=" * 60)
    print("All tasks completed!")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "all":
            run_all_tasks()
        else:
            run_single_task(sys.argv[1])
    else:
        print("Usage:")
        print("  python example_multi_function.py task_a    # Run task_a only")
        print("  python example_multi_function.py task_b    # Run task_b only")
        print("  python example_multi_function.py task_c    # Run task_c only")
        print("  python example_multi_function.py all       # Run all tasks concurrently")
        print("\nExample:")
        print("  python example_multi_function.py all")

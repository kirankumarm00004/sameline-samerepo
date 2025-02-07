import gcpcloud
import time

def cpu_stress():
    while True:
        pass  # Keeps the CPU busy

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()  # Get the number of CPU cores
    print(f"Starting stress test on {num_cores} cores...")

    processes = []
    for _ in range(num_cores):  # Create a process for each core
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)

    try:
        time.sleep(90)  # Run the stress test for 60 seconds
    except KeyboardInterrupt:
        print("Stopping stress test...")

    for p in processes:
        p.terminate()  # Stop all processes

    print("Stress dev completed.")

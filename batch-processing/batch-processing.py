import csv
import concurrent.futures
import multiprocessing
import os
import time


# Sample processing function to simulate file processing
def process_file(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pass  # Simulate processing each row
    return f"{file_path} processed"


# Sequential processing
def process_sequential(files):
    results = []
    for file in files:
        result = process_file(file)
        results.append(result)
    return results


# Parallel processing
def process_parallel(files):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_file, file) for file in files]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results


# Batch processing
def process_batch(files, batch_size):
    results = []
    for i in range(0, len(files), batch_size):
        batch = files[i:i + batch_size]
        batch_results = process_parallel(batch)
        results.extend(batch_results)
    return results

# Parallel processing using multiprocessing
def process_multiprocessing(files):
    results = []
    with multiprocessing.Pool() as pool:
        results = pool.map(process_file, files)
    return results


# Main function to run the different processing methods
def main():
    # Create a list of dummy file paths (replace with actual file paths)
    files = ['employee.csv', 'sales.csv', 'student.csv', 'weather.csv', 'product.csv']

    # Sequential processing
    print("Sequential Processing:")
    start_time = time.time()
    sequential_results = process_sequential(files)
    print(f"Time taken: {time.time() - start_time} seconds")
    for result in sequential_results:
        print(result)

    # Parallel processing
    print("\nParallel Processing:")
    start_time = time.time()
    parallel_results = process_parallel(files)
    print(f"Time taken: {time.time() - start_time} seconds")
    for result in parallel_results:
        print(result)

    # Parallel processing using multiprocessing
    print("\nParallel Processing using Multiprocessing:")
    start_time = time.time()
    multiprocessing_results = process_multiprocessing(files)
    print(f"Time taken: {time.time() - start_time} seconds")
    for result in multiprocessing_results:
        print(result)

    # Batch processing
    print("\nBatch Processing:")
    batch_size = 5  # Example batch size
    start_time = time.time()
    batch_results = process_batch(files, batch_size)
    print(f"Time taken: {time.time() - start_time} seconds")
    for result in batch_results:
        print(result)


if __name__ == "__main__":
    main()

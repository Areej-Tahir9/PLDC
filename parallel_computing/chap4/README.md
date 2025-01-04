# **Chapter 4: Distributed Computing with MPI**

This directory contains Python scripts demonstrating various concepts in distributed computing using the Message Passing Interface (MPI) library. MPI is a standard for message-passing communication between multiple processes running on different computers or cores within a single machine.

## **Contents**

* **broadcast.py:**
    - Demonstrates the **broadcast** operation in MPI.
    - A single process (usually the "root" process) sends data to all other processes in the MPI communicator.
    - Example: Broadcasting an initial value or a set of parameters to all processes.

* **deadLockProblems.py:**
    - Illustrates common **deadlock scenarios** that can occur in MPI programs. 
    - Deadlock happens when two or more processes are waiting for each other to complete an action, resulting in none of them proceeding.
    - Shows examples of deadlock situations and discusses potential solutions, such as using locks or carefully ordering communication operations.

* **gather.py:**
    - Demonstrates the **gather** operation.
    - Each process sends data to a designated root process, which collects all the data from all processes.
    - Example: Collecting partial results from different processes to compute a global sum or average.

* **pointToPointCommunication.py:**
    - Shows examples of **point-to-point communication** between MPI processes.
    - Uses `send` and `receive` operations to exchange data between specific pairs of processes.
    - Demonstrates different communication patterns, such as one-to-one, many-to-one, and all-to-all.

* **scatter.py:**
    - Demonstrates the **scatter** operation.
    - A root process distributes data to all other processes.
    - Example: Distributing different portions of a dataset to different processes for parallel processing.

## **Getting Started**

1.  **Prerequisites:**
    *   **Python:** Ensure you have Python installed.
    *   **MPI:** Install the MPI library (e.g., Open MPI, MPICH) and its Python bindings (`mpi4py`). You can typically install `mpi4py` using `pip`:
        ```bash
        pip install mpi4py
        ```

2.  **Clone the repository:** If you haven't already, clone this repository to your local machine.

3.  **Run the scripts:** Execute the desired script using the `mpiexec` command (or a similar command for your MPI implementation):

    ```bash
    mpiexec -n <number_of_processes> python broadcast.py
    ```

    Replace `<number_of_processes>` with the desired number of MPI processes to run the script. For example, `mpiexec -n 4 python broadcast.py` will run the `broadcast.py` script with 4 MPI processes.

## **Usage**

Each script has its own specific functionality. Please refer to the individual script files for detailed usage instructions, examples, and comments within the code for better understanding.

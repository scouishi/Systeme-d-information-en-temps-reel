INTRODUCTION
This repository contains two types of simulations : C and Python. They're designed to profile, analyze, and schedule a set of real-time tasks. The project is turned on non-preemptive job scheduling. It combine C for accurate workload simulation (nearest to CPU) with  Python Earliest Deadline First algorithm, this environment show the CPU schedulability and how to optimize task execution to maximize processor idle time without missing any deadlines.

1. ARCHITECTURE
I made an hybrid project with C and python, I'm better working on python and implemented some C files for it's speed.
Here are the files you'll find in my repositorie :

- tache_1.c : It simulate an heavy CPU load with the multiplication of large arrays of random big numbers. It's in ;c becase C is the low-level language that is run directly on the OS, providing the fastest and more realistic execution time. It's only an executable called by another python file.

- boucle.py : It compile tache_1.c and execute it a large aount of time (1000 iterations) and it measure the execution time and calculate the World Case Execution Time (WCET). It returns the WCET.

- 


3. SCHEDULABILITY



5. ASSUMPTIONS



7. COMPLEXITY



9. RESPONSE TIMES



CONCLUSION

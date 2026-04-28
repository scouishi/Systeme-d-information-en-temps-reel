INTRODUCTION
This repository contains two types of simulations : C and Python. They're designed to profile, analyze, and schedule a set of real-time tasks. The project is turned on non-preemptive job scheduling. It combine C for accurate workload simulation (nearest to CPU) with  Python Earliest Deadline First algorithm, this environment show the CPU schedulability and how to optimize task execution to maximize processor idle time without missing any deadlines.

1. ARCHITECTURE
I made an hybrid project with C and python, I'm better working on python and implemented some C files for it's speed.
Here are the files you'll find in my repositorie :

- tache_1.c : It simulate an heavy CPU load with the multiplication of large arrays of random big numbers. It's in ;c becase C is the low-level language that is run directly on the OS, providing the fastest and more realistic execution time. It's only an executable called by another python file.

- boucle.py : It compile tache_1.c and execute it a large aount of time (1000 iterations) and it measure the execution time and calculate the World Case Execution Time (WCET). It returns the WCET.

- ordonnanceur.py : It calculate the CPU load, the Hyperperiod and genereate the list of jobs instances required during that period. It returns a list of 29 jobs instance with their data

-  algo.py : Implements the scheduling logic to ensure any deadlines aren't missed. It contains the strict mode and the "error" mode (with t5 which can be late). It returns the final execution trace and total accumulated waiting time (also compare the two modes)

To test the codes, you just need to run : python3 algo.py (ecerything is executed from there).


2. SCHEDULABILITY
Before scheduling, we need to prove that the processor is capable of handling the task set. The total CPU utilization (U) is the sum of the execution time to period ratios (C_i/T_i) for all tasks.

We use the WCET calculated in task_1.c (WCET = 0.903ms) 

U = 0.903/10 + 3/10 + 2/20 + 2/20 + 2/40 + 2/40 + 3/80
U = 0.7278
U = 72.78% < 100% So the task is schedulable.

3. ASSUMPTIONS
- The Hyperperiod: To guarantee the system will never miss a deadline indefinitely, we only need to simulate the schedule over one Hyperperiod. This is the Least Common Multiple (LCM) of all periods. LCM(10, 20, 40, 80) = 80 ms. The exact pattern of these 80 ms will repeat forever.

- Optimization Methods: We use a Greedy Earliest Deadline First (EDF) algorithm to optimise the approach (better than Branch and Bound). It selects the available job with the closest deadline, ensuring safety while maximizing idle time quickly.


4. COMPLEXITY
If we had kept the exhaustive tree-search approach to find the absolute perfect minimum waiting time, the algorithm would have to evaluate every permutation. fro N jobs the complexity fo 29 jobs would have been 29! = 8.8*10^30 (impossible for my computer)
Thats why using the Greedy EDF we reduce drasticly the complexity wich is now dropped to O(N^2*log(N)) wch ca be done in milliseconds (O(N) to filters the available jobs et O(N^2log(n) to sort them by deadlines)

5. SCHEDULABILITY ANALYSIS & RESPONSE TIMES
The system is verified by ensuring the Response Time (R = Finish_time - Arrival_time) is <= Deadline for every job.

With a total waiting time of 106.74 ms in strict mode, the execution trace confirms that:

- High-priority tasks (t1, t2) consistently meet their 10ms deadlines.
- Medium-priority tasks (t3, t4, t5, t6) are interleaved effectively.
- The low-priority task (t7) finishes well before its 80ms deadline.

The CPU successfully reaches idle states between job bursts, maximizing energy efficiency or background processing availability.

CONCLUSION
This project demonstrates that the task set is fully schedulable with a CPU load of 72.8%. By using a hybrid C/Python approach and a Greedy EDF algorithm, we avoided combinatorial explosion and produced an optimized non-preemptive schedule. The comparison between modes shows that a strict EDF policy provides the best overall waiting time (106.74 ms) for this specific workload.

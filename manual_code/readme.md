# Parallel vs Sequential Matrix Multiplication (C, fork())

## 📌 Overview

This project implements *square matrix multiplication (n × n)* in C using:

* ✅ Sequential execution (single process)
* ✅ Parallel execution using multiple child processes (fork())

The goal is to compare execution times and evaluate performance improvements when using process-based parallelism on multi-core systems.

The implementation uses the *naive O(n³) matrix multiplication algorithm* (no Strassen’s algorithm).

---

## 🚀 Features

* Dynamic allocation of large matrices (n ≥ 10,000 supported depending on RAM)
* Random matrix initialization using srand() and rand()
* Sequential multiplication
* Parallel row-wise multiplication using fork()
* Execution time measurement
* Performance comparison for different numbers of child processes
* Minimal virtual memory usage (dynamic allocation only)

---
---

## ⚙️ Compilation

Use GCC to compile:

bash
gcc matrix.c -o matrix


Run the program:

bash
./matrix


---

## ▶️ OUTPUT:



## 🧠 Implementation Details
* Time Complexity: *O(n³)*
* Matrix rows are evenly divided among children.
* Each child computes a subset of rows.
Parallelization Strategy: *Row-wise partitioning*

---

## 📊 Performance Testing

To test different numbers of processes, modify number of children.
Check available CPU cores:

bash
nproc


### Expected Behavior

| Processes   | Expected Result                   |
| ----------- | --------------------------------- |
| 1           | Same as sequential                |
| < CPU cores | Moderate speedup                  |
| = CPU cores | Best performance                  |
| > CPU cores | Overhead due to context switching |

---

## ⚠️ Limitations

* Uses naive O(n³) algorithm
* clock() measures CPU time, not true wall-clock time
* Large n values require high RAM
* Process creation overhead affects small matrix sizes

---

## 📈 Conclusion

This project demonstrates:

* Matrix multiplication is computationally intensive (O(n³)).
* Process-based parallelism significantly reduces execution time for large matrices.
* Optimal performance is achieved when the number of processes matches available CPU cores.
* Excessive processes may degrade performance due to context switching overhead.

The experiment highlights practical performance scaling using UNIX process parallelism.

---

## 👨‍💻 Author

1.Bharath Reddy.

2.Aman Das.

3.Samam Roy.

4. Saumya Kumari.
   
5.Rinika Banajree.

6.Pedelna Bhutia.

7.Sruthi Vaddadhi.

8.Anay Bhattacharya(group leader).

9.Dhrub Sah.



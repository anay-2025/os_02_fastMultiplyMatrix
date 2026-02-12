*import subprocess
import matplotlib.pyplot as plt

# Same input values used in C program
n_list = [1000, 2000, 3000]

# Same variable meaning as C code
st_list = []   # Sequential Time (st)
pt_list = []   # Parallel Time (pt)

for n in n_list:
    # Run compiled C program
    process = subprocess.Popen(
        ["./a.out"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    # Send n as input (same as scanf in C)
    output, _ = process.communicate(str(n))

    # Extract st and pt exactly like printed in C
    for line in output.splitlines():
        if "Sequential Time" in line:
            st = float(line.split("=")[1].replace("sec", "").strip())
            st_list.append(st)

        if "Parallel Time" in line:
            pt = float(line.split("=")[1].replace("sec", "").strip())
            pt_list.append(pt)

# Plot Sequential Time (st)
plt.figure()
plt.plot(n_list, st_list, marker='o')
plt.xlabel("Matrix Size n")
plt.ylabel("Time (seconds)")
plt.title("Sequential Matrix Multiplication Time (st)")
plt.show()

# Plot Parallel Time (pt)
plt.figure()
plt.plot(n_list, pt_list, marker='o')
plt.xlabel("Matrix Size n")
plt.ylabel("Time (seconds)")
plt.title("Parallel Matrix Multiplication Time (pt)")
plt.show()
*

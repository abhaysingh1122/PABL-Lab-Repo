"""Round Robin scheduling simulation.

Converted from the provided C implementation.
"""


def main() -> None:
    n = int(input("Enter number of processes: "))

    at = [0] * n  # Arrival times
    bt = [0] * n  # Burst times
    rt = [0] * n  # Remaining times
    ct = [0] * n  # Completion times
    wt = [0] * n  # Waiting times
    tat = [0] * n  # Turnaround times

    time = 0

    for i in range(n):
        at[i] = int(input(f"Enter Arrival Time of P{i + 1}: "))
        bt[i] = int(input(f"Enter Burst Time of P{i + 1}: "))
        rt[i] = bt[i]

    tq = int(input("Enter Time Quantum: "))

    remain = n

    while remain > 0:
        done = True

        for i in range(n):
            if at[i] <= time and rt[i] > 0:
                done = False

                if rt[i] > tq:
                    time += tq
                    rt[i] -= tq
                else:
                    time += rt[i]
                    ct[i] = time
                    rt[i] = 0
                    remain -= 1

        if done:
            time += 1

    print("\nProcess\tAT\tBT\tCT\tWT\tTAT")

    for i in range(n):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]
        print(f"P{i + 1}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{wt[i]}\t{tat[i]}")


if __name__ == "__main__":
    main()

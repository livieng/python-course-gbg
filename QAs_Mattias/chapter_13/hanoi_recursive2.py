from time import sleep, time


# Note: This is where recursion gets weird. The algorithm can be very difficult to fully grasp.
# I modified the other script just so that we can more easily view in which step we are.
def move(n, source, target, auxiliary):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        print("Before checkpoint 1: n =", n)
        sleep(sleeptime)
        move(n - 1, source, auxiliary, target)
        print("After checkpoint 1: n =", n)

        # Move the top disk from source to target
        target.append(source.pop())

        # Display our progress
        print(A, B, C)
        print("_" * 10)

        # Move the n - 1 disks that we left on auxiliary onto target
        print("Before checkpoint 2: n =", n)
        sleep(sleeptime)
        move(n - 1, auxiliary, target, source)
        print("After checkpoint 2: n =", n)


sleeptime = 1
n = 5
A = list(range(n, 0, -1))
B = []
C = []

print(A, B, C)
print("_" * 10)

# Initiate call from source A to target C with auxiliary B
start_time = time()
move(len(A), A, C, B)
end_time = time()
print("Elapsed time:", end_time-start_time)
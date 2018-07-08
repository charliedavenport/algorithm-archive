import math

# solves for dy/dx = (1-x)x, x0 = 0.1
# solution: y = 0.1 - (x^3)/3 + (x^2)/2
#
# this diff eq. is "stiff", meaning that forward euler will diverge, but backward euler will converge fine

def forward_euler(time_step, n):
    result = [0] * n
    result[0] = 1
    for i in range(1, n):
        result[i] = result[i-1] + time_step * result[i-1] * (1-result[i-1])
    return result

def backward_euler(time_step, n):
    result = [0] * n
    result[0] = 0.1
    for i in range(0, n-1):
        result[i + 1] = result[i]
        for _ in range(5):
            # Use 5 iterations of Newton's Method to approximate the zero
            result[i+1] = result[i+1] - (( result[i+1] - result[i] - time_step * result[i+1] * (1-result[i+1]) ) / (1 - time_step + 2*time_step*result[i+1]))
    return result 


def check(result, threshold, time_step):
    approx = True
    for i in range(len(result)):
        x = i * time_step
        solution = 0.1 - (x**3)/3 + (x**2)/2 
        if abs(result[i] - solution) > threshold:
            print(result[i], solution)
            approx = False
    return approx


def main():
    time_step = 0.01
    n = 100
    threshold = 0.1

    forward_result = forward_euler(time_step, n)
    backward_result = backward_euler(time_step, n)
    forward_approx = check(forward_result, threshold, time_step)
    backward_approx = check(backward_result, threshold, time_step)
    print("Forward Euler: All values within threshold") if forward_approx else print("Forward Euler: Value(s) not in threshold")
    print("Backward Euler: All values within threshold") if backward_approx else print("Backward Euler: Value(s) not in threshold")


main()
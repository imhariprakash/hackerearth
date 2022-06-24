def calculate_time(a, b):
    final = lcm(a, b)
    initial_a = a
    initial_b = b
    time = 1
    while((a + initial_a <= final) && (b + initial_b <= final)):
        time = time + 1
        a = a + initial_a
        b = b + initial_b
    while(a + initial_a <= final):
        time = time + 1
        a = a + initial_a
    while(b + initial_b <= final):
        time = time + 1
        b = b + initial_b
    return time

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a / gcd(a,b))* b
    
    
a, b = input().split()
out_ = calculate_time(a, b)
print(out_)
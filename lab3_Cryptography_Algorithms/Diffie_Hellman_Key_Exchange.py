def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)
    shared_key_a = pow(B, a, p)
    shared_key_b = pow(A, b, p)
    return shared_key_a, shared_key_b

# Example usage:
p = 23
g = 5
a = 6
b = 15

shared_key_a, shared_key_b = diffie_hellman(p, g, a, b)
print(f"Shared Key A: {shared_key_a}")
print(f"Shared Key B: {shared_key_b}")

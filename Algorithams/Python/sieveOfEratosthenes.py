#Sieve of Eratosthenes to print all prime numbers up to N

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    primes = [i for i in range(2, n+1) if is_prime[i]]
    return primes

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    primes = sieve_of_eratosthenes(N)
    print(f"Prime numbers up to {N} are: {primes}")

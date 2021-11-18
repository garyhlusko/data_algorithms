

# hashing alogirthm.
def polynomialRollingHash_upper(text,prime=104659,m = 1e9 + 9):
    text = text.upper()
    hash_value = 0
    prime_power = 1
    for i in range(len(text)):
        hash_value = (hash_value + (ord(text[i]) - ord('a') + 1) * prime_power) % m
        prime_power = (prime_power * prime) % m
    return int(hash_value)


print(polynomialRollingHash_upper("PittsburghPA15216"))
print(polynomialRollingHash_upper("PittsburghPA15216"))
print(polynomialRollingHash_upper("Gary Robert Hlusko"))
print(polynomialRollingHash_upper("geeksforgeeks"))
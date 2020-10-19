def prinme_gen():
    yield 1
    yield 2
    yield 3
    primes = [2, 3]
    number = 5
    while True:
        for item in primes:
            if item ** 2 <= number:
                if number % item == 0:
                    number += 2
                    break # for loop
            else:
                primes.append(number)
                yield number
                number += 2
                break


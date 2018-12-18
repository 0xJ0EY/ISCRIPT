
def fetch_count_test_cases():
    test_cases = int(input("Aantal test cases: "))

    while not (test_cases > 0 and test_cases <= 50):
        test_cases = int(input("Aantal test cases moeten <= 50 zijn: "))
    
    return test_cases

def fetch_test_case(number):
    test_case = int(input("Test case {}: ".format(number)))

    while not (test_case > 0 and test_case <= 100):
        test_case = int(input("De test case moet boven de 0 en onder de 100 zijn: "))

    return test_case

def fetch_test_cases(amount):
    test_cases = []

    for i in range(amount):
        test_cases.append(fetch_test_case(i + 1))

    return test_cases


def test_case_divisible_sum(test_case):
    ans = test_case
    
    while (True):
        sum = 0
        parts = list(str(ans))

        for part in parts:
            sum += int(part)

        if (ans % test_case == 0 and sum == test_case):
            return ans

        ans += test_case

def main():
    amount = fetch_count_test_cases()
    test_cases = fetch_test_cases(amount)

    for test_case in test_cases:
        print(test_case_divisible_sum(test_case))

if __name__ == '__main__':
    main()

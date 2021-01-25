# Functions for the program
def arithmetic(a, d, flag=0):
    n = int(input("Enter total no of terms: "))
    if flag == 0:
        if n <= 0:
            print(f"\n{n}th term of A.P does not exist.")
            print("\nSum of A.P = 0  (Since, no terms to compute sum)")
        elif n >= 1:
            tn = a + (n - 1) * d
            print(f"{n}th term of the A.P= {tn}\r")
            Sum = n * ((a + tn) / 2)
            print(f"Sum of A.P = {Sum}")
            # print(f"A.M = {Sum/n}")
    elif flag == 1:
        if n <= 0:
            print(f"\n{n}th term of H.P does not exist.")
            print("\nSum of H.P = 0  (Since, no terms to compute sum)")
        elif n >= 1:
            tn = a + (n - 1) * d
            print(f"{n}th term of the H.P= {1/tn}\r")
            Sum = n * ((a[0] + tn) / 2)
            print(f"Sum of H.P = {Sum}")
            # print(f"H.M = {Sum/n}")


def geometric(sequence):
    r = sequence[1] / sequence[0]
    n = int(input("Enter total no of terms: "))
    if n <= 0:
        print("\nSum of the sequence = 0 \t Since, there are no terms to compute sum. ")
        print(f"\n{n}th term of the G.P does not exist.")
    elif n >= 1:
        tn = sequence[0] * pow(r, n - 1)
        print(f"{n}th term of the G.P= {tn}\r")
        if r < 1:
            if n < 20:
                Sum = (sequence[0] * (1 - pow(r, n))) / (1 - r)
                print(f"Sum of G.P = {Sum}")
            elif n >= 20:
                Sum = sequence[0] / (1 - r)
                print(f"Sum of G.P = {Sum}")
        elif r > 1:
            if n <= 50:
                Sum = (sequence[0] * (1 - pow(r, n))) / (r - 1)
                print(f"Sum of G.P = {Sum}")
            else:
                print("Sum of G.P= Infinity")
        elif r == 1:
            Sum = n * sequence[0]
            print(f"Sum of G.P = {Sum}")
            exit()


def firstDifference(k, a, d):
    # where, k: first term of the entered series
    #        a: first term of the first difference series
    #        d: common difference of the first difference series
    n = int(input("Enter total no of terms: "))
    if n >= 1:
        tn = k + ((n - 1) * (2 * a + (n - 2) * d)) / 2
        Sum = n * k + ((n * (n - 1)) * (3 * a + (n - 2) * d) / 6)
        print(f"\n{n}th term of the sequence= {tn}")
        print(f"\nSum of the sequence= {Sum}")
    elif n <= 0:
        print("\nSum of the sequence = 0 \t Sine, there are no terms to compute sum. ")
        print(f"\n{n}th term of the sequence does not exist.")


def secondDifference(t0, a0, a, d):
    # where, k: first term of the entered series
    #        a: first term of the first difference series
    #        a0: first term of the second difference series
    #        d: common difference of the first difference series
    n = int(input("Enter total no of terms: "))
    if n >= 1:
        tn = t0 + (n - 1) * a0 + ((n - 1) * (n - 2) * (3 * a + (n - 3) * d)) / 6
        Sum = n * t0 + n * (n - 1) * a0 / 2 + ((n - 1) * (n - 2) * (n - 3)) * ((8 * a + n * d) / 24)
        print(f"\n{n}th term of the sequence= {tn}")
        print(f"\nSum of the sequence= {Sum}")
    elif n <= 0:
        print("\nSum of the sequence = 0 \t Sine, there are no terms to compute sum. ")
        print(f"\n{n}th term of the sequence does not exist.")


def sum_nSquares():
    n = int(input(print("Enter total no. of terms: ")))
    print(f"tn = {pow(n, 2)}")
    print(f"Sum = {(n * (n + 1) * (2 * n + 1)) / 6}")


def sum_nCube():
    n = int(input(print("Enter total no. of terms: ")))
    print(f"tn = {pow(n, 3)}")
    print(f"Sum= {pow((n * (n + 1)) / 6, 2)}")


def firstRatio(a, ro, r):
    return


def AGP(sequence, diff, r):
    n = int(input("Enter total no of terms: "))
    if n >= 1:
        tn = (sequence[0] + (n - 1) * diff) * pow(r, n-1)
        print(f"\n{n}th term of the sequence= {tn}")
        if r < 1:
            Sum = sequence[0]/(1 - r) + (diff * r(1 - pow(r, n-1)) / pow((1 - r), 2))
            print(f"\nSum of the sequence= {Sum}")
    elif n <= 0:
        print("\nSum of the sequence = 0 \t Sine, there are no terms to compute sum. ")
        print(f"\n{n}th term of the sequence does not exist.")


# Code Execution starts here
def main():
    # raw = input("1. AGP \n\t2. Other series\nEnter your option no.: ")
    # if raw == '1':
    terms = []
    difference = []
    ratio = []
    firstDiff = []
    secondDiff = []
    harmonicTerms = []
    harmonicDiff = []
    squareTerm = []
    # Fetching Input Sequence of numbers
    series = input(f"Enter six terms of your sequence: ")
    series = series.split(',')
    # Arithmetic Progression
    for count in range(6):
        terms.append(float(series[count]))
        if count >= 1:
            difference.append(terms[count] - terms[count - 1])

    if difference.count(difference[0]) == 5:
        print("The entered series is an arithmetic progression.\r")
        arithmetic(terms[0], difference[0])

    else:
        # Geometric Progression
        for count in range(1, 6):
            ratio.append(terms[count] / terms[count - 1])

        if ratio.count(ratio[0]) == 5:
            print("The entered series is a geometric progression.")
            geometric(terms)

        else:
            # Harmonic Progression
            for count in range(6):
                harmonicTerms.append(1 / terms[count])
                if count >= 1:
                    harmonicDiff.append(harmonicTerms[count] - harmonicTerms[count - 1])

            if harmonicDiff.count(harmonicDiff[0]) == 5:
                print("The entered series is a harmonic progression.")
                arithmetic(terms, 1)

            else:
                # First Difference in A.P
                for count in range(1, 5):
                    firstDiff.append(difference[count] - difference[count - 1])

                if firstDiff.count(firstDiff[0]) == 4:
                    print("The first difference of the entered series is in A.P.")
                    firstDifference(terms[0], difference[0], firstDiff[0])
                else:
                    # Second Difference in A.P
                    for count in range(1, 4):
                        secondDiff.append(firstDiff[count] - difference[count - 1])
                        if count >= 1:
                            difference.append(terms[count] - terms[count - 1])

                    if difference.count(difference[0]) == 3:
                        print("The second difference of the entered series is in A.P.")
                        secondDifference(terms, difference, firstDiff, secondDiff)
                    else:
                        # First ratio in G.P:-
                        for count in range(1, 6):
                            firstratio
                        if
                        else:
                            # Arithmetico Geometric Progression(A.G.P)
                            for count in range(1, 6):
                                print("I've failed")
                            if difference.count() == 5:
                                print("\nThe entered sequence is an Arithmetico Geometric Progression.")
                                AGP(terms, difference[0], ratio)

                            else:

                                print(f"\nSorry!!! your entered sequence does not match any of our series.")


main()
#BOJ_2447_gold5-별찍기 10

import sys
input =sys.stdin.readline


N = int(input())
for i in range(N):
    for j in range(N):
        if (i // 3**8) % 3 == 1 and (j // 3**8) % 3 == 1:
            print(' ', end='')
        else:
            if (i // 3**7) % 3 == 1 and (j // 3**7) % 3 == 1:
                print(' ', end='')
            else:
                if (i // 3 ** 6) % 3 == 1 and (j // 3 ** 6) % 3 == 1:
                    print(' ', end='')
                else:
                    if (i // 3 ** 5) % 3 == 1 and (j // 3 ** 5) % 3 == 1:
                        print(' ', end='')
                    else:
                        if (i // 3**4) % 3 == 1 and (j // 3**4) % 3 == 1:
                            print(' ', end='')
                        else:
                            if (i // 27) % 3 == 1 and (j // 27) % 3 == 1:
                                print(' ',end='')
                            else:
                                if (i // 9) % 3 == 1 and (j // 9) % 3 == 1:
                                    print(' ',end='')
                                else:
                                    if (i // 3) % 3 == 1 and (j // 3) % 3 == 1:
                                        print(' ',end='')
                                    else:
                                        if i % 3 == 1 and j % 3 == 1:
                                            print(' ',end='')
                                        else:
                                            print('*',end='')
    print()
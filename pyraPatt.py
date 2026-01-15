n = 10 # Number of rows
for i in range(n):
    # 1. Print Spaces: n - i - 1 spaces
    for j in range(n - i - 1):
        print(' ', end='')
    
    # 2. Print Stars: 2 * i + 1 stars
    for k in range(2 * i + 1):
        print('*', end='')
    
    print()
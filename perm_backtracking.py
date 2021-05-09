def backtrack(depth, max_level):
    global solution, appears ## in Python, global variables used inside a function definition should be mentioned beforehand.
    if depth <= max_level: ## if depth reaches max_level, we have generated a permutation.
        for i in range(1, max_level+1):
            if appears[i] == False: ## check for appearance in the additional vector
                appears[i] = True ## mark number i as used and add it to the solution
                solution[depth] = i

                backtrack(depth+1, max_level)

                appears[i] = False ## when coming back from recursion, unmark the number to add it later.
                solution[depth] = 0
    else:
        print(solution[1:]) ## as we are using indexes 1 through N

N = int(input("Give N: "))
solution = [0] * (N+1)
appears = [False] * (N+1)
backtrack(1, N)

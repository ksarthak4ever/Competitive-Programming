""" Assigning workers a pair of tasks and the time to perform each task should be minimum """

A = [6, 3, 2, 7, 5, 5] #i.e time to perform each task 


A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i]) #using ~ to access negative indeces
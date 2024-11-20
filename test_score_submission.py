def can_achieve_marks(total_problems, marks_per_problem, target_marks):
    max_marks = total_problems * marks_per_problem
    min_marks = 0
    return "YES" if min_marks <= target_marks <= max_marks and target_marks % marks_per_problem == 0 else "NO"
N, X, Y = map(int, input().split())
print(can_achieve_marks(N, X, Y))

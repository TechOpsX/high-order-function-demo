# demo
def sort_abs(nums):
    return sorted(nums, key=abs)


def reverse_letter(letters):
    return sorted(letters, key=str.lower, reverse=True)


# test, sorted by score
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[-1]


def sort_student():
    return sorted(L, key=by_score)


if __name__ == "__main__":
    print(sort_abs([36, 5, -12, 9, -21]))
    print(reverse_letter(['bob', 'about', 'Zoo', 'Credit']))
    print(sort_student())

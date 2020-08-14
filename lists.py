# def sum_all(t):
#     #t is a list of numbers
#     total = 0
#     for x in t:
#         total += x
#     return total

# def cumulative_sum(t):
#     cumulative_total = 0
#     cumulative_sum = []
#     for x in t:
#         cumulative_total += x
#         cumulative_sum.append(cumulative_total)
#     return cumulative_sum


# t = [10,20,30]
# print(cumulative_sum(t))
#10,30,60

def report_card():
    num_classes = int(input("How many classes did you take? "))
    classes = []
    grades = []

    for x in range(num_classes):
        class_name = input("what is the name of this class? ")
        classes.append(class_name)
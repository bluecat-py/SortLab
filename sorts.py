def bubble_sort(numbers):
    steps = []
    for i in range(1, len(numbers)):
        for n in range(0, len(numbers)-i):

            steps.append({
                    "array": numbers[:],
                    "compare": numbers[n:n+2],
                    "swap": None
            })

            if numbers[n] > numbers[n+1]:
                steps[n]["swap"] = True
                numbers[n], numbers[n+1] = numbers[n+1], numbers[n]
            else:
                steps[n]["swap"] = False
            steps.append(numbers[:])
    return steps
            
def selection_sort(numbers):
    steps = [numbers[:]]
    for min in range(0, len(numbers)-1):
        currentMin = min
        for i in range(min +1, len(numbers)):
            if numbers[i] < numbers[currentMin]:
                currentMin = i
        numbers[min], numbers[currentMin] = numbers[currentMin], numbers[min]
        steps.append(numbers[:])
    return steps

def insertion_sort(numbers):
    steps = [numbers[:]]
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j-1] > numbers[j]:
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
            j = j -1
            steps.append(numbers[:])
    return steps


lst = [4, 7, 2, 5, 3, 1, 6]
print(bubble_sort(lst))
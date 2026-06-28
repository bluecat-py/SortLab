def bubble_sort(numbers):
    bubbled: list[int] = []
    for i in range(1, len(numbers)):
        for n in range(0, len(numbers)-i):
            if numbers[n] > numbers[n+1]:
                yield{
                    "array": numbers,
                    "compare": [n, n+1],
                    "swap": False,
                    "color": "red",
                    "bubbled": bubbled[:]
                }
                numbers[n], numbers[n+1] = numbers[n+1], numbers[n]
                yield{
                    "array": numbers,
                    "compare": [n, n+1],
                    "swap": True,
                    "color": "cyan",
                    "bubbled": bubbled[:]
                }
            else:     
                yield{
                    "array": numbers,
                    "compare": [n, n+1],
                    "swap": False,    
                    "color": "cyan", #I don't actually need this
                    "bubbled": bubbled[:]
                }
        bubbled.append(len(numbers) -i)
    yield{
        "array": numbers,
        "compare": [],
        "swap": None,
        "color": None,
        "bubbled": list(range(len(numbers)))
    }



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


lst = [4, 5, 2, 1, 7, 3, 6]


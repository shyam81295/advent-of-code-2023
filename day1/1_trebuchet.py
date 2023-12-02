def trebuchet(words):
    sum = 0
    for word in words:
        num = form_two_digit_num(word)
        sum += num
    return sum

def read_file(filename):
    import os
    f = open(filename, "r")
    lines = f.readlines()
    words = []
    for line in lines:
        words.append(line.strip('\n'))
    return words
    
def form_two_digit_num(word):
    first_num = second_num = 0
    for char in word:
        if char.isnumeric():
            first_num = int(char)
            break
    for char in word[::-1]:
        if char.isnumeric():
            second_num = int(char)
            break
    return (first_num * 10) + second_num

if __name__ == "__main__":
    words = read_file("input1.txt")
    sum = trebuchet(words)
    print(sum)

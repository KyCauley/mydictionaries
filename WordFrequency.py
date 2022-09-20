infile = open('sometext.txt','r')
frequency = {}

for line in infile:
    line = line.strip()
    line = line.lower()
    words = line.split(' ')

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

print(frequency)
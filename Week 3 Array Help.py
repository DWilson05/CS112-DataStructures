import array

arrayExample = array.array('f', [1.2, 2.4, 5.6])
print(arrayExample)
print(arrayExample[2])

arrayExample[1] += 3
print(arrayExample[1])

for m in arrayExample:
    print(m)

print(len(arrayExample))
arrayExample.append(5.7)
print(len(arrayExample))

arrayExample.insert(2, 2.9)

# .remove removes first instance of value if value not in array prog crashes
# .count checks how many times value appears in array
# .pop removes variable and you can assign it somewhere x = arrayExample.pop()
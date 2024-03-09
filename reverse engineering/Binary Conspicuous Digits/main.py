encoded_flag = ''

with open('output.txt', 'r') as file:
    encoded_flag = file.read()

decoded = ''
for i in range(0, len(encoded_flag), 4):
    chunk = encoded_flag[i:i+4]
    decoded += chr(int(chunk, 2))

print(decoded)

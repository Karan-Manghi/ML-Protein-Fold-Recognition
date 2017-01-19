file1 = set(line.strip() for line in open('1.txt'))
file2 = set(line.strip() for line in open('2.txt'))

with open('results.txt', 'w') as file_out:
    for line in file1 & file2:
          file_out.write(line)
          file_out.write("\n")
          
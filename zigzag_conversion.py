s="PAYPALISHIRING"
numRows=4

for row in range(numRows):
    i,counter = 0, row
    if row == numRows -1:
        row = 0
    while counter < len(s):
        print(s[counter])
        counter += 2*(numRows)-2*(row+1)

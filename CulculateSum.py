import re
text = open('regex_sum_4596.txt')
total = 0
for line in text:
    line = line.strip()
    nums = re.findall('[0-9]+',line)
    if len(nums) < 1 : continue
    for num in nums:
        total += int(num)
print (total)
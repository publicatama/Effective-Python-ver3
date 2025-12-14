#-----------------------------------------------
names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]
print(counts)

#見づらい
longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

#まだみづらい
longest_name = None
max_count = 0

for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

#zipをつかおう
longest_name = None
max_count = 0

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
print(longest_name)

#追加時に問題が起こる
names.append("Rosalind")
for name, count in zip(names, counts):
    print(name)

#厳密評価にするとエラー
for name, count in zip(names, counts, strict=True):
    print(name)
    
#-----------------------------------------------
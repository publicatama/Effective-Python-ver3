#-----------------------------------------
#内包表記では式を3つ以上使わない

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
flat1 = [x for row in matrix1 for x in row]
print(flat1)

#これもまだ読みやすい👆👇

squared1 = [[x**2 for x in row] for row in matrix1]
print(squared1)

#しかしこれは読みづらい👇
my_lists1 = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[10,11,12,],[13,14,15],[16,17,18]],
    [[19,20,21],[22,23,24],[25,26,27]]
]
flat2 = [x for sublist1 in my_lists1
         for sablist2 in sublist1
         for x in sablist2]

print(flat2)

flat3 = []
for sublist1 in my_lists1:
    for sublist2 in sublist1:
        flat3.extend(sublist2)
        
print(flat3)

a = [1,2,3,4,5,6,7,8,9,10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
filtered1 = [[x for x in row if x % 4 == 0] for row in matrix2 if sum(row) >= 10]
print(filtered1)

#内包表記では多重ループとループごとの条件文をサポートできるが、式が３つ以上だと可読性が極めて低いので使わない。
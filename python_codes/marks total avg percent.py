a1,a2 = input().split()
# a2 = input()
a3 = input()
a4 = input()
a5 = input()

total = int(a1) + int(a2) + int(a3) + int(a4) + int(a5) 

average = ( int(a1) + int(a2) + int(a3) + int(a4) + int(a5) ) / 5 

percentage_1 = (int(a1) / total ) * 100
percentage_2 = (int(a2) / total ) * 100
percentage_3 = (int(a3) / total ) * 100
percentage_4 = (int(a4) / total ) * 100
percentage_5 = (int(a5) / total ) * 100


print("total = ",total)
print("average = ",average)
print("percentage of a1 = ",percentage_1)
print("percentage of a2 = ",percentage_2)
print("percentage of a3 = ",percentage_3)
print("percentage of a4 = ",percentage_4)
print("percentage of a5 = ",percentage_5)

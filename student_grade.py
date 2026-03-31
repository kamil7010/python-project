tamil = int(input('enter your tamil mark here:'))
eng = int(input('enter your eng mark here:'))
mat = int(input('enter your maths mark here:'))
sci = int(input('enter your science mark here:'))
soc = int(input('enter your social mark here:'))

total = tamil+eng+mat+sci+soc

avg = total / 5

if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = 'A'
elif avg >= 70:
    grade = 'B'
elif avg >= 60:
    grade = 'C'
else:
    print('Fail')
print(f'Your total {total} & {avg} mark is here')
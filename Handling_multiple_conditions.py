# P22
country = str.lower(input('What country do you live in? '))
# country = country.lower() # 输入字符转小写，方便条件匹配

if country == 'xx':
    province = str.lower(input('What province do you live in? ')) # 优化代码，一行搞定
    # province = province.lower() # 同 country 变量处理方式

    if province == 'abc':
        tax = 0.05
    elif province in('bcd','ddd','ddb','wiz'): # 相同条件放一起
        tax = .07
    elif province == 'oo':
        tax = .06
    else:
        tax = 0.15
else:
    tax = 0
print(tax) # 也可用在每条判断之后，但会增加代码量
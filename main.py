# იდენტური/არაიდენტური მონაცემების შედარება

my_birthyear = 1995
her_birthyear = 1995
our_birthyear = my_birthyear == her_birthyear
print("Our birthyear is same:")
print(our_birthyear)

my_birthmonth = "July"
her_birthmonth = "January"
our_birthmonth = my_birthmonth == her_birthmonth
print('Our birthmonth is same:')
print(our_birthmonth)

my_work = "TBC"
her_work = "TBC"
our_work = my_work != her_work
print("Our work is not same:")
print(our_work)

# შედარებითი ოპერატორები

my_age = 26
her_age = 22
print(my_age>her_age)
print(my_age<her_age)

# int + str

#რთული გზა:
print("მე ვმუშაობ თიბისიში " + str(6) + " თვეა")

#მარტივი გზა:
print(f"მე ვმუშაობ თიბისიში {6} თვეა")

# if True/False

if True:
    print("მე მაგარი კაცი ვარ")

# False ბრძანება არ იბეჭდება!
if False:
    print("მე არ ვარ მაგარი კაცი")


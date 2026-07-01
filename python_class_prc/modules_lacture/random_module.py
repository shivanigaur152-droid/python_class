import random
# emp_name=["aman","kamal","shivam","anshu"]
# res=random.choice(emp_name)
# print(res) 

# emp_name=["aman","kamal","shivam","anshu"]
# weight=[2,3,1,0]
# res=random.choices(emp_name,weights=weight,k=4)
# print(res)


# res=random.random()*1000
# print(int(res))

# rand_int=random.randint(1,10)
# rand_range=random.randrange(1,10)
# print(rand_int)
# print(rand_range)

# user max attempt = 6
# each attempt random number generate
# random number generate
# fix_value=150

# fix_value=150
# max_attempt=6

# # shuffle()
# emp_name=["aman","kamal","shivam","anshu"]
# random.shuffle(emp_name)
# print(emp_name)

# coupon code
def generate_cupon():
  a_to_z="abcdefghijklmnopqrstuvwxyz"
  num="1234567890"
  char=[random.choice(a_to_z) for i in range(1,5)]
  num=[random.choice(num) for i in range(1,5)]
  print("".join(char+num))

for i in range(1,10):
  generate_cupon()


  def generate_cupon():
      a_to_z="abcdefghijklmnopqrstuvwxyz"
      num="1234567890"

      
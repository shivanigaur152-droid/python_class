# creation of dictionary.
# indexing and slicing. ❌
# Traversing
# In-built methods
# dictionary comprehension 
# Assignment and class Activity

# --------- Defination and property of dictionary.
# 1.Dictionary is a data sturcture in python used store multiple data in 
# key:value format.
# 2.Ordered , mutable
# 3.Indexed by key , not position.
# 4.key must be unique (immuatable)
# 5.value can be any type of data.
# 6.Used in fast lookup


# ----------creation of dictionary.
# stu_profile={"aman":"noida","rohan":"delhi"}
# print(type(stu_profile))
# print(stu_profile)

# stu_marks=dict([("aman",300),("shivam",80)])
# print(stu_marks)

# stu_profile={"aman":"noida","rohan":"delhi"}
# stu_profile["aman"]="dubai"
# print(stu_profile)


#inbuilt_methods.
# stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':44}
# v=stu_marks.values()
# k=stu_marks.keys()
# i=stu_marks.items()
# res=stu_marks['rohan',"N/A"]
# print(v)
# print(k)
# print(i)
# print(res)

#update()
stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':44}
new_marks={"kamal":89,"ram":77,"aman":30}
stu_marks.update(new_marks)
print(stu_marks)


profile={
    'aman':{
        'address':["Noida","Delhi","mumbai"],
        'hobbies':["reading","cooking","travelling"],
        'password':{"insta":443534,"fb":87898},
        },

    'dev':{
        'address':["Noida","Delhi","mumbai","varanasi"],
        'hobbies':["reading","cooking","travelling"],
        'password':{"insta":"000000","fb":"1097867"},
        },

}
res=profile["dev"]["password"]["insta"]
res=profile["aman"]["password"]["insta"]

print(res)


# Traversing.
stu_marks={'aman': 300, 'shivam': 80 , 'rohan':40 , 'abhi':44}
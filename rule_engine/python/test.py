




def foo(sex, id, *args, **kargs):
    print(type(sex), "sex=", sex)
    print(type(id), "id=", id)
    print('args=', len(args))
    print("args...")
    for item in args:
        print(item)

    print("kargs...")
    for item in kargs.values():
        print(item)
    print(type(args))
    print(type(kargs))

# foo(4, b=5, name="wong", id=2)



def bar(*args, whenFunc=True):
    print("args...")
    print(type(args))
    for item in args:
        print(item)

bar(3)
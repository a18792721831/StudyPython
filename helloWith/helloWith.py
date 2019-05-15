class myWith():
    def __enter__(self):
        print('this is enter method')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_tb)
        print(exc_val)
        print(exc_type)
        print('this is exit method')


with myWith() as obj:
    print('this is do')
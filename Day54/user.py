

class User:
    def __init__(self, name):
        self.name = name;
        self.logged_in = False;
    

    def authenticate_decorator(function):
        def wrapper(*args):
            if args[0].logged_in == True:
                function();
        return wrapper;


    @authenticate_decorator
    def create_blog_post(self):
        return f"This is {self.name} blog post";
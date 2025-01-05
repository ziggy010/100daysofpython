class Instagram():
    def __init__(self, id, username):
        self.id = id;
        self.username = username.capitalize();
        self.followers = 0;
        self.following = 0;
    
    def follow(self, user):
        user.followers += 1;
        self.following += 1;


user_one = Instagram("001", "risab");
user_two = Instagram("002", "krisa");
user_three = Instagram("003", "risa");

user_one.follow(user_two);
user_three.follow(user_two);

print(user_one.following);
print(user_two.followers);



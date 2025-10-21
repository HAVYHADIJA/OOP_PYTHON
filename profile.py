#creating Class profile
class Profile:
    def __init__(self, name,favourite_language,hobby,tech_stack,github_username,fun_fact):
        self.name = name
        self.favourite_language = favourite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

# first method to introduce myself
    def introduce(self):
        print(f"Hello, My name is {self.name}, I love {self.favourite_language}, and I also enjoy {self.hobby}.")
    
# second method to display my tech stack
    def display_tech_stack(self):
        print("This is my Tech Stack:")
        for i in self.tech_stack:
            print(f"- {i}")

# method that returns my github profile link
    def github_profile(self):
        return f"https://github.com/{self.github_username}"
    
    
if __name__ == "__main__":
    my_profile = Profile(
        name="Nakalyowa Hadijah",
        favourite_language="Python",
        hobby="Listening to Podcasts",
        tech_stack=["Python", "JavaScript", "MERN", "CSS", "HTML"],
        github_username="havyhadija",
        fun_fact="i used to dance kalipso for my grandparents"
    )

    my_profile.introduce()
    my_profile.display_tech_stack()
    print(f"GitHub Profile:{my_profile.github_profile()}")
    
    







class Website:
    def __init__(self, name, siteURL, description):
        self.name = name
        self.siteURL = siteURL
        self.description = description

    def create_site(self):
        print("Enter the information about the site: ")
        self.name = input("Enter the site name: ")
        self.siteURL = input("Enter the siteURL: ")
        self.description = input("Enter the site description: ")

    def __str__(self):
        return (f"Information about the site: "
                f"name - {self.name}, "
                f"URL - {self.siteURL}, "
                f"description - {self.description}")

    def __add__(self, descr):
        self.description += " " + descr
        return self

    def __sub__(self, descr):
        self.description = self.description.replace(descr, "")
        return self

    def __eq__(self, other):
        return len(self.description) == len(other.description)

    def __gt__(self, other):
        return len(self.description) > len(other.description)

    def __lt__(self, other):
        return len(self.description) < len(other.description)


first_site = Website("", "", "")
second_site = Website("", "", "",)

first_site.create_site()
second_site.create_site()

print(first_site)
print(second_site)

print(first_site + "Some additional description")
print(second_site - "second description")

if first_site == second_site:
    print("This sites have the same description length")
elif first_site > second_site:
    print("First site description is longer than the second one")
elif first_site < second_site:
    print("Second site description is longer than the first one")

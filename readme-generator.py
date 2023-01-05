import json

def main():
    name = input("What is your Name?: ")
    about_me = []
    i = 0

    while True:
        print("Add an About Me about yourself based on points:\
        [Example: I love to Code/Travel.]")

        temp = input("Point {}: ".format(i))
        done = input("Are you done? (Yes/No): ")
        if done.lower() == "yes":
            break
        i += 1
        
    with open("tech.json") as tech_file:
        tech_stack_dict = json.load(tech_file)

    print("Please check the description file to add technology stack for front end and back end")
    print("Add the technology for Front End")

    user_front_end = []
    while True:
        temp = input("Technlogy for Front-End: ")
        user_front_end.append(temp)
        done = input("Done: (1 for done /0 for not done): ")
        if int(done) == 1:
            break
    
    user_back_end = []
    while True:
        temp = input("Technlogy for Back-End: ")
        user_back_end.append(temp)
        done = input("Done: (1 for done /0 for not done): ")
        if int(done) == 1:
            break
    
    linkedin_profile = input("What is your Linkedin Profile (URL): ")
    github_profile = input("What is your Github Profile (URL): ")
    email = input("What is your email? (Email): ")

    output_file = open("README.md", "w")
    output_file.write("# Hello I am {}\n".format(name))

    output_file.write("### &nbsp;About Me ")
    for point in about_me:
        temp = "- 🎓 &nbsp; "
        temp.append(point)
        output_file.write(temp)

    output_file.write("![myComp](https://user-images.githubusercontent.com/92009321/173706037-3414d647-59bd-475d-8595-a5c7c8da1aa2.gif)")
    output_file.write("## Tech Stack")

    output_file.write("## Front End")
    for tech in user_front_end:
        output_file.write("![{}]{}".format(tech, tech_stack_dict[tech]))
    
    output_file.write("## Back End")
    for tech in user_back_end:
        output_file.write("![{}]{}".format(tech, tech_stack_dict[tech]))

    output_file.write("<div align=\"center\">\
        <h3><b>Connect with me:</b></h3>\
        </div>\
        <p align=\"center\">\
        <a href=\"{}\" target=\"_blank\">\
        <img align=\"center\" alt=\"{} | Linkedin\" width=\"24px\" src=\"https://github.com/SatYu26/SatYu26/blob/master/Assets/Linkedin.svg\" />\
        </a> &nbsp;&nbsp;\
        <a href=\"mailto:{}\" >\
        <img align=\"center\" alt=\"{} | Gmail\" width=\"26px\" src=\"https://github.com/SatYu26/SatYu26/blob/master/Assets/Gmail.svg\" />\
        </a> &nbsp;&nbsp;\
        <p>".format(linkedin_profile, name, email, name)
    )

    output_file.close()


if __name__ == "__main__":
    main()




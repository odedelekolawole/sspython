file = open("main2.txt", "w")
file.write("Here are some of the things you can do \n")
applications = [
    "=> Machine Learning \n",
    "=> Web Development \n",
    "=> Data Science \n",
    "=> Automation \n",
]
file.writelines(applications)
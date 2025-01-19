universities_file = open("universities.csv", "r")

# for i, line in enumerate(universities_file):
#     if i > 10:
#         break
#     print(line)

universities_data = universities_file.readlines()
universities_file.close()

print(universities_data[:5])
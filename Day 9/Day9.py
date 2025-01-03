# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {};

# for item in student_scores:

#     if student_scores[item] > 90:
#         student_grades[item] = "Outstanding";
#     elif student_scores[item] > 80:
#         student_grades[item] = "Exceeds Expectations";
#     elif student_scores[item] > 70:
#         student_grades[item] = "Acceptable"
#     else:
#         student_grades[item] = "Fail"

# print(student_grades);

# travel_log = {
#     "France" : ["Paris", "lille", "Dijon"]
# }

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "France" : {
        "cities_visited": ["Paris", "lille", "Dijon"],
        "total_visited" : 10,
    },
    "Germany" :{
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited" : 5,
    }
}

print(travel_log["Germany"]["cities_visited"][2])
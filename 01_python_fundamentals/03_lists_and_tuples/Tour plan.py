tour_plan =("Istanbule", "Baku", "paris", "Tashkent", "Baku")
Access = tour_plan[3]
print(Access)
serch =tour_plan.count("Baku")
print(serch)
Find = tour_plan.index("Tashkent")
print(Find)
print(tour_plan)
temp_list = list(tour_plan)
temp_list.append("Lahore")
temp_list[2] = "London" 
tour_plan = tuple(temp_list)
print("Updated tour plan:", tour_plan)
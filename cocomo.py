print("             COCOMO MODEL")
print("Student Assignment Management System")

# User-defined input
kloc = float(input("Enter Project Size (KLOC): "))

# Basic COCOMO coefficients for Organic Mode
a = 2.4
b = 1.05
c = 2.5
d = 0.38

# COCOMO calculations
effort = a * (kloc ** b)

development_time = c * (effort ** d)

team_size = effort / development_time

# Display results
print("\nRESULTS")
print("------------------------------------------")
print("Project Name             : Student Assignment Management System")
print("Project Size (KLOC)      :", kloc)
print("Effort (Person-Months)   :", round(effort, 2))
print("Development Time (Months):", round(development_time, 2))
print("Average Team Size        :", round(team_size, 2))
print("------------------------------------------")

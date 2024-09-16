import random
import csv

# First names and surnames
first_names =   first_names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Krishna", 
    "Laksh", "Ayaan", "Dhruv", "Kabir", "Ishaan", "Rudra", "Shaurya", 
    "Atharv", "Ananya", "Aadhya", "Diya", "Saanvi", "Pari", "Ira", 
    "Navya", "Advika", "Aarohi", "Myra", "Amaira", "Sara", "Ishita", 
    "Anika", "Prisha", "Reyansh", "Dev", "Ayaan", "Harsh", "Aryan",
    "Riya", "Anvi", "Manvi", "Tanya", "Arya", "Meera", "Aarush", 
    "Raghav", "Yash", "Gauri", "Naina", "Tanvi", "Vanya", "Eva", 
    "Zara", "Manya", "Aadhvik", "Hriday", "Samarth", "Atharva", 
    "Ayansh", "Vivika", "Aditi", "Ishanvi", "Avi", "Kiaan", "Amaya", 
    "Anushka", "Aman", "Shiv", "Nirav", "Ved", "Ira", "Veer", "Jay", 
    "Siddharth", "Raahi", "Naina", "Gaurav", "Rudraansh", "Ahaan", 
    "Akshara", "Soham", "Manan", "Nandini", "Ayush", "Viraaj", "Krish", 
    "Rishi", "Tisha", "Harshita", "Kriti", "Radhika", "Divya", "Laksha", 
    "Kavya", "Bhuvi", "Chirag", "Ritik", "Vihan", "Riyaan", "Shlok", 
    "Aryaman", "Nikhil", "Shaan", "Om", "Saisha", "Yuvraj", "Yuvaan", 
    "Moksh", "Reva", "Anaya", "Tara", "Sia", "Kiara", "Niharika", 
    "Sohail", "Harshit", "Shruti", "Kaira", "Ayra", "Ishani", "Ritika", 
    "Samar", "Riyan", "Jiya", "Neha", "Anika", "Vidhi", "Vibha", 
    "Rahul", "Nandita", "Ishir", "Anvay", "Shivansh", "Devansh", 
    "Mahika", "Dhriti", "Harini", "Akira", "Shivika", "Arnav", 
    "Ishq", "Rakesh", "Sumit", "Vivek", "Charan", "Sahil", "Harshit", 
    "Surya", "Raj", "Aditi", "Aarohi", "Sanjana", "Karan", "Amisha", 
    "Ankita", "Ishika", "Manish", "Aishwarya", "Tanisha", "Rajesh", 
    "Jai", "Meghna", "Tina", "Kushal", "Bhairav", "Anusha", "Sumitra", 
    "Anand", "Sujata", "Vikas", "Priya", "Shreya", "Anjali", "Preeti", 
    "Smita", "Sunita", "Manish", "Rahul", "Ramesh", "Ajay", "Uday", 
    "Deepak", "Yogesh", "Sameer", "Gaurav", "Amit", "Sonal", "Naina", 
    "Mahesh", "Tejas", "Nikhil", "Vishal", "Sandeep", "Prakash", 
    "Mukesh", "Srinivas", "Deepti", "Aarti", "Swati", "Hema", 
    "Rohit", "Siddhi", "Rajiv", "Manju", "Rani", "Rohini", "Sudhir", 
    "Gopal", "Anil", "Kiran", "Vani", "Vinod", "Rekha", "Narendra", 
    "Parag", "Nikhilesh", "Bharath", "Anil", "Dinesh", "Geeta", 
    "Kalpana", "Anita", "Seema", "Laxmi", "Amol", "Mohan", "Anup", 
    "Ashwin", "Jayant", "Ravindra", "Hemant", "Milind", "Shravan", 
    "Inder", "Satish", "Ganesh", "Pankaj", "Rajendra", "Navin", 
    "Alok", "Bhaskar", "Jagdish", "Santosh", "Raghavendra", 
    "Vijay", "Ravi", "Shalini", "Lata", "Durga", "Saroj", "Suman", 
    "Sandhya", "Sita", "Devendra", "Rajesh", "Ashok", "Sunil", 
    "Satyendra", "Ranjan", "Bhaskar", "Sujith", "Pradeep", 
    "Sharad", "Sudhanshu", "Akhil", "Vasudha", "Sumathi", 
    "Sharanya", "Bharathi", "Sushma", "Chandra", "Vandana", 
    "Lakshmi", "Ashok", "Devika", "Meenakshi", "Shyam", 
    "Rupesh", "Madhavi", "Jayanti", "Leela", "Kalyani", "Srinidhi", 
    "Sunanda", "Kishore", "Vikram", "Neeraj", "Shalini", "Veena", 
    "Ganga", "Manju", "Rohini", "Manoj", "Vaibhav", "Suresh", 
    "Santosh", "Keshav", "Vivekanand", "Surendra", "Neha", 
    "Parth", "Kiran", "Aniket", "Bhavana", "Sheetal", "Kalpesh", 
    "Roshan", "Vinay", "Raj", "Anirudh", "Kanchan", "Sameera", 
    "Harshita", "Umesh", "Manasi", "Ajith", "Jagannath", 
    "Uma", "Charu", "Madhura", "Leena", "Chinmay", "Aadesh", 
    "Amrita", "Siddhartha", "Alka", "Maya", "Sita", "Krishna", 
    "Manu", "Nisha", "Gautam", "Harsha", "Raghavan", "Bhavya", 
    "Amol", "Vishnu", "Jayesh", "Parul", "Vijaya", "Trupti", 
    "Haritha", "Hemalatha", "Supriya", "Shanti", "Padma", 
    "Prasanna", "Srinivasa", "Kamal", "Shashi", "Radha", "Sharad", 
    "Vimal", "Mallika", "Madhu", "Saurabh", "Sanket", "Darshan", 
    "Anupama", "Swapnil", "Chaitanya", "Pranav", "Suraj", 
    "Bharath", "Jagadish", "Chirag", "Swarup", "Ravikumar", 
    "Srinivas", "Varun", "Ashwin", "Poonam", "Chinmay", 
    "Rupali", "Aishwarya", "Jitendra", "Rashmi", "Sneha", 
    "Naveen", "Teja", "Meenal", "Manu", "Preeti", "Jaya", 
    "Sanjay", "Sahil", "Shravan", "Ganesh", "Virendra"
]

surnames = ['Agarwal', 'Dangar', 'Valmiki', 'Choudhary', 'Sharma', 'Jain', 'Ahemad', 'Sherawat', 'Koushik', 'Pandit', 'Jat', 'Tiwari', 'Gupta']

# Generate 1000 names
names = []
for _ in range(10000):
    name = f"{random.choice(first_names)} {random.choice(surnames)}"
    names.append([name])

# Define the CSV file path
csv_file_path = "names.csv"

# Write the names to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name"])  # Writing header
    writer.writerows(names)

csv_file_path

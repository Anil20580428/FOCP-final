import random

def generate_email(student_id, name):
    # Here we split the name and student id
    fname= name.split(" ")
    # Initials 
    initials = ".".join([n[0] for n in fname])
    # Generating random numbers
    random_number = str(random.randint(1000, 9999))
    # Email Section
    email = f"{initials}{random_number}@poppleton.ac.uk"
    # Return the student ID and email
    student_id=student_id.split(" ")[0]
    return student_id, email

def main(input_filename):
    # Opening input files as students.txt and output files as encrypted.txt
    with open("students.txt", "r") as input_file, open("output.txt", "w") as output_file:

        for line in input_file:
            # Here we split the student id and name
            student_id, name = line.strip().split(", ")
            # Email for students
            student_id, email = generate_email(student_id, name)
            output_file.write(f"{student_id} {email}\n")

#Test the program here
main("students.txt")
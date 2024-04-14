Health and Fitness Club Management System

Description: 
The Health and Fitness Club Management System is a web application designed to manage various aspects of a health and fitness club, including member profiles, 
trainer schedules, room bookings, equipment maintenance, class schedules, billing, and payments for membership fees and personal training sessions.

Video presentation:
https://youtu.be/BByu4W7wn68?si=GltYv3uO9iawbAUK 

Templates
- Login.html: Allows users to log in to the system based on their account type (Member, Trainer, Staff).
NOTE: the login is case sensitive

- signup.html: Allows users to make an account to the system as a member only
- Dashboard.html: Displays a personalized dashboard for each user, showing relevant information and options based on their role.
- training_sessions.html: Displays upcoming training sessions for members to view and manage their bookings with trainers.
- fitness_goals.html: Enables members to set, track, and update their fitness goals, including target weight, target time, cardio records, and weightlifting goals.
- equipment_management.html: Provides staff with the ability to manage fitness equipment, including maintenance schedules, availability, and tracking.
- trainer_payroll_profiles.html: Allows staff to view and manage payroll profiles for trainers, including salary, hours worked, and payment details.
- class_schedule.html: Displays the schedule of classes available at the health and fitness club for members to enroll in.
- classes.html: Displays a list of classes offered by the club, including details like class name, instructor, and schedule.
- members.html : Allows staff to view a list of club members, including basic information like username and address.
- **trainers.html**: Allows staff to view a list of trainers, including basic information like username and specialization.
- trainer_profiles.html: Provides staff with the ability to view and manage trainer profiles, including qualifications, schedules, and client feedback

Database functions
- Add Health Metric: Enables members to add health metrics such as weight, height, blood pressure, and heart rate to track their fitness progress.
- Book Training Session: Allows members to book training sessions with available trainers by selecting a date and time.
- Add Fitness Goals: Enables members to set fitness goals, including target weight, target time, cardio records, and weightlifting goals.
- Manage Equipment: Provides staff with the ability to manage fitness equipment, including maintenance schedules and availability.
- View Trainer Payroll Profiles: Allows staff to view payroll profiles for trainers, including salary, hours worked, and other relevant information.
- View Classes: Displays a list of available classes for members to enroll in.
- View Members: Allows staff to view a list of all members along with their profiles and activity.
- View Trainers: Provides staff with a list of all trainers along with their profiles and schedules.
  
Installation:
-------------
1. Python 3.x is required to run the application.
2. Install Flask using pip: `pip install Flask`
3. Install psycopg2 for PostgreSQL database support: `pip install psycopg2`
4. Clone the repository: `git clone https://github.com/your/repository.git`
5. Navigate to the project directory: `cd path/to/project`
6. Run the Flask application: `python app.py`

Usage
1. Run the main.py file to start the application.
2. Use the login page to log in with your account credentials.
3. Explore the different pages and features of the application based on your role (member, trainer, staff)

Credits
Omar Hamzat (101244220) - all files and code

Copyright 2024  Omar Hamzat 
Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0


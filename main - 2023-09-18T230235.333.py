import time
import matplotlib.pyplot as plt

# Define a dictionary to store the time spent on each URL/app
activity_data = {}

# Function to track time spent on a URL/app
def track_activity(activity_name):
    if activity_name in activity_data:
        activity_data[activity_name] += 1
    else:
        activity_data[activity_name] = 1

# Simulate tracking by opening URLs/apps (replace with real tracking logic)
while True:
    user_input = input("Enter the URL/app name you're currently using (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    track_activity(user_input)

# Create a pie chart to visualize time spent on different activities
labels = activity_data.keys()
sizes = activity_data.values()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Time Spent on Different Activities")
plt.show()

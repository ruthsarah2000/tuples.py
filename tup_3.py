'''
3. Python Loops and Tuples in Analytical Applications
Task 1: Stock Market Data Analysis
Enhance your skills in data manipulation and analysis using tuples and loops.

Problem Statement:
You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, the date, and the closing price. Your task is to analyze this data to find the average closing price of a specified stock over a given period.
Create a function to calculate the average closing price of a specific stock symbol over all dates.
Ensure your solution handles cases where the stock symbol does not exist in the data.

'''

def average_closing_price(stock_data, symbol):
    total_price = 0
    count = 0
    for data in stock_data:
        if data[0] == symbol:
            total_price += data[2]
            count += 1
    
    if count == 0:
        return f"No data found for stock symbol '{symbol}'."
    else:
        return total_price / count


stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("AMZN", "2021-01-03", 180.0),
    ("GOOG", "2021-01-04", 1200.0)
]

print("Average closing price for AAPL:", average_closing_price(stock_data, "AAPL"))
print("Average closing price for TSLA:", average_closing_price(stock_data, "TSLA"))


'''
Task 2: Event Attendance Tracker
Apply loops and tuples to track and report on event attendance.

Problem Statement:
Your goal is to manage an attendance system for various events. Each attendee's data is stored as a tuple containing their name and the event they attended.

Develop a function to list all attendees of a specific event.
Implement a feature to count the number of attendees for each event.
'''

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    ("Bailey", "Google Fair"),
    ("Brink", "HJAIA Summit"),
    ("Sally", "Java Symposium")
]

def list_attendees(event_name, attendees):
    event_attendees = [attendee[0] for attendee in attendees if attendee[1] == event_name]
    if event_attendees:
        print(f"Attendees of {event_name}:")
        for attendee in event_attendees:
            print("-", attendee)
    else:
        print(f"No attendees found for {event_name}.")

def count_attendees(attendees):
    event_counts = {}
    for attendee in attendees:
        event_name = attendee[1]
        if event_name in event_counts:
            event_counts[event_name] += 1
        else:
            event_counts[event_name] = 1
    
    print("Number of attendees for each event:")
    for event_name, count in event_counts.items():
        print(f"- {event_name}: {count}")


event_name = "Python Conference"
list_attendees(event_name, attendees)

print()  
count_attendees(attendees)

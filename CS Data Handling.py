#2. Python Programming Challenges for Customer Service Data Handling
#Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

#Problem Statement: Develop a program that:

#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets or filter by status.
#Initialize with some sample tickets and include functionality for additional ticket entry.
#Example ticket structure:

#service_tickets = {
#    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
#}

#############################################################

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer, issue):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} opened.")
    else:
        print(f"Ticket {ticket_id} already issued.")

def ticket_status_update(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket {ticket_id} status updated to {status}.")
    else:
        print(f"Ticket {ticket_id} not found!")

def display_tickets(status=None):
    print("\n Service Tickets ")
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"{ticket_id}: {details}")

def add_ticket():
    ticket_id = input("Enter Ticket ID: ")
    customer = input("Enter Customer Name: ")
    issue = input("Enter Issue Description: ")

print("Service Tickets")
display_tickets()
while True:
    print("Options:\n    1 - Add Ticket\n    2 - Update Ticket\n    3 - Display Tickets\n    4 - Exit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        ticket_id = input("Enter Ticket ID: ")
        customer = input("Enter Customer Name: ")
        issue = input("Enter Issue Description: ")
        open_ticket(ticket_id, customer, issue)
    elif choice == "2":
        ticket_id = input("Enter Ticket ID to update: ")
        status = input("Enter status update (open/closed): ").strip().lower()
        ticket_status_update(ticket_id, status)
    elif choice == "3":
        filter_status = input("Filter by status (open/closed/leave blank for all): ").strip().lower() or None
        display_tickets(filter_status)
    elif choice == "4":
        print("Thank you. Goodbye!")
        break
    else:
        print("Choice not valid. Please enter choice from the menu options.\n")

open_ticket("Ticket003", "Nicholas", "CAPTCHA not loading")

ticket_status_update("Ticket001", "closed")

display_tickets()

display_tickets(status="open")



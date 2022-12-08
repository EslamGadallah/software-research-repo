class Ticket():

    #Defining variables needed
    counter = 2000

    staffName = ""
    staffEmail = ""
    staffID = ""
    ticketNumber = ""
    description = ""
    response = "Not Yet Provided"
    ticketstatus = "Open"

    ticketsCreated = 0
    ticketsOpened = 0
    ticketsClosed = 0

    #Constructor of the class
    def __init__(self, staffName="", staffEmail="", staffID="", description=""):
        self.staffName = staffName
        self.staffEmail = staffEmail
        self.staffID = staffID
        self.description = description
        Ticket.counter  += 1
        self.ticketNumber = Ticket.counter
        Ticket.ticketsCreated += 1
        Ticket.ticketsOpened += 1

        if ('password change' in self.description.lower()):
            self.response = "New password generated: " + Ticket.PasswordGenerator(self.staffID, self.staffName)
            self.ticketstatus = "Closed"

    #Method for showing the stats of the tickets
    def ShowStats():
        print('Tickets Created: ' + str(Ticket.ticketsCreated) + '\nTickets Open: ' + str(Ticket.ticketsOpened) + '\nTickets Closed: ' + str(Ticket.ticketsClosed))

    #Method for responding to tickets
    def RespondTicket(self, response):
        self.response = response
        self.ticketstatus = 'Closed'
        Ticket.ticketsOpened -= 1
        Ticket.ticketsClosed += 1
        print("\nTICKET CLOSED\n")

    #Method for re-opening tickets
    def ReopenTicket(self):
        self.ticketstatus = "Reopened"
        print("\nTICKET REOPENED\n")
        Ticket.ticketsOpened += 1
        Ticket.ticketsClosed -= 1

    #Method for getting the number of the ticket
    def getTicketNumber(self):
        return self.ticketNumber

    #Method for showing the ticket
    def ShowTicket(self): 
        print('Ticket number: ' + str(self.ticketNumber) + '\nTicket Creator: ' + self.staffName + '\nStaff ID: ' + self.staffID + '\nEmail: ' + self.staffEmail + '\nDescription: ' + self.description + '\nResponse: ' + self.response + '\nTicket status: ' + self.ticketstatus + '\n')
        print("---------------------------\n")

    #Static method for changing the password
    @staticmethod
    def PasswordGenerator(staffID, staffName):
            one = staffID[0:2]
            two = staffName[0:3]
            newPassword = one + two
            Ticket.ticketsClosed += 1
            Ticket.ticketsOpened -= 1

            return newPassword

    
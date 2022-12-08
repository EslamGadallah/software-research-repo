from Ticket import Ticket

class Main():

    #Main method of the tickting application.
    def Main():

        #Defining needed variables
        isRunning = "true"
        ticketsList = []
        print("Welcome \n")
        print("---------------------------\n")
        print("Please select from the following options: \n")

        #While loop for the application
        while(isRunning == "true"):
            print("0: Exit \n")
            print("1: Submit Ticket \n")
            print("2: Show Tickets \n")
            print("3: Respond to Ticket \n")
            print("4: Re-open Ticket \n")
            print("5: Display Stats \n")

            selection = input("Enter selection 0 - 5: ")
            
            if(selection == "0"):
                print("Thank you and Goodbye.")
                isRunning = 'false'

            elif(selection == "1"):
                staffName = input("Enter your name: ")
                staffId = input("Enter your Staff ID: ")
                staffEmail = input("Enter your Staff Email: ")
                ticketDesc = input("Enter a description of the issue: ")

                newTicket = Ticket(staffName, staffEmail, staffId, ticketDesc)
                ticketsList.append(newTicket)
                print("Your ticket has been added.\n")
                print("---------------------------\n")

            elif(selection == "2"):
                for i in range(len(ticketsList)):
                    ticketsList[i].ShowTicket()
                    print("---------------------------\n")
                    print("---------------------------\n")

            elif(selection == "3"):
                ticketNumber = input("Enter the number of ticket you want to respond to: ")
                ticketResponse = input("Enter your response: ")
                for i in range(len(ticketsList)):
                    ticketNeeded = ticketsList[i]
                    if (ticketNeeded.getTicketNumber() == int(ticketNumber)):
                        ticketNeeded.RespondTicket(ticketResponse)

            elif(selection == "4"):
                ticketNumber = input("Enter the number of ticket you want to re-open: ")
                for i in range(len(ticketsList)):
                    ticketNeeded = ticketsList[i]
                    if (ticketNeeded.getTicketNumber() == int(ticketNumber)):
                            ticketNeeded.ReopenTicket()

            elif(selection == "5"):
                Ticket.ShowStats()

            else:
                print("Please enter a valid number.")

    Main()
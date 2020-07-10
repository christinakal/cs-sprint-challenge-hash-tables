#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    # source: starting airport
    # destination: next airport
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # create an array with the same length as the tickets array
    destinations = [None] * length

    destination_lookup = dict()

    # store it's ticket's destination
    for ticket in tickets:
        destination_lookup[ticket.source] = ticket.destination
        # print(f"destination lookup: {destination_lookup}") # the chain starts with NONE

    # the starting ticket has a source of "NONE". Start there to build a chain
    next_destination = destination_lookup['NONE']


    for i in range(0, length):
        # record next destination
        destinations[i] = next_destination
        print(f"destinations[i]: {destinations[i]}")

        # retrieve next destination
        next_destination = destination_lookup[next_destination]
        print(f"next_destination: {next_destination}")


    return destinations


# tickets = [
#     Ticket{ source: "PIT", destination: "ORD" },
#     Ticket{ source: "XNA", destination: "CID" },
#     Ticket{ source: "SFO", destination: "BHM" },
#     Ticket{ source: "FLG", destination: "XNA" },
#     Ticket{ source: "NONE", destination: "LAX" },
#     Ticket{ source: "LAX", destination: "SFO" },
#     Ticket{ source: "CID", destination: "SLC" },
#     Ticket{ source: "ORD", destination: "NONE" },
#     Ticket{ source: "SLC", destination: "PIT" },
#     Ticket{ source: "BHM", destination: "FLG" }
# ]

# Output should be like: ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
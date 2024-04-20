
class Star_Cinema:
    hall_list=[]


    @classmethod
    def entry_hall(cls,rows, cols, hall_no):
        hall= Hall(rows,cols,hall_no)
        cls.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        Hall.hall_list.append(self)

    # def allocate_seat(self):
    #     seats = []
    #     for _ in range(self.rows):
    #         row = ['free'] * self.cols
    #     seats.append(row)

    # def entry_show(self, id, movie_name, time):
    #     show_info = (id, movie_name, time)
    #     self.show_list.append(show_info)


    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        seats = [[('free') for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seats


    def book_seats(self, id, seats):
        if id in self.seats:
            for seat in seats:
                row, col = seat
                if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                    print(f"Seat ({row}, {col}) is out of bounds.")
                    continue
                if self.seats[id][row][col] == 'free':
                    self.seats[id][row][col] = 'booked'
                    print(f"Seat ({row}, {col}) booked for show {id}.")
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
        else:
            print('ID does not exist.')

    
    def view_show_list(self):
        print("Shows running in this hall:")
        for show in self.show_list:
            print(f"MovieId: {show[0]}, MovieName: {show[1]}, ShowTime: {show[2]}")
    

    def view_available_seats(self,id):
        if id in self.seats:
            print(f"Available seats for show {id}:")
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.seats[id][row][col] == 'free':
                        print(f"Seat ({row}, {col})")
        else:
            print(f"Show with ID {id} does not exist.")

class Counter:
    __total_revenue = 10000
    
    def __init__(self, hall):
        self.hall = hall

    def view_all_shows(self):
        self.hall.view_show_list()

    def view_available_seats_in_show(self, id):
        self.hall.view_available_seats(id)

    def book_tickets(self, id, seat_list):
        self.hall.book_seats(id, seat_list)



hall = Hall(3,3,1)

hall.entry_show('1', "Singam", "12:00")
hall.entry_show('2', "Jawan", "2:00")


hall.view_show_list()
hall.book_seats('1',[(0, 1)])
print(hall.seats)
hall.book_seats('1',[(0, 1)])
hall.view_available_seats('1')
counter1 = Counter(hall)

run = True
while run:
    print("\n1. View all shows")
    print("2. View available seats in a show")
    print("3. Book tickets for a show")
    print("4. Exit")

    ch = input("Enter your ch: ")

    if ch == "1":
        counter1.view_all_shows()
    elif ch == "2":
        id = input("Enter the show ID: ")
        counter1.view_available_seats_in_show(id)
    elif ch == "3":
        show_id = input("Enter the show ID: ")
        seat_list =(input("Enter the seat Numer as row and colum(e.g: [(0,2)]) : "))
        counter1.book_tickets(show_id, seat_list)
    elif ch == "4":
        print("Exiting...")
        run = False
        break
    else:
        print("Invalid choice. Please try again.")
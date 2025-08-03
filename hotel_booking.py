room = {
    '101': {'type': 'Single', 'price': 1000, 'status': 'available'},
    '102': {'type': 'Double', 'price': 1500, 'status': 'available'},
    '103': {'type': 'Suite', 'price': 2500, 'status': 'available'},
    '104': {'type': 'Double', 'price': 1500, 'status': 'available'},
    '105': {'type': 'Single', 'price': 1000, 'status': 'available'}
}

booking = []

def available_room():
    print("\nAvailable Rooms are:")
    available = False
    for num, info in room.items():
        if info['status'] == 'available':
            print(f"Room {num}: {info['type']} - Rs{info['price']}")
            available = True
    if not available:
        print("No Rooms Available.\n")

def book_room():
    name = input("Enter guest name: ").strip().title()
    available_room()
    room_no = input("Enter Room No. to Book: ").strip()
    if room_no in room and room[room_no]['status'] == 'available':
        room[room_no]['status'] = 'booked'  # Fixed from '=='
        booking.append({'guest': name, 'room': room_no})
        print(f"\nRoom {room_no} Booked for {name}.")
        print(f"Total Price: Rs.{room[room_no]['price']}\n")
    else:
        print("\nRoom Not Available or Invalid Room No.\n")

def cancel_booking():
    name = input("Enter guest name to Cancel Booking: ").strip().title()
    found = False
    for b in booking:
        if b['guest'] == name:
            room_no = b['room']
            room[room_no]['status'] = 'available'
            booking.remove(b)
            print(f"\nBooking Cancelled for {name} (Room {room_no}).\n")
            found = True
            break
    if not found:
        print(f"\nNo Booking Found for {name}.\n")

def view_booking():
    print("\nCurrent Bookings:")
    if not booking:
        print("No Bookings Yet.\n")
    else:
        for b in booking:
            room_type = room[b['room']]['type']
            print(f"{b['guest']} - Room {b['room']} ({room_type})")
        print()

def main():
    while True:
        print("\nHotel Booking Menu")
        print("-" * 30)
        print("1. View Available Rooms")
        print("2. Book a Room")
        print("3. Cancel Booking")
        print("4. View All Bookings")
        print("5. Exit")

        try:
            ch = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if ch == 1:
            available_room()
        elif ch == 2:
            book_room()
        elif ch == 3:
            cancel_booking()
        elif ch == 4:
            view_booking()
        elif ch == 5:
            print("\nTHANK YOU! Visit Again.\n")
            break
        else:
            print("Invalid Choice. Try Again.")

main()
def is_lucky_ticket(ticket_number):
    if len(ticket_number) % 2 != 0:
        return False

    half_length = len(ticket_number) // 2
    first_half = list(map(int, ticket_number[:half_length]))
    second_half = list(map(int, ticket_number[half_length:]))

    return sum(first_half) == sum(second_half)

ticket_number = input("Введите номер билета: ")
if is_lucky_ticket(ticket_number):
    print("Этот билет счастливый!")
else:
    print("Этот билет не счастливый.")
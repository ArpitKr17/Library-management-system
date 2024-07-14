from django.dispatch import receiver
from lms.signals import book_add_signal, book_borrow_signal



@receiver(book_add_signal)
def book_add_receiver(sender, **kwargs):
    print(f'New Book is added')


@receiver(book_borrow_signal)
def book_borrowe_receiver(sender, **kwargs):
    print(f'Borrowed user is updated')


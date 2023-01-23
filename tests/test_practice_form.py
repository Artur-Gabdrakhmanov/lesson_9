from datetime import date

from demoqa_tests.model.data.user import User
from demoqa_tests.model.pages.practice_form import PracticePage

practice_form = PracticePage()


def test_practice_form():
    user = User(
        first_name='Chev',
        last_name='Chelios',
        email='ChevChelios@gmail.com',
        phone='1234567890',
        address='Moscow',
        birthday=date(1989, 10, 12),
        gender='Male',
        subject='Economics',
        hobbies='Music',
        image='1.png',
        state='NCR',
        city='Delhi')

    practice_form.open()
    practice_form.fill(user).submit()
    practice_form.assert_results_registration(user)

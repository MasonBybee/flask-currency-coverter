from unittest import TestCase, main
from app import app
from flask import session


app.config['TESTING'] = True


class ConvertTestCase(TestCase):


    def test_home_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Currency Converter</h1>', html)

    def test_invalid_currency_code(self):
        with app.test_client() as client:
            data = {
            "from_currency": "123",
            "to_currency": "USD",
            "amount": "100"
            }
            response = client.post('/convert', data=data)
            with client.session_transaction() as session:
                flashed_messages = session.get('_flashed_messages', [])
                self.assertIn('Not a valid code: 123', flashed_messages)


    def test_valid_conversion(self):
       with app.test_client() as client:
            resp = client.post('/convert', data={'from_currency': 'USD', 'to_currency': 'EUR', 'amount': '100'})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Result:', html)

    # def test_result_page(self):
    #     with app.test_client() as client:
    #         resp = client.get('/result')
    #         html = resp.get_data(as_text=True)
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn('<h1>Currency Converter</h1>', html)

if __name__ == '__main__':
    main()
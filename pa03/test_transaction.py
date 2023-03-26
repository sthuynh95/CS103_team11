'''Use pytest to test the transaction module'''

from transaction import Transaction

def test_add():
    '''test the add method'''
    transaction_list = Transaction()
    transaction = {'amount':11,'category':'food','date':'2019-01-01',
                        'description': 'test'}
    transaction_list.add(transaction)
    # note that transaction_list.select_active() is a list of dictionaries
    # transaction_list.select_active()[-1] is the last transaction in the list
    assert transaction_list.select_active()[-1]['amount'] == 11
    assert transaction_list.select_active()[-1]['category'] == 'food'
    assert transaction_list.select_active()[-1]['date'] == '2019-01-01'
    assert transaction_list.select_active()[-1]['description'] == 'test'
    transaction_list.delete(transaction_list.select_active()[-1]['item #'])
    

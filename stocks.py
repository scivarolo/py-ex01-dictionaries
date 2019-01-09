stock_dict = {
  'GM': 'General Motors',
  'AAPL': 'Apple',
  'MSFT': 'Microsoft',
  'GOOG': 'Google'
}

stock_purchases = [
  ('AAPL', 125, '10-sep-2001', 36),
  ('GOOG', 100, '1-apr-2009', 46),
  ('AAPL', 35, '12-dec-2018', 178),
  ('MSFT', 75, '5-mar-2012', 25)
]

def purchase_report(stock_purchases):
    """Loops through a list of purchases and prints a report."""
    for purchase in stock_purchases:
        abbrev = purchase[0]
        name = stock_dict[abbrev]
        date = purchase[2]
        shares = purchase[1]
        share_price = purchase[3]
        cost = shares * share_price
        print(f'I purchased {name} stock on {date} for ${cost}.')

purchase_report(stock_purchases)

def portfolio_report(purchases):
    """Loop through purchases, group them together by company and print a report."""
    grouped_purchases = {}
    for purchase in purchases:
        if purchase[0] in grouped_purchases:
            grouped_purchases[purchase[0]].append(purchase)
        else:
            grouped_purchases[purchase[0]] = [purchase]

    for key, stock_list in grouped_purchases.items():
        total_cost = 0
        print("\n")
        print("-------------- {0} --------------".format(key))
        for purchase in stock_list:
            total_cost += purchase[1] * purchase[3]
            print(purchase)
        print("Total value of {} in portfolio: ${}".format(key, total_cost))

portfolio_report(stock_purchases)
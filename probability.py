import csv

num_consec_candles = int(input("Enter the number of consecutive candles to analyze: "))

consec_green = 0
consec_red = 0
num_green_candles = 0
num_red_candles = 0
green_followed_by_green = 0
green_followed_by_red = 0
red_followed_by_green = 0
red_followed_by_red = 0

with open('Bitfinex.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    for row in reader:
        close_price = float(row[1].replace(',', ''))
        open_price = float(row[2].replace(',', ''))
        if close_price > open_price:
            num_green_candles += 1
            consec_green += 1
            if consec_red > 0:
                red_followed_by_green += 1
                consec_red = 0
            if consec_green >= num_consec_candles:
                green_followed_by_green += 1
            else:
                green_followed_by_red += 1
        else:
            num_red_candles += 1
            consec_red += 1
            if consec_green > 0:
                green_followed_by_red += 1
                consec_green = 0
            if consec_red >= num_consec_candles:
                red_followed_by_red += 1
            else:
                red_followed_by_green += 1

prob_green_after_n_green = green_followed_by_green / (green_followed_by_green + green_followed_by_red)
prob_red_after_n_green = 1 - prob_green_after_n_green
prob_green_after_n_red = red_followed_by_green / (red_followed_by_green + red_followed_by_red)
prob_red_after_n_red = 1 - prob_green_after_n_red

print('Number of green candles:', num_green_candles)
print('Number of red candles:', num_red_candles)
print('Probability of green after', num_consec_candles, 'consecutive green candles:', prob_green_after_n_green)
print('Probability of red after', num_consec_candles, 'consecutive green candles:', prob_red_after_n_green)
print('Probability of green after', num_consec_candles, 'consecutive red candles:', prob_green_after_n_red)
print('Probability of red after', num_consec_candles, 'consecutive red candles:', prob_red_after_n_red)



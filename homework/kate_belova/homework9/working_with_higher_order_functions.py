# fmt: off
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
                34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
                29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# fmt: on

hot_days = list(filter(lambda temp: temp > 28, temperatures))

the_hottest = max(hot_days)
the_less_hottest = min(hot_days)
avg_hot = sum(hot_days) / len(hot_days)

print(
    f'The hottest temperature: {the_hottest}\n'
    f'The less hottest temperature: {the_less_hottest}\n'
    f'The average among hot temperatures: {round(avg_hot, 2)}'
)

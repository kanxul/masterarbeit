import pandas as pd

start_block_reward = 50
reward_interval = 210000


def max_coins():
    current_reward = 50*10**8
    year = 0
    total = 0
    while current_reward > 1.0*10**8:

        total = total + (reward_interval * current_reward)
        current_reward = int(current_reward / 2)
        year = year + 4
        sfr = total/(reward_interval * (current_reward + 0.000001))
        pred_price = (2.71**14.6*sfr**3.3)/(total*10**-8)
        print("Y:{} R = {} T = {} SFR = {:4.2f} --> Pred Price {:8.2f} ".format(year, current_reward, total, sfr, pred_price))

    return total


print("Total BTC to ever be created {} Sathosi".format(max_coins()))




    
import math
import matplotlib.pyplot as plt
from text_gcn.train import train
from text_gcn.build_graph import build_graph


def mean(nums: list) -> float:
    return sum(nums) / len(nums)


def standard_deviation(mean_num: float, nums: list) -> float:
    the_sum = 0
    length = len(nums)
    for num in nums:
        the_sum = the_sum + math.pow((num - mean_num), 2)
    return math.sqrt(the_sum / length)


def plot_figure(mean_set: list, sd_set: list, label: str):
    f = plt.figure()
    plt.errorbar(
        [5, 10, 15, 20, 25, 30],  # set of X-axis
        mean_set,  # set of Y-axis
        yerr=sd_set,  # set of Y error
        label=label,
        fmt="ro--",
        linewidth=2
    )
    plt.xlabel("Window Size")
    plt.ylabel("Test Accuracy")

    plt.legend()
    plt.show()

    f.savefig("./window_" + label + ".png", bbox_inches='tight')


def produce_figure(dataset: str):
    sliding_window_size = 5
    test_accuracy_mean_set = []
    test_accuracy_sd_set = []
    while sliding_window_size < 31:
        temp_result = []
        for i in range(1, 6):
            print("Attempt: " + str(i) + "/" + "5")
            print("Building Graph of " + dataset + " in the window size of " + str(sliding_window_size))
            build_graph(dataset=dataset, sliding_window_size=sliding_window_size)
            temp_result.append(train(dataset))
        the_mean = mean(temp_result)
        the_sd = standard_deviation(mean_num=the_mean, nums=temp_result)
        test_accuracy_mean_set.append(the_mean)
        test_accuracy_sd_set.append(the_sd)
        sliding_window_size = sliding_window_size + 5
    plot_figure(mean_set=test_accuracy_mean_set, sd_set=test_accuracy_sd_set, label=dataset)

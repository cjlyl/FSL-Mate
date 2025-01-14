from paddlefsl.datasets import Omniglot

training_set = Omniglot(mode='train', root='~/.cache/paddle/dataset', image_size=(28, 28))


def get_item_test():
    image, label = training_set[15]
    print(image)  # A numpy array
    print(label)  # /images_background/Japanese_(katakana)/character44


def len_test():
    print(len(training_set))  # 22000


def class_num_test():
    print(training_set.class_num(mode='self'))  # 1100
    print(training_set.class_num(mode='total'))  # 1623


def split_task_test():
    print(training_set.class_num())  # 1100
    training_set.split_task(shuffle=True, train_class_num=1200)
    print(training_set.class_num())  # 1200


def sample_task_set_test():
    task = training_set.sample_task_set(ways=5, shots=5)
    print(task.support_data.shape)  # (25, 1, 18, 18)
    print(task.query_data.shape)  # (25, 1, 18, 18)


if __name__ == '__main__':
    get_item_test()
    len_test()
    class_num_test()
    split_task_test()
    sample_task_set_test()

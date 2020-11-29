""" Аблација Problem 6 (2 / 2)
Во науката за анализа на податоци откако ќе биде истрениран модел врз податочно множество базирано на неколку карактеристики, често се прави експеримент кој се нарекува аблација (отстранување). Целта на овој експеримент е да се одреди која од карактеристиките има најмногу влијание врз точноста на моделот, а со тоа и која е најклучна карактеристика - од која најмногу зависи класната припадност на примероците.

За оваа задача во променливата dataset ви е дадено податочно множество кое се однесува на цвеќиња наречени Iris. Секој ред од множеството се однесува на едно од трите класи на цвеќиња означени со 0, 1 и 2. За секое цвеќе има четири карактеристики кои се однесуваат на должината и ширината на неговите листови. Ова податочно множество го делите на два дела: тренирачко множество со првите 80% од редиците и тестирачко множество со останатите 20% од податоците.

Од стандарден влез се чита индексот на една колона од податочното множество во променливата column_ind. Ваша задача е да направите две дрва на одлука, така што првото дрво на одлука ќе ги користи сите карактеристики од податочното множество, додека второто дрво на одлука ќе го користи множеството каде што е отстранета колоната со индекс column_ind. Пресметајте точност со двете дрва и на стандарден излез испечатете ја точноста на двете дрва. """

from math import log
dataset = [
    [6.3, 2.9, 5.6, 1.8, 0],
    [6.5, 3.0, 5.8, 2.2, 0],
    [7.6, 3.0, 6.6, 2.1, 0],
    [4.9, 2.5, 4.5, 1.7, 0],
    [7.3, 2.9, 6.3, 1.8, 0],
    [6.7, 2.5, 5.8, 1.8, 0],
    [7.2, 3.6, 6.1, 2.5, 0],
    [6.5, 3.2, 5.1, 2.0, 0],
    [6.4, 2.7, 5.3, 1.9, 0],
    [6.8, 3.0, 5.5, 2.1, 0],
    [5.7, 2.5, 5.0, 2.0, 0],
    [5.8, 2.8, 5.1, 2.4, 0],
    [6.4, 3.2, 5.3, 2.3, 0],
    [6.5, 3.0, 5.5, 1.8, 0],
    [7.7, 3.8, 6.7, 2.2, 0],
    [7.7, 2.6, 6.9, 2.3, 0],
    [6.0, 2.2, 5.0, 1.5, 0],
    [6.9, 3.2, 5.7, 2.3, 0],
    [5.6, 2.8, 4.9, 2.0, 0],
    [7.7, 2.8, 6.7, 2.0, 0],
    [6.3, 2.7, 4.9, 1.8, 0],
    [6.7, 3.3, 5.7, 2.1, 0],
    [7.2, 3.2, 6.0, 1.8, 0],
    [6.2, 2.8, 4.8, 1.8, 0],
    [6.1, 3.0, 4.9, 1.8, 0],
    [6.4, 2.8, 5.6, 2.1, 0],
    [7.2, 3.0, 5.8, 1.6, 0],
    [7.4, 2.8, 6.1, 1.9, 0],
    [7.9, 3.8, 6.4, 2.0, 0],
    [6.4, 2.8, 5.6, 2.2, 0],
    [6.3, 2.8, 5.1, 1.5, 0],
    [6.1, 2.6, 5.6, 1.4, 0],
    [7.7, 3.0, 6.1, 2.3, 0],
    [6.3, 3.4, 5.6, 2.4, 0],
    [5.1, 3.5, 1.4, 0.2, 1],
    [4.9, 3.0, 1.4, 0.2, 1],
    [4.7, 3.2, 1.3, 0.2, 1],
    [4.6, 3.1, 1.5, 0.2, 1],
    [5.0, 3.6, 1.4, 0.2, 1],
    [5.4, 3.9, 1.7, 0.4, 1],
    [4.6, 3.4, 1.4, 0.3, 1],
    [5.0, 3.4, 1.5, 0.2, 1],
    [4.4, 2.9, 1.4, 0.2, 1],
    [4.9, 3.1, 1.5, 0.1, 1],
    [5.4, 3.7, 1.5, 0.2, 1],
    [4.8, 3.4, 1.6, 0.2, 1],
    [4.8, 3.0, 1.4, 0.1, 1],
    [4.3, 3.0, 1.1, 0.1, 1],
    [5.8, 4.0, 1.2, 0.2, 1],
    [5.7, 4.4, 1.5, 0.4, 1],
    [5.4, 3.9, 1.3, 0.4, 1],
    [5.1, 3.5, 1.4, 0.3, 1],
    [5.7, 3.8, 1.7, 0.3, 1],
    [5.1, 3.8, 1.5, 0.3, 1],
    [5.4, 3.4, 1.7, 0.2, 1],
    [5.1, 3.7, 1.5, 0.4, 1],
    [4.6, 3.6, 1.0, 0.2, 1],
    [5.1, 3.3, 1.7, 0.5, 1],
    [4.8, 3.4, 1.9, 0.2, 1],
    [5.0, 3.0, 1.6, 0.2, 1],
    [5.0, 3.4, 1.6, 0.4, 1],
    [5.2, 3.5, 1.5, 0.2, 1],
    [5.2, 3.4, 1.4, 0.2, 1],
    [5.5, 2.3, 4.0, 1.3, 2],
    [6.5, 2.8, 4.6, 1.5, 2],
    [5.7, 2.8, 4.5, 1.3, 2],
    [6.3, 3.3, 4.7, 1.6, 2],
    [4.9, 2.4, 3.3, 1.0, 2],
    [6.6, 2.9, 4.6, 1.3, 2],
    [5.2, 2.7, 3.9, 1.4, 2],
    [5.0, 2.0, 3.5, 1.0, 2],
    [5.9, 3.0, 4.2, 1.5, 2],
    [6.0, 2.2, 4.0, 1.0, 2],
    [6.1, 2.9, 4.7, 1.4, 2],
    [5.6, 2.9, 3.6, 1.3, 2],
    [6.7, 3.1, 4.4, 1.4, 2],
    [5.6, 3.0, 4.5, 1.5, 2],
    [5.8, 2.7, 4.1, 1.0, 2],
    [6.2, 2.2, 4.5, 1.5, 2],
    [5.6, 2.5, 3.9, 1.1, 2],
    [5.9, 3.2, 4.8, 1.8, 2],
    [6.1, 2.8, 4.0, 1.3, 2],
    [6.3, 2.5, 4.9, 1.5, 2],
    [6.1, 2.8, 4.7, 1.2, 2],
    [6.4, 2.9, 4.3, 1.3, 2],
    [6.6, 3.0, 4.4, 1.4, 2],
    [6.8, 2.8, 4.8, 1.4, 2],
    [6.7, 3.0, 5.0, 1.7, 2],
    [6.0, 2.9, 4.5, 1.5, 2],
    [5.7, 2.6, 3.5, 1.0, 2],
    [5.5, 2.4, 3.8, 1.1, 2],
    [5.4, 3.0, 4.5, 1.5, 2],
    [6.0, 3.4, 4.5, 1.6, 2],
    [6.7, 3.1, 4.7, 1.5, 2],
    [6.3, 2.3, 4.4, 1.3, 2],
    [5.6, 3.0, 4.1, 1.3, 2],
    [5.5, 2.5, 4.0, 1.3, 2],
    [5.5, 2.6, 4.4, 1.2, 2],
    [6.1, 3.0, 4.6, 1.4, 2],
    [5.8, 2.6, 4.0, 1.2, 2],
    [5.0, 2.3, 3.3, 1.0, 2],
    [5.6, 2.7, 4.2, 1.3, 2],
    [5.7, 3.0, 4.2, 1.2, 2],
    [5.7, 2.9, 4.2, 1.3, 2],
    [6.2, 2.9, 4.3, 1.3, 2],
    [5.1, 2.5, 3.0, 1.1, 2],
    [5.7, 2.8, 4.1, 1.3, 2],
    [6.4, 3.1, 5.5, 1.8, 0],
    [6.0, 3.0, 4.8, 1.8, 0],
    [6.9, 3.1, 5.4, 2.1, 0],
    [6.8, 3.2, 5.9, 2.3, 0],
    [6.7, 3.3, 5.7, 2.5, 0],
    [6.7, 3.0, 5.2, 2.3, 0],
    [6.3, 2.5, 5.0, 1.9, 0],
    [6.5, 3.0, 5.2, 2.0, 0],
    [6.2, 3.4, 5.4, 2.3, 0],
    [4.7, 3.2, 1.6, 0.2, 1],
    [4.8, 3.1, 1.6, 0.2, 1],
    [5.4, 3.4, 1.5, 0.4, 1],
    [5.2, 4.1, 1.5, 0.1, 1],
    [5.5, 4.2, 1.4, 0.2, 1],
    [4.9, 3.1, 1.5, 0.2, 1],
    [5.0, 3.2, 1.2, 0.2, 1],
    [5.5, 3.5, 1.3, 0.2, 1],
    [4.9, 3.6, 1.4, 0.1, 1],
    [4.4, 3.0, 1.3, 0.2, 1],
    [5.1, 3.4, 1.5, 0.2, 1],
    [5.0, 3.5, 1.3, 0.3, 1],
    [4.5, 2.3, 1.3, 0.3, 1],
    [4.4, 3.2, 1.3, 0.2, 1],
    [5.0, 3.5, 1.6, 0.6, 1],
    [5.9, 3.0, 5.1, 1.8, 0],
    [5.1, 3.8, 1.9, 0.4, 1],
    [4.8, 3.0, 1.4, 0.3, 1],
    [5.1, 3.8, 1.6, 0.2, 1],
    [5.5, 2.4, 3.7, 1.0, 2],
    [5.8, 2.7, 3.9, 1.2, 2],
    [6.0, 2.7, 5.1, 1.6, 2],
    [6.7, 3.1, 5.6, 2.4, 0],
    [6.9, 3.1, 5.1, 2.3, 0],
    [5.8, 2.7, 5.1, 1.9, 0],
]


def unique_counts(rows):
    results = {}
    for row in rows:
        r = row[len(row) - 1]
        if r not in results:
            results[r] = 0
        results[r] += 1
    return results


def entropy(rows):
    log2 = lambda x: log(x) / log(2)
    results = unique_counts(rows)
    ent = 0.0
    for r in results.keys():
        p = float(results[r]) / len(rows)
        ent = ent - p * log2(p)
    return ent


class DecisionNode:
    def __init__(self, col=-1, value=None, results=None, tb=None, fb=None):
        self.col = col
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb


def compare_numerical(row, column, value):
    return row[column] >= value


def compare_nominal(row, column, value):
    return row[column] == value


def divide_set(rows, column, value):
    if isinstance(value, int) or isinstance(value, float):
        split_function = compare_numerical
    else:
        split_function = compare_nominal
    set1 = [row for row in rows if
            split_function(row, column, value)]
    set2 = [row for row in rows if
            not split_function(row, column, value)]
    return set1, set2


def build_tree(rows, scoref=entropy):
    if len(rows) == 0:
        return DecisionNode()
    current_score = scoref(rows)
    best_gain = 0.0
    best_criteria = None
    best_sets = None

    column_count = len(rows[0]) - 1
    for col in range(0, column_count):
        column_values = {}
        for row in rows:
            column_values[row[col]] = 1

        for value in column_values.keys():
            (set1, set2) = divide_set(rows, col, value)
            p = float(len(set1)) / len(rows)
            gain = current_score - p * scoref(set1) - (1 - p) * scoref(set2)
            if gain > best_gain and len(set1) > 0 and len(set2) > 0:
                best_gain = gain
                best_criteria = (col, value)
                best_sets = (set1, set2)
    if best_gain > 0:
        true_branch = build_tree(best_sets[0], scoref)
        false_branch = build_tree(best_sets[1], scoref)
        return DecisionNode(col=best_criteria[0], value=best_criteria[1],
                            tb=true_branch, fb=false_branch)
    else:
        return DecisionNode(results=unique_counts(rows))


def print_tree(tree, indent=''):
    if tree.results:
        print(str(tree.results))
    else:
        print(str(tree.col) + ':' + str(tree.value) + '? ')
        # Се печатат True гранките, па False гранките
        print(indent + 'T->', end='')
        print_tree(tree.tb, indent + '  ')
        print(indent + 'F->', end='')
        print_tree(tree.fb, indent + '  ')


def classify(observation, tree):
    if tree.results:
        return tree.results
    else:
        value = observation[tree.col]
        if isinstance(value, int) or isinstance(value, float):
            compare = compare_numerical
        else:
            compare = compare_nominal

        if compare(observation, tree.col, tree.value):
            branch = tree.tb
        else:
            branch = tree.fb

        return classify(observation, branch)




if __name__ == "__main__":
    column_ind = int(input())

    # Vashiot kod tuka

    trainData1 = dataset[: int(len(dataset)*0.8)]
    trainData2 = list()

    test_set1 = dataset[int(len(dataset)*0.8) :]
    test_set2 = list()

    for train_sample in trainData1:
        sample = [train_sample[i] for i in range(len(train_sample)) if i != column_ind]
        trainData2.append(sample)

    for train_sample in test_set1:
        sample = [train_sample[i] for i in range(len(train_sample)) if i != column_ind]
        test_set2.append(sample)

    tree1 = build_tree(trainData1, entropy)
    tree2 = build_tree(trainData2, entropy)

    correctSamples1, correctSamples2= 0, 0

    for test_sample in test_set1:
        true_class = test_sample[-1]
        result1 = classify(test_sample, tree1)
        res = sorted(list(result1.items()),key=lambda x: x[1], reverse=True)[0][0]
        if res == true_class:
            correctSamples1 += 1
    for test_sample in test_set2:
        true_class= test_sample[-1]
        result2 = classify(test_sample, tree2)
        res = sorted(list(result2.items()),key=lambda x: x[1],reverse=True)[0][0]
        if res == true_class:
            correctSamples2 += 1

    accuracy1 = correctSamples1/len(test_set1)
    accuracy2 = correctSamples2 / len(test_set2)

    print("Tochnost so prvoto drvo na odluka: " + str(accuracy1))
    print("Tochnost so vtoroto drvo na odluka: " + str(accuracy2))
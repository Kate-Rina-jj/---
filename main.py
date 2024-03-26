class Classifier:
    def __init__(self, data):
        self.data = data

    def euclidean_distance(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def predict_class(self, predict_point, k):
        distances = []
        for class_name, points in self.data.items():
            for point in points:
                distance = self.euclidean_distance(predict_point, point)
                distances.append((class_name, distance))

        distances.sort(key=lambda x: x[1])
        nearest_neighbors = distances[:k]
        classes_count = {}
        for neighbor in nearest_neighbors:
            if neighbor[0] not in classes_count:
                classes_count[neighbor[0]] = 0
            classes_count[neighbor[0]] += 1

        predicted_class = max(classes_count, key=classes_count.get)
        return predicted_class


data = {}
while True:
    x = int(input("Введите координаты точки по значению x: "))
    y = int(input("Введите координаты точки по значению y: "))
    class_name = input("Введите класс объекта: ")

    if class_name not in data:
        data[class_name] = []

    data[class_name].append((x, y))

    choice = input("Хотите ли Вы еще добавить точку? (y/n) ")
    if choice != 'y':
        break

predict_point = tuple(map(int, input("Введите координаты точки неизвестного класса: ").split()))
k = int(input("Задайте величину радиуса ближайших соседей: "))

classifier = Classifier(data)
predicted_class = classifier.predict_class(predict_point, k)

print(f"Предсказанный класс точки: {predicted_class}")

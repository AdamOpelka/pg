#def process_numbers(numbers):
#    result = []
#    for num in numbers:
#        if num == 10:
 #           break
  #      if num > 5:
   #         result.append(num * 2)
    #return result

# Pytest testy pro Příklad 1
#def test_process_numbers():
    #assert process_numbers([1, 6, 3, 10, 8]) == [12]
    #assert process_numbers([7, 8, 10, 12]) == [14, 16]
    #assert process_numbers([1, 2, 3, 4]) == []
    #assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}
'''
def fetch_and_save_data():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for item in data:
            user_id = item.get("userId")
            item["userName"] = user_names.get(user_id, "Unknown")

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        return True
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return False
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

# Pytest testy pro Příklad 2
from unittest.mock import patch, MagicMock, mock_open

def test_fetch_and_save_data():
    mock_data = [
        {"userId": 1, "id": 1, "title": "Test post", "body": "This is a test."}
    ]
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_data), text=json.dumps(mock_data), content=json.dumps(mock_data))

        with patch("builtins.open", mock_open()) as mock_file:
            assert fetch_and_save_data() == True
            mock_file().write.call_args[0][0] == json.dumps([
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Test post",
                    "body": "This is a test.",
                    "userName": "Leanne Graham"
                }
            ])
            '''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3

    with patch("abc.ABC", side_effect=NotImplementedError):
        try:
            shape = Shape()
        except TypeError:
            pass
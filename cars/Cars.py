import os
import csv
import sys
import io

def get_car_list(csv_filename):
    vehicle_list =[]
    with io.open(csv_filename,encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if row and row[0]:
                vehicle = None
                if(row[0] == "car"):
                    vehicle = Car(row[1], row[2], row[3], row[5])
                if(row[0] == "truck"):
                    vehicle = Truck (row[1], row[3], row[4], row[5])
                    print(vehicle.body_height, vehicle.body_length, vehicle.body_width)
                if (row[0] == "spec_machine"):
                    vehicle = SpecMachine(row[1], row[3], row[5], row[6])
                vehicle_list.append(vehicle)
    # print(vehicle_list)
    return  vehicle_list

class BaseCar:
    def __init__(self, brand, photo_file_name, carrying, car_type):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    def get_photo_file_ext(self):
        file_extension = os.path.splitext(self.photo_file_name)
        return file_extension

class Car(BaseCar):
    def __init__(self, brand, passenger_seats_count, photo_file_name, carrying ):
        super().__init__(brand, photo_file_name, carrying, car_type = "car")
        self.passenger_seats_count = int(passenger_seats_count) if passenger_seats_count != '' else 0

class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, body_whl, carrying ):
        super().__init__(brand, photo_file_name, carrying, car_type = "truck")
        self.body_whl = body_whl
        self.body_length, self.body_width, self.body_height = self.split_body_whl()

    def split_body_whl(self):
        if(self.body_whl == ""):
            return 0.0,0.0,0.0
        else:
            body_params = self.body_whl.split('x')
            return float(body_params[0]), float(body_params[1]), float(body_params[2])

    def get_body_volume(self):
        return self.body_height*self.body_length*self.body_width

class SpecMachine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying, car_type = "spec_machine")
        self.extra = extra

if __name__ == "__main__":
    # try:
    #     sys.argv[1]
    #     csv_filename = sys.argv[1]
        csv_filename = "coursera_week3_cars.csv"
        get_car_list(csv_filename)
    # except IndexError:
    #     print("I can not find the file")
    # except OSError:
    #     print ("I can not open", sys.argv[1])
    # except:
    #     print("Something is wrong")




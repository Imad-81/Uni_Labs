class Vehicle {
    void drive() {
        System.out.println("Driving a vehicle");
    }
}

class Car extends Vehicle {
    @Override
    void drive() {
        System.out.println("Driving a car");
    }
}

public class TestVehicle {
    public static void main(String[] args) {
        Vehicle v = new Car(); // polymorphism
        v.drive();
    }
}
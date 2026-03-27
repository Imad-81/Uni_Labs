// Parent class
class Employee {
    String name;
    double salary;

    // Constructor
    Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    void work() {
        System.out.println(name + " is working");
    }

    double getSalary() {
        return salary;
    }
}

// Child class
class HRManager extends Employee {

    // Constructor
    HRManager(String name, double salary) {
        super(name, salary);
    }

    @Override
    void work() {
        System.out.println(name + " manages employees");
    }

    void addEmployee() {
        System.out.println(name + " is adding a new employee");
    }
}

// Main class
public class TestEmployee {
    public static void main(String[] args) {
        Employee emp = new HRManager("Ravi", 50000); // polymorphism

        emp.work();
        System.out.println("Salary: " + emp.getSalary());

        // Downcasting to access child-specific method
        HRManager hr = (HRManager) emp;
        hr.addEmployee();
    }
}
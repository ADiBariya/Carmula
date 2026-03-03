class CarPhysics {
    constructor(weight) {
        this.weight = weight;
        this.velocity = 0;
        this.acceleration = 0;
        this.position = 0;
    }

    applyForce(force) {
        // F = ma
        this.acceleration = force / this.weight;
    }

    update(deltaTime) {
        this.velocity += this.acceleration * deltaTime;
        this.position += this.velocity * deltaTime;
    }

    getPosition() {
        return this.position;
    }

    getVelocity() {
        return this.velocity;
    }
} \n\n// Example usage:\nconst car = new CarPhysics(1500); // weight of 1500 kg\ncar.applyForce(3000); // apply a force of 3000 N\ncar.update(1); // update for 1 second\nconsole.log(car.getPosition()); // get the current position

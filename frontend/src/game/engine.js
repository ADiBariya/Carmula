// Babylon.js game engine for Carmula

import { Engine, Scene } from '@babylonjs/core';

class GameEngine {
    constructor(canvasElementId) {
        this.canvas = document.getElementById(canvasElementId);
        this.engine = new Engine(this.canvas, true);
        this.scene = new Scene(this.engine);
    }

    initialize() {
        // Initialize the game scene
        this.engine.runRenderLoop(() => {
            this.scene.render();
        });

        // Resize the engine on window resize
        window.addEventListener('resize', () => {
            this.engine.resize();
        });
    }

    // Additional game methods can be added here
}

export default GameEngine;

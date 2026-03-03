// Main Menu UI for Carmula

import React from 'react';
import './menu.css';

const Menu = () => {
    return (
        <div className="menu">
            <h1>Carmula Main Menu</h1>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
                <li><a href="#logout">Logout</a></li>
            </ul>
        </div>
    );
};

export default Menu;

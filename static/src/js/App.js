import React, { Component } from 'react';
import ItemShelf from "./ItemShelf";
import Card from './Card';
import '../css/main.css';

class App extends Component { 
    constructor(props) { 
        super(props);
    }
    render() { 
        return (
            <div>
                <div className="split left">
                    <ItemShelf />
                </div>
                <div className="split right">
                    <Card />
                </div>
            </div>
        )
    }
}

export default App;
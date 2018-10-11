import React, { Component } from 'react';
import ItemShelf from "./ItemShelf";
import Card from './Card';
import '../css/main.css';

import ItemStore from "./ItemStore"

const TOPIC = "addcard";
class App extends Component { 
    constructor(props) { 
        super(props);
    }
    render() { 
        return (
            <div>
                <div className="split left">
                    <ItemShelf topic={TOPIC}/>
                </div>
                <div className="split right">
                    <Card topic={TOPIC}/>
                </div>
            </div>
        )
    }
}

export default App;
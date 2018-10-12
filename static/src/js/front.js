import "../css/main.css"
import React from "react"
import ReactDOM from  "react-dom"

// import TodoStore from "./TodoStore"
// import TodoList from "./TodoList"

import App from "./App"

const app = document.getElementById("app");

// ReactDOM.render(<Counter store={TodoStore} />, app)
ReactDOM.render(<App />, app)

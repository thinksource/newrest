import "../css/main.css"
import React from "react"
import ReactDOM from  "react-dom"

// import TodoStore from "./TodoStore"
// import TodoList from "./TodoList"
import Counter from "./Counter"
import App from "./App"
import AppState from "./AppState"
const app = document.getElementById("app");
const appstate = new AppState();
console.log(appstate);
// ReactDOM.render(<Counter store={TodoStore} />, app)
ReactDOM.render(<App store={appstate}/>, app)

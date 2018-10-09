import { observable, action } from "mobx";

class AppState { 
    @observable count = 0;
    
    @action.bound
    increment() {

        this.count += 1;
    }

    @action.bound
    decrement() { 
        this.count -= 1;
    }

    constructor() { 
        this.count = 0;

    }
}

export default AppState
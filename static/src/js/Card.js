import React, { Component } from 'react';
import { Table, Button, Input, notification} from 'antd';
import PubSub from 'pubsub-js';
import { v4 } from "uuid";
import axios from "axios";


function copy(o) {
    var output, v, key;
    output = Array.isArray(o) ? [] : {};
    for (key in o) {
        v = o[key];
        output[key] = (typeof v === "object") ? copy(v) : v;
    }
    return output;
}
class Card extends Component {
    static mystate;
    card_columns = [
        { title: 'Product Id', dataIndex: 'product_id', key: 'product_id' },
        { title: 'Name', dataIndex: 'product_name', key: 'name' },
        { title: 'Amount', dataIndex: 'amount', key: 'amount' },
        { title: 'Price', dataIndex: 'item_price', key: 'price' },
        {
            title: 'Action', dataIndex: "id", key: 'x', render: (x) =>
                <Button onClick={()=>this.deleteitem(x)}>Delete</Button>
        }
    ];

    constructor(props) { 
        super(props);
        this.state = {
            OrderItems: []
        };
        this.mystate = [];

    }

    componentDidMount() {
        this.pubsub_token=PubSub.subscribe(this.props.topic, function (msg, data) {
            
            for (let i of data) {
                console.log(i);
                console.log(this.mystate);
                let exist_item = this.mystate.filter(item => item["product_id"] == i["id"]);
                console.log(exist_item);
                if (exist_item.length >= 1) {
                    exist_item[0]["amount"] += 1;
                } else {
                    let tmp = {
                        "id": v4(),
                        "product_name": i["name"],
                        "amount": 1,
                        "item_price": i["price"],
                        "product_id": i["id"]
                    };
                    console.log(tmp);
                    this.mystate.push(tmp);
                    console.log(this.mystate);
                    
                }
            }
            this.setState({});
        }.bind(this));
    }

    getDerivedStateFromProps(props, state) { 
        return { OrderItems: copy(this.mystate) };
    }

    componentDidUpdate(prevProps, prevState) { 
        console.log(prevState.OrderItems);
        
        console.log(this.mystate);
        if (this.mystate != prevState.OrderItems) { 
            this.state.OrderItems=copy(this.mystate)
        }
        console.log(this.state);
    }

    componentWillUnmount() { 
        PubSub.unsubscribe(this.pubsub_token);
    }

    deleteitem(id) {
        for (let i = 0; i < this.mystate.length; i++) { 
            if (this.mystate[i]["id"] == id) { 
                this.mystate.splice(i, 1);
                this.setState({});
                break;
            }
        }
    }

    sendOrder() {
        let mycus = document.getElementById("customer").value;
        let myjson = {
            desc: document.getElementById("desc").value,
            customer: mycus,
            status: "creat",
            order_item: this.mystate
        }
        console.log(myjson);
        axios.post('/api/order', myjson).then(
            res => { 
                if (res.status == 201) { 
                    this.mystate = [];
                    notification.open({
                        message: "Order successfull",
                        description:`${mycus} order number is ${res.data.id}`
                    })
                    this.setState({});
                }
                console.log(res);
            }
        ).catch(err => { 
            notification.open({
                message: "Order Error",
                description: JSON.stringify(err.data)
            });
            this.mystate = [];
            this.setState({});
        })
    }

    

    render() { 
        return (
            <div>
                <h3>Shopping Card</h3>
                <label for="customer">Customer Name:</label>
                <Input type="text" defaultValue="my name" id="customer"></Input>
                <label for="desc">Writen some description of this order</label>
                <Input type="text" id="desc"></Input>
                <Button onClick={()=>this.sendOrder()} type="primary">Order</Button>
            <Table  columns={this.card_columns}
                    dataSource={this.mystate} />
            </div>
        )
    }
}

export default Card;
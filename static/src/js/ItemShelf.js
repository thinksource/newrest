import React, { Component } from 'react';
import { Table, Button } from 'antd';
import axios from 'axios';
import PubSub from 'pubsub-js';
// import 'antd/dist/antd.css';
import "@babel/polyfill";


// rowSelection object indicates the need for row selection
const rowSelection = {
    onChange: (selectedRowKeys, selectedRows) => {
        console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
    },
    getCheckboxProps: record => ({
        disabled: record.name === 'Disabled User', // Column configuration not to be checked
        name: record.name,
    }),
};

class ItemShelf extends Component {
    product_columns = [
        { title: 'Id', dataIndex: 'id', key: 'id' },
        { title: 'Name', dataIndex: 'name', key: 'name' },
        { title: 'Provider', dataIndex: 'provider', key: 'provider' },
        { title: 'Price', dataIndex: 'price', key: 'price' },

    ];

    rowSelection = {
        onChange: (selectedRowKeys, selectedRows) => {
            console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
            this.setState({
                selectItem: selectedRows
            })
        },
        getCheckboxProps: record => ({
            disabled: record.name === 'Disabled User', // Column configuration not to be checked
            name: record.name,
        }),
    };
    constructor(props) {
        super(props);
        this.state = {
            selectItem:[]
        }
    }
    
    componentWillMount() { 
        this.init_product();
    }
    async init_product() {
        let that = this;
        await axios.get('/api/product').then(res => {
            if (res.status == 200) {
                that.setState(
                    { productdata: res.data }
                );
            }
        });
    }

    addCard() { 
        console.log(this.state.selectItem);
        PubSub.publish(this.props.topic, this.state.selectItem);
    }

    render() {
        return (
            <div>
                <h3>Item Shelf:</h3>
                <Button onClick={()=>this.addCard()}>Add Card</Button>
                <Table rowSelection={this.rowSelection} columns={this.product_columns}
                    dataSource={this.state.productdata} />
            </div>
        )
    }
}


export default ItemShelf;
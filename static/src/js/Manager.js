
import React, { Component } from 'react';
import 'antd/dist/antd.css';
import { Tabs, Table, Button } from 'antd';
import "@babel/polyfill";
import axios from 'axios';
const cate_columns = [
    { title: 'Id', dataIndex: 'id', key: 'id' },
    { title: 'Name', dataIndex: 'name', key: 'name' },
    { title: 'Action', dataIndex: '', key: 'x', render: () => <a href="javascript:;">Delete</a> },
  ];


const product_columns = [
    { title: 'Id', dataIndex: 'id', key: 'id' },
    { title: 'Name', dataIndex: 'name', key: 'name' },
    { title: 'Provider', dataIndex: 'provider', key: 'provider' },
    { title: 'Price', dataIndex: 'price', key: 'price' },
    
    { title: 'Action', dataIndex: '', key: 'x', render: () => <a href="javascript:;">Delete</a> },
];
//   const data = [
//     { key: 1, name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park', description: 'My name is John Brown, I am 32 years old, living in New York No. 1 Lake Park.' },
//     { key: 2, name: 'Jim Green', age: 42, address: 'London No. 1 Lake Park', description: 'My name is Jim Green, I am 42 years old, living in London No. 1 Lake Park.' },
//     { key: 3, name: 'Joe Black', age: 32, address: 'Sidney No. 1 Lake Park', description: 'My name is Joe Black, I am 32 years old, living in Sidney No. 1 Lake Park.' },
//   ];
const TabPane = Tabs.TabPane;
class Manager extends Component { 
    constructor(props) { 
        super(props);
        this.state = {};
        this.init_cate();
        this.init_product();
    }


    onChange(key) { 
        console.log("onChange" + key);
        // if (key == "category") {
        //     this.init_cate();
        // } else if (key == "product")
        // { 
        //     this.init_product();
        // }
        
    }

    async init_cate() { 
        let that = this;
        await axios.get('/api/category').then(res => {
            if (res.status == 200) {
                let mystate = {};
                res.data.forEach(e => mystate[e.id] = e.name);
                that.setState(
                    {
                        catedata: res.data,
                        catedict: mystate
                    }
                );     
            }
        });
        console.log(this.state.catedict);
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
    render() { 
        return (
            <div>
                <h1>Managment of Production</h1>
                <Button type="primary">Add Category</Button>
                <Button type="primary">Add Product</Button>
                <Tabs defaultActiveKey="Cate" onChange={key => this.onChange(key)} type="card">
                    <TabPane tab="Category" key="category">
                        <Table
                    columns={cate_columns}
                    dataSource={this.state.catedata}
                /></TabPane>
                    <TabPane tab="Product" key="product" type="card">
                        <Table
                        columns={product_columns}
                            expandedRowRender={record =>
                                <div>
                                <p>
                                    category: {this.state.catedict[record.category_id]}
                                </p>
                                    <p style={{ margin: 0 }}>
                                        description:{record.desc}
                                    </p>
                                </div>
                            }
                            dataSource={this.state.productdata} />
                    </TabPane>
                </Tabs>
            </div>
        )
    }
}

export default Manager;
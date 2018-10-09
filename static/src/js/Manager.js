
import React, { Component } from 'react';
import 'antd/dist/antd.css';
import { Tabs, Table, Button, Modal, Input, Alert, Select,InputNumber } from 'antd';
import "@babel/polyfill";
import axios from 'axios';

const Option = Select.Option;

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


    cate_columns = [
        {
            title: 'Id', dataIndex: 'id', key: 'id', render: text => <a href="javascript:;"
                onClick={e => {
                    this.showedit(e);
                }
                }>{text}</a>
        },
        { title: 'Name', dataIndex: 'name', key: 'name' },
        { title: 'Action', dataIndex: 'id', key: 'x', render: (text) => <a href="javascript:;" onClick={()=>this.delete_cate(text)}>Delete</a> },
    ]
    

    constructor(props) { 
        super(props);
        this.state = {
            alert: false,
            message: "successfull loaded",
            alert_type:"success",
            category_visible: false,
            edit_cate_box: false,
            new_product_box: false,
            edit_product_box:false,
            product_visible: false,
            edit_cate_item: {},
            catedict: {}
        };
        this.editModal = React.createRef();
        this.edit_cate_name = React.createRef();
        this.product_cate = React.createRef();
        this.producte_price = React.createRef();

        this.init_cate();
        this.init_product();
        window.mystate = this.state;
        window.axios = axios;
        window.product_cate = this.product_cate;
        window.product_price = this.producte_price;
    }

    async delete_cate(id) { 
        await axios.delete(`/api/category/${id}`).then(
            res => { 
                if (res.status == 200) {
                    this.setState({
                        message: "successful deleted",
                        alert_type: "success"
                    });
                 }
            }
        ).catch(
            err => { 
                this.setState({
                    message: err.data.message,
                    alert_type: "error"
                });
            }
        )
        this.init_cate();
    }

    async showedit(e) {
        let that = this;
        console.log(e.target.innerText);
        await axios.get(`/api/category/${e.target.innerText}`).then(
            res => {
                if (res.status == 200) { 
                    that.editModal.visible = true;
                    that.setState({
                        edit_cate_item: res.data,
                        edit_cate_box: true
                    });
                }
            }
        )
    }

    async editCategory() {
        console.log(this.state.edit_cate_item);
        await axios.put(`/api/category/${this.state.edit_cate_item.id}`,
            this.state.edit_cate_item).then(
            res => {
                console.log(res.data);
                if (res.status == 201) {
                    this.setState({
                        edit_cate_box: false,
                        alert: true,
                        message: "successfull update item",
                        alert_type: "success",
                    });
                }
            }
        ).catch(err => { 
            this.setState({
                edit_cate_box: false,
                alert: true,
                message: err.data.message,
                alert_type: "error",
            });
        });
        
        this.init_cate();
    }

    editname(e) { 
        let editItem = this.state.edit_cate_item;
        editItem.name = e.target.value;
        this.setState({
            edit_cate_item:editItem
        });
    }
    showCategory() { 
        this.setState({
            category_visible: true
        });
    }
    showProduct() {
        this.setState({
            new_product_box: true
        });
    }

    hideCategory() { 
        this.setState({
            category_visible: false,  
        });
    }

    async addNewCategory() {
        let that = this;
        let myjson = { name: document.getElementById("cate_name").value }
        console.log(myjson);
        await axios.post('/api/category', myjson).then(
            res => { 
                if (res.status == 201) { 
                    that.setState({
                        alert: true,
                        message: "successful add category",
                        alert_type: "success"
                    });
                }
                that.init_cate();
            }
        ).catch(err => { 
            that.setState({
                alert: true,
                message: err.data.message,
                alert_type: "error"
            });
        });
        this.hideCategory();
    }

    async addNewProduct() {
        let newproduct = {};
        newproduct["name"] = document.getElementById("product_name").value;
        newproduct["desc"] = document.getElementById("product_desc").value;
        newproduct["provider"] = document.getElementById("product_provider").value;
        newproduct["barcode"] = document.getElementById("product_barcode").value;
        console.log(this.product_cate);
        console.log(this.product_price.valueOf());
        newproduct["price"] = this.product_price.value;
        newproduct["category_id"] = this.product_cate.value;
        
        console.log(newproduct);
        
        // await axios.post('/api/product')
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
                <Alert banner={this.state.alert} message={this.state.message}
                    type={this.state.alert_type} closable></Alert>
                <Button type="primary" onClick={()=>this.showCategory()}>Add Category</Button>
                <Button type="primary" onClick={()=>this.showProduct()}>Add Product</Button>
                <Modal
                    title="add new Category"
                    visible={this.state.category_visible}
                    onCancel={() => this.hideCategory()}
                    onOk={()=>this.addNewCategory()}>
                    <label for="cate_name">Input category name:</label>
                    <Input type="text" id="cate_name"/>

                </Modal>
                <Modal
                    ref={this.editModal}
                    title="edit Category"
                    visible={this.state.edit_cate_box}
                    onCancel={() => this.setState({edit_cate_box:false})}
                    onOk={() => this.editCategory()}>
                    <p>
                        <lable for="cate_id">Category Id:</lable>
                        <label id>{this.state.edit_cate_item.id}</label>
                    </p>
                    <label for="cate_name">Input category name:</label>
                    <Input type="text" ref="edit_cate_name"
                        value={this.state.edit_cate_item.name}
                        onChange={e=>this.editname(e)}/>
                </Modal>
                <Modal
                    title="add new Product"
                    visible={this.state.new_product_box}
                    onCancel={() => this.setState({ new_product_box: false })}
                    onOk={()=>this.addNewProduct()}>
                    <label for="product_name">Input product name:</label>
                    <Input type="text" id="product_name"/>
                    <label for="product_desc">Input product description:</label>
                    <Input type="text" id="product_desc" />
                    <label for="product_provider">Input product provider:</label>
                    <Input type="text" id="product_provider" />
                    <label for="product_barcode">Input product barcode:</label>
                    <Input type="text" id="product_barcode" />
                    <label for="product_price">Input product price:</label>
                    <InputNumber type="text" ref={this.product_price} step={0.01} min={0}/>
                    <label for="product_cate">Input Category:</label>
                    <Select style={{ width: 200 }} ref={this.product_cate}>
                        {Object.entries(this.state.catedict)
                            .map(en => <Option key={en[0]}>{en[1]}</Option>)}
                    </Select>
                </Modal>
                <Tabs defaultActiveKey="Cate" onChange={key => this.onChange(key)} type="card">
                    <TabPane tab="Category" key="category">
                        <Table
                    columns={this.cate_columns}
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
                                        description: {record.desc}
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
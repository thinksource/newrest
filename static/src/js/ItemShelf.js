import React, { Component } from 'react';
import { Table, Modal } from 'antd';
import axios from 'axios';
import 'antd/dist/antd.css';
const columns = [{
    title: 'Name',
    dataIndex: 'name',
    render: text => <a href="javascript:;">{text}</a>,
  }, {
    title: 'Id',
    dataIndex: 'age',
  }, {
    title: 'Address',
    dataIndex: 'address',
  }];
  const data = [{
    key: '1',
    name: 'John Brown',
    age: 32,
    address: 'New York No. 1 Lake Park',
  }, {
    key: '2',
    name: 'Jim Green',
    age: 42,
    address: 'London No. 1 Lake Park',
  }, {
    key: '3',
    name: 'Joe Black',
    age: 32,
    address: 'Sidney No. 1 Lake Park',
  }, {
    key: '4',
    name: 'Disabled User',
    age: 99,
    address: 'Sidney No. 1 Lake Park',
  }];
  
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
    constructor(props) { 
        super(props);
    }

    rowSelection = {
        onChange: (selectedRowKeys, selectedRows) => { 
            
        }
    }
    render() { 
        return (
            <div>
                <h1>shelf</h1>
                <Table rowSelection={rowSelection} columns={columns} dataSource={data} />
            </div>
        )
    }
}

export default ItemShelf;
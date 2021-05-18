import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import reportWebVitals from '../reportWebVitals';
import TaskTable from './components/TaskTable'
import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'
import { Layout, Breadcrumb,Typography,Modal } from 'antd';
import { UserOutlined, LaptopOutlined, NotificationOutlined } from '@ant-design/icons';

export default class normal_task extends Component {
    render(){
        return(
            <h1>LoopTask</h1>
        //    <TaskTable/>
        )
    }
}

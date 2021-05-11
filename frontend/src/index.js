import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import TaskTable from './components/TaskTable'
import MyMenu from './components/Menu'
import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'
import { Layout, Breadcrumb,Typography } from 'antd';
import { UserOutlined, LaptopOutlined, NotificationOutlined } from '@ant-design/icons';

const { Header, Content, Footer, Sider } = Layout;

ReactDOM.render(
    <Layout>
        <Header className="header" style={{backgroundColor:"#1890ff"}}>
        <Typography>TaskManager</Typography>
        </Header>
        <Layout>
            <Sider theme='light'>
                <MyMenu/>
            </Sider>
            <Content>
                <TaskTable/>
            </Content>
        </Layout>
    </Layout>
    ,  
    document.getElementById('root')
);

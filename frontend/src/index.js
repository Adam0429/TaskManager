import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import NormalTaskPage from './NormalTask/page'
import MyMenu from './components/Menu'
import MyContent from './components/Content'

import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'
import { Layout, Breadcrumb,Typography,Modal } from 'antd';
import { UserOutlined, LaptopOutlined, NotificationOutlined } from '@ant-design/icons';
import Logo from './images/logo.png'
import Icon from '@ant-design/icons';
import { createFromIconfontCN } from '@ant-design/icons';
import PubSub from 'pubsub-js' 

const { Header, Content, Footer, Sider } = Layout;


ReactDOM.render(
    <Layout>
        <Sider>
            <img src={Logo} alt="logo" style={{width: 180}}/>
            <MyMenu/>
        </Sider>
        <MyContent/>
    </Layout>
    ,
    document.getElementById('root')
);

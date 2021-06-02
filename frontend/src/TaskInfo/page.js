import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import reportWebVitals from '../reportWebVitals';
import TaskTable from './components/TaskTable'
import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'
import { Layout, Breadcrumb,Typography,Modal } from 'antd';
import { UserOutlined, LaptopOutlined, NotificationOutlined } from '@ant-design/icons';
import { PageHeader } from 'antd';
import PubSub from 'pubsub-js' 

export default class normal_task extends Component {
    constructor(props){
        super(props)
    }

    handleClick = e => {
		PubSub.publish('menu_back', 1);
	};

    render(){
        return(
            <div>
                  <PageHeader
                        className="site-page-header"
                        onBack={() => this.handleClick()}
                        title="Title"
                        subTitle="This is a subtitle"
                    />,
               <TaskTable task_name={this.props.task_name}/>
            /</div>
        )
    }
}

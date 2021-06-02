import React, { Component } from 'react';
import { Layout } from 'antd';
import PubSub from 'pubsub-js' 
import NormalTaskPage from '../NormalTask/page'
import LoopTaskPage from '../LoopTask/page'
import Monitor from '../Monitor/page'
import TaskInfo from '../TaskInfo/page'

const { Header, Content, Footer, Sider } = Layout;

export default class content extends Component {
    constructor(props) {
        super(props);
        this.state = {
            menu:1,
        };

        PubSub.subscribe('menu', (msg, data) => {
            console.log( msg, data );
            this.last_menu = this.state.menu;
            this.setState({
                menu: data,
            });
        });
        //从task信息页面点击返回按钮，返回上一个页面
        PubSub.subscribe('menu_back', (msg, data) => {
            console.log( msg, data );
            this.setState({
                menu: this.last_menu,
            });
        });
    }
      
    render() {
        let {menu} = this.state
        //数字menu都是正常页面，其他的是task详细页面
        if(menu==1){
            var page = <NormalTaskPage/>
        }
        else if(menu==2){
            var page = <LoopTaskPage/>
        }
        else if(menu==3){
            var page = <Monitor/>
        }
        else{
            var page = <TaskInfo task_name={menu}/>
        }
        return (
            <Content>
                {page}
            </Content>

        );
      }
    }
    
  